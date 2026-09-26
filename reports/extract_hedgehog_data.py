"""Extract selected published measurements for the report; does not fit a model.

Usage: python3 reports/extract_hedgehog_data.py /path/to/source-data.xlsx
The source workbook is pinned by SHA-256. All exported values retain source cells.
"""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import statistics
import sys
import xml.etree.ElementTree as ET
import zipfile

EXPECTED_SHA256 = '41deeecbecbcc97d0c1336c4b1aaf009b3723b93c396086c0cc0ba1fb4866667'
FILENAME = '41467_2022_35527_MOESM3_ESM.xlsx'
SOURCE_URL = 'https://media.springernature.com/full/springer-static/esm/art%3A10.1038%2Fs41467-022-35527-4/MediaObjects/' + FILENAME
MIRROR_URL = 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9763350/supplementaryFiles'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL_ID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
OUT = Path(__file__).resolve().parent


def read_workbook(raw):
    sheets = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        shared = [''.join(e.itertext()) for e in ET.fromstring(
            archive.read('xl/sharedStrings.xml')).findall('m:si', NS)]
        rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(
            archive.read('xl/_rels/workbook.xml.rels'))}
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        for sheet in workbook.find('m:sheets', NS):
            target = rels[sheet.get(REL_ID)]
            path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            cells = {}
            for cell in ET.fromstring(archive.read(path)).findall('m:sheetData/m:row/m:c', NS):
                value = cell.find('m:v', NS)
                inline = cell.find('m:is', NS)
                if value is not None:
                    text = shared[int(value.text)] if cell.get('t') == 's' else value.text
                elif inline is not None:
                    text = ''.join(inline.itertext())
                else:
                    continue
                if text is not None and text.strip():
                    cells[cell.get('r')] = text
            sheets[sheet.get('name')] = cells
    return sheets


def column_number(ref):
    number = 0
    for char in re.match(r'[A-Z]+', ref).group():
        number = number * 26 + ord(char) - ord('A') + 1
    return number


def row_values(cells, row, first, last):
    return [(ref, float(value)) for ref, value in cells.items()
            if int(re.search(r'\d+', ref).group()) == row
            and first <= column_number(ref) <= last]


