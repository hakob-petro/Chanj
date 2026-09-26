"""Build written reports; rebuild the HTML snapshot only with --with-html."""
from pathlib import Path
from collections import Counter
import argparse
import base64
import csv
import html
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports'
ROWS = list(csv.DictReader((ROOT / 'research/awesome-fly-repositories.csv').open()))
FEEDING_REVIEW = json.loads((ROOT / 'research/fly-brain-feeding-audit.json').read_text())
CATEGORIES = list(dict.fromkeys(row['category'] for row in ROWS))
assert len(ROWS) == len({r['repository'] for r in ROWS}) == 96
assert FEEDING_REVIEW['repository'] not in {r['repository'] for r in ROWS}

def escape(value):
    return html.escape(str(value), quote=True)

def build_markdown():
    source = (OUT / 'session-report-core.md').read_text()
    counts = Counter(r['category'] for r in ROWS)
    table = '| Category | Repositories |\n|---|---:|\n' + ''.join(
        f'| {category} | {counts[category]} |\n' for category in CATEGORIES
    ) + '| **Total** | **96** |'
    entries = []
    for category in CATEGORIES:
        entries.append(f'### {category}\n')
        for r in ROWS:
            if r['category'] != category:
                continue
            entries.append(
                f"#### {r['number']}. [{r['title']}]({r['url']})\n\n"
                f"Repository: {r['repository']}\n\n"
                f"**Purpose.** {r['purpose']}\n\n"
                f"**Biological substrate.** {r['substrate']}.\n\n"
                f"**Method.** {r['method']}\n\n"
                f"**Evidence and limits.** {r['evidence_and_limits']}\n\n"
                f"**Potential reuse.** {r['reusable_contribution']}\n"
            )
    report = source.replace('<!-- CATEGORY_TABLE -->', table).replace(
        '<!-- REPOSITORY_CATALOG -->', '\n'.join(entries)
    )
    (OUT / 'session-research-report.md').write_text(report)
    return report

def build_catalog():
    entries = []
    for r in ROWS:
        search = ' '.join(r.values()).lower()
        entries.append(f'''<details class="repo" data-category="{escape(r['category'])}" data-search="{escape(search)}">
<summary><span class="repo-number">{int(r['number']):02d}</span><span class="repo-heading"><strong>{escape(r['title'])}</strong><span>{escape(r['purpose'])}</span></span><span class="repo-category">{escape(r['category'])}</span><svg class="disclosure-icon" viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m5 7 5 5 5-5"/></svg></summary>
<div class="repo-content"><p><a href="{escape(r['url'])}">{escape(r['repository'])}</a></p><dl>
<dt>Substrate</dt><dd>{escape(r['substrate'])}</dd>
<dt>Method</dt><dd>{escape(r['method'])}</dd>
<dt>Evidence &amp; limits</dt><dd>{escape(r['evidence_and_limits'])}</dd>
<dt>Potential reuse</dt><dd>{escape(r['reusable_contribution'])}</dd>
</dl></div></details>''')
    return '\n'.join(entries)

