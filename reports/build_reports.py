"""Build the two self-contained session deliverables from reviewed source material."""
from pathlib import Path
from collections import Counter
import base64
import csv
import html
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports'
ROWS = list(csv.DictReader((ROOT / 'research/awesome-fly-repositories.csv').open()))
CATEGORIES = list(dict.fromkeys(row['category'] for row in ROWS))
assert len(ROWS) == len({r['repository'] for r in ROWS}) == 96

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

def main():
    report = build_markdown()
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
    manifest = {
        'review_date': '2026-09-25',
        'compiled_on': '2026-09-26',
        'repositories': len(ROWS),
        'category_counts': dict(Counter(r['category'] for r in ROWS)),
        'report_words': len(report.split()),
        'report_sha256': hashlib.sha256(report.encode()).hexdigest(),
        'html_bytes': target.stat().st_size,
        'html_sha256': hashlib.sha256(source.encode()).hexdigest(),
        'scientific_status': 'Literature and repository review; proposed experiment; no simulation executed.',
        'font': {'family': 'Bricolage Grotesque', 'license': 'SIL Open Font License 1.1', 'source': 'https://github.com/google/fonts/tree/main/ofl/bricolagegrotesque'},
    }
    (OUT / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(manifest, indent=2))

if __name__ == '__main__':
    main()