def write_csv(name, records):
    path = OUT / 'data' / name
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    return {'path': 'reports/data/' + name, 'rows': len(records),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raw = Path(sys.argv[1]).read_bytes()
    if hashlib.sha256(raw).hexdigest() != EXPECTED_SHA256:
        raise SystemExit('Workbook differs from the reviewed version; review before changing the pin.')
    sheets = read_workbook(raw)
    (OUT / 'data').mkdir(exist_ok=True)
    per = []
    for first_row, fraction in [(3, .06), (12, .075), (21, .10), (30, .15), (39, .34)]:
        for row in range(first_row, first_row + 7):
            concentration = float(sheets['Fig 1'][f'B{row}'])
            for ref, value in row_values(sheets['Fig 1'], row, 3, 100):
                per.append({'panel': '1b', 'sheet': 'Fig 1', 'cell': ref,
                            'diet_sucrose_fraction': fraction, 'stimulus': 'sucrose',
                            'stimulus_mM': concentration, 'per_percent': value})
    sensory = []
    for row in range(3, 8):
        concentration = float(sheets['Fig 7'][f'A{row}'])
        for genotype, first, last in [('Mex-Gal4', 2, 12), ('Mex-Gal4>UAS-Hh-RNAi', 13, 23)]:
            for ref, value in row_values(sheets['Fig 7'], row, first, last):
                sensory.append({'panel': '7b', 'sheet': 'Fig 7', 'cell': ref,
                                'genotype': genotype, 'stimulus': 'L-glucose',
                                'stimulus_mM': concentration,
                                'evoked_spikes_per_3s': value,
                                'derived_mean_evoked_spikes_per_s': value / 3})
    protein = []
    for row, panel, condition in [(77, '4d', 'w1118; 6% diet'),
                                  (78, '4d', 'w1118; 34% diet'),
                                  (109, '4f', 'Mex-Gal4/+; 34% diet'),
                                  (110, '4f', 'Mex-Gal4/Hh-IR; 34% diet'),
                                  (111, '4f', 'Mex-Gal4/; disp-IR/+; 34% diet')]:
        for ref, value in row_values(sheets['Fig 4'], row, 2, 5):
            protein.append({'panel': panel, 'sheet': 'Fig 4', 'cell': ref,
                            'condition': condition, 'relative_Hh_protein': value})
    assert len(per) == 1071 and len(sensory) == 76 and len(protein) == 17
    outputs = [write_csv('hedgehog-per-fig1b.csv', per),
               write_csv('hedgehog-sensory-fig7b.csv', sensory),
               write_csv('hedgehog-protein-fig4.csv', protein)]
    examples = []
    for fraction in [.06, .34]:
        subset = [r for r in per if r['diet_sucrose_fraction'] == fraction and r['stimulus_mM'] == 100]
        examples.append({'panel': '1b', 'diet_sucrose_fraction': fraction,
                         'stimulus': '100 mM sucrose', 'n_fly_aggregates': len(subset),
                         'mean_per_percent': statistics.mean(r['per_percent'] for r in subset)})
    for genotype in ['Mex-Gal4', 'Mex-Gal4>UAS-Hh-RNAi']:
        subset = [r for r in sensory if r['genotype'] == genotype and r['stimulus_mM'] == 100]
        examples.append({'panel': '7b', 'genotype': genotype, 'stimulus': '100 mM L-glucose',
                         'n_sensillum_records': len(subset),
                         'mean_evoked_spikes_per_3s': statistics.mean(r['evoked_spikes_per_3s'] for r in subset),
                         'derived_mean_evoked_spikes_per_s': statistics.mean(r['derived_mean_evoked_spikes_per_s'] for r in subset)})
    # Verify the repeated block used to explain why panel-level splitting can leak data.
    repeated = all([v for _, v in row_values(sheets['Fig 1'], row, 3, 41)] ==
                   [v for _, v in row_values(sheets['Fig 3'], row + 42, 3, 41)]
                   for row in range(3, 10))
    assert repeated
    audit = {
        'reviewed_on': '2026-09-26',
        'paper': {'title': 'Hedgehog-mediated gut-taste neuron axis controls sweet perception in Drosophila',
                  'authors': 'Zhao et al.', 'year': 2022,
                  'doi': '10.1038/s41467-022-35527-4',
                  'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9763350/',
                  'license': 'CC BY 4.0', 'license_url': 'https://creativecommons.org/licenses/by/4.0/'},
        'workbook': {'filename': FILENAME, 'bytes': len(raw), 'sha256': EXPECTED_SHA256,
                     'publisher_url': SOURCE_URL, 'mirror_archive_url': MIRROR_URL,
                     'publisher_and_mirror_bytes_matched': True,
                     'sheets': [{'name': name, 'nonempty_cells': len(cells)} for name, cells in sheets.items()]},
        'exports': outputs,
        'transformations': ['Selected numerical cells exported with original sheet/cell provenance.',
                            'Fig 1b diet fractions carried down their seven-row blocks.',
                            'Fig 7b three-second evoked counts also expressed as a mean per second; not instantaneous firing or baseline activity.',
                            'No concentration, age, genotype, batch, or per-fly pairing harmonization performed.',
                            'Means calculated directly from rounded workbook values; no significance reanalysis.'],
        'example_summaries': examples,
        'quality_and_compatibility_notes': [
            'Fig 1b uses sucrose; Fig 7b uses L-glucose. Equal mM does not establish equal sensory input.',
            'Main methods describe PER four days after diet switch and electrophysiology at age 8-10 days.',
            'PER entries are percentages of three trials per fly. Source columns are not verified cross-condition fly identifiers.',
            'Fig 7 recordings are sensillum measurements nested within flies, not independent animal replicates.',
            'Fig 3 axes show log10 relative expression. Negative values must not be interpreted as negative protein concentration.',
            'Fig 4d and 4f use different genotype comparisons and normalization contexts; do not pool scales without checking.',
            'Fig 1b C3:AO9 exactly repeats in Fig 3g C45:AO51. Do not count as independent validation.',
            'Fig 3f row labels for 34% and 34%>6% appear inconsistent with the corresponding arrays in Fig 3e; quarantine pending clarification.',
            'Fig 7f workbook cell A27 labels diet 0.34, while the published panel and caption say 15%; quarantine pending clarification.'
        ],
        'followup_paper': {'year': 2023, 'doi': '10.1016/j.celrep.2023.113387',
                           'url': 'https://pubmed.ncbi.nlm.nih.gov/37934669/',
                           'role': 'Related same-group taste-balancing study; candidate future comparison, not independent-laboratory replication.',
                           'data_availability': 'Article states reported data are available from lead contact on request; not acquired here.'},
        'status': {'selected_source_data_extracted': True, 'model_fitted': False,
                   'neural_simulation_run_for_this_followup': False, 'biological_validation_completed': False}
    }
    (OUT / 'hedgehog-data-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
    print(json.dumps({'sheets': len(sheets), 'exports': outputs,
                      'status': 'Source-data extraction only; no model fit or biological validation.'}, indent=2))


if __name__ == '__main__':
    main()