def build_html(report):
    font_path = OUT / 'assets/heading.ttf'
    if not font_path.exists():
        raise SystemExit('Missing reports/assets/heading.ttf. Restore the licensed font asset before building.')
    font = base64.b64encode(font_path.read_bytes()).decode()
    options = ''.join(f'<option value="{escape(c)}">{escape(c)}</option>' for c in CATEGORIES)
    source = (OUT / 'fly-project-brief.template.html').read_text()
    tokens = {
        '@@FONT@@': font,
        '@@REPORT@@': base64.b64encode(report.encode()).decode(),
        '@@CATALOG@@': build_catalog(),
        '@@CATEGORY_OPTIONS@@': options,
        '@@LICENSE@@': escape((OUT / 'assets/OFL.txt').read_text()),
    }
    for token, value in tokens.items():
        source = source.replace(token, value)
    assert not any(token in source for token in tokens)
    target = OUT / 'fly-project-brief.html'
    target.write_text(source)
    return source

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--with-html', action='store_true',
                        help='Also rebuild the HTML presentation, only when explicitly requested.')
    args = parser.parse_args()
    report = build_markdown()
    target = OUT / 'fly-project-brief.html'
    if args.with_html:
        build_html(report)
    html_bytes = target.read_bytes() if target.exists() else None
    embedded = re.search(rb'<script id="report-data"[^>]*>([^<]+)</script>', html_bytes) if html_bytes else None
    embedded_sha = hashlib.sha256(base64.b64decode(embedded.group(1))).hexdigest() if embedded else None
    neuromodulation_review = json.loads((OUT / 'neuromodulation-source-audit.json').read_text())
    neuromodulation_report = (OUT / 'neuromodulation-doom-experiment.md').read_bytes()
    hedgehog_report = (OUT / 'hedgehog-experiment-data-and-value.md').read_bytes()
    critique_report = (OUT / 'experiment-critique.md').read_bytes()
    alternative_report = (OUT / 'alternative-experiment-proposals.md').read_bytes()
    alternative_audit_bytes = (OUT / 'alternative-experiments-audit.json').read_bytes()
    alternative_audit = json.loads(alternative_audit_bytes)
    hedgehog_audit = json.loads((OUT / 'hedgehog-data-audit.json').read_text())
    manifest = {
        'review_date': FEEDING_REVIEW['reviewed_on'],
        'collection_review_date': '2026-09-25',
        'compiled_on': '2026-09-26',
        'repositories': len(ROWS) + 1,
        'repository_count_scope': 'Original 96-entry catalog plus feeding review; excludes code inspected in the later alternative-experiment search.',
        'catalog_repositories': len(ROWS),
        'additional_repository_reviews': [{
            'repository': FEEDING_REVIEW['repository'],
            'commit': FEEDING_REVIEW['commit'],
            'reviewed_on': FEEDING_REVIEW['reviewed_on'],
            'tests_passed': FEEDING_REVIEW['local_verification']['passed'],
            'audit': 'research/fly-brain-feeding-audit.json',
        }],
        'focused_repository_reinspections': [{
            'repository': neuromodulation_review['repository'],
            'commit': neuromodulation_review['commit'],
            'reviewed_on': neuromodulation_review['reviewed_on'],
            'audit': 'reports/neuromodulation-source-audit.json',
            'simulation_rerun': False,
        }],
        'category_counts': dict(Counter(r['category'] for r in ROWS)),
        'report_words': len(report.split()),
        'report_sha256': hashlib.sha256(report.encode()).hexdigest(),
        'neuromodulation_report': {
            'path': 'reports/neuromodulation-doom-experiment.md',
            'words': len(neuromodulation_report.decode().split()),
            'sha256': hashlib.sha256(neuromodulation_report).hexdigest(),
        },
        'hedgehog_report': {
            'path': 'reports/hedgehog-experiment-data-and-value.md',
            'words': len(hedgehog_report.decode().split()),
            'sha256': hashlib.sha256(hedgehog_report).hexdigest(),
        },
        'critique_report': {
            'path': 'reports/experiment-critique.md',
            'words': len(critique_report.decode().split()),
            'sha256': hashlib.sha256(critique_report).hexdigest(),
            'review_type': 'Separate critic-agent literature and selected code review',
            'simulation_rerun': False,
        },
        'alternative_experiment_report': {
            'path': 'reports/alternative-experiment-proposals.md',
            'words': len(alternative_report.decode().split()),
            'sha256': hashlib.sha256(alternative_report).hexdigest(),
            'audit': 'reports/alternative-experiments-audit.json',
            'audit_sha256': hashlib.sha256(alternative_audit_bytes).hexdigest(),
            'search_branches': alternative_audit['review_method']['search_branches'],
            'shortlisted_candidates': alternative_audit['review_method']['shortlisted_candidates'],
            'dedicated_critics': alternative_audit['review_method']['dedicated_critics'],
            'selected_candidates': alternative_audit['review_method']['selection'],
            'model_execution': False,
            'biological_validation': False,
        },
        'hedgehog_data': {
            'audit': 'reports/hedgehog-data-audit.json',
            'source_workbook_sha256': hedgehog_audit['workbook']['sha256'],
            'exports': hedgehog_audit['exports'],
            'status': 'Selected published measurements extracted; no physiological model fitted or biologically validated.',
        },
        'html_bytes': len(html_bytes) if html_bytes is not None else None,
        'html_sha256': hashlib.sha256(html_bytes).hexdigest() if html_bytes is not None else None,
        'html_embedded_report_sha256': embedded_sha,
        'html_embeds_current_report': embedded_sha == hashlib.sha256(report.encode()).hexdigest(),
        'update_policy': 'Written reports only by default; preserve HTML and its embedded report snapshot unless a presentation rebuild is explicitly requested.',
        'scientific_status': 'Literature and repository review; 15 included fly-brain-feeding software tests previously rerun successfully. Hedgehog source workbook inspected and selected measurements extracted. Original critique followed by three search branches and three dedicated critics reviewing nine alternative assays. Current first recommendation: bounded visual motion-opponency reproduction; neural compass is an alternative and feeding sequencing is conditional. Selected published numerical data inspected, but no alternative model executed, fitted, trained, or biologically validated. Hedgehog and neuromodulation extensions remain unimplemented; DOOMFLY simulation not rerun.',
        'font': {'family': 'Bricolage Grotesque', 'license': 'SIL Open Font License 1.1', 'source': 'https://github.com/google/fonts/tree/main/ofl/bricolagegrotesque'},
    }
    (OUT / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(manifest, indent=2))

if __name__ == '__main__':
    main()
