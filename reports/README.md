# Session reports

Written reports and the preserved presentation:

- [session-research-report.md](session-research-report.md) — comprehensive research synthesis, proposed experiments, validation plan, focused feeding and neuromodulation reviews, critical assessment, and the original 96 repository entries.
- [experiment-critique.md](experiment-critique.md) — separate critic-agent assessment of both proposals, strongest objections, evidence versus inference, smallest defensible experiments, and conditions for proceeding or narrowing the claims.
- [neuromodulation-doom-experiment.md](neuromodulation-doom-experiment.md) — assessment of dopamine, octopamine, tyramine, and cortisol; pinned DOOMFLY code findings; proposed assays, controls, and visual demonstration.
- [hedgehog-experiment-data-and-value.md](hedgehog-experiment-data-and-value.md) — original idea, validation standard, real Hedgehog dataset mapping, compatibility gaps, feedback stages, and practical value.
- [fly-project-brief.html](fly-project-brief.html) — shareable briefing for a mixed technical audience, preserved at the feeding-review snapshot. Open it in a modern browser. The single file includes its font, styles, diagram, qualitative evidence explorer, searchable repository directory, and a downloadable copy of the earlier Markdown report.

**Update preference, 26 September 2026:** update written reports only unless the user explicitly requests changes to the HTML presentation. Its embedded Markdown download is intentionally an older snapshot; use the standalone Markdown files above for the latest findings.

The HTML works offline. External citations need internet access. Its Print button supports printing or saving the briefing as PDF; the full 96-entry directory is omitted from that print layout and remains available in the Markdown report. The interactive explorer summarizes published qualitative findings and does not run a neural simulation.

Collection snapshot: September 25, 2026. Focused feeding-repository review and compilation: September 26, 2026. The original 96-entry inventory is preserved; the additional review brings the total to 97 distinct repositories. The new [feeding audit](../research/fly-brain-feeding-audit.json) pins commit 86c7d84 and records the 15 passing repository tests. Our proposed Hedgehog extension remains unimplemented and has no biological validation.

The September 26 [neuromodulation audit](neuromodulation-source-audit.json) pins DOOMFLY at 71ecf53 and documents the literature and selected code inspection. That repository was already in the collection, so the total remains 97. No Doom simulation or new chemical intervention was run for this follow-up.

The [Hedgehog data audit](hedgehog-data-audit.json) pins the downloaded 2022 source workbook and three selected CSV extracts in data/. These contain 1,164 measurement entries, not independent animal counts. The data were inspected and summarized; a physiological model has not been fitted or validated. Source measurements are credited to Zhao et al. (2022), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); extraction and the indicated unit conversion are documented in the audit.

The September 26 [critic review](experiment-critique.md) revised the next milestone to a small Hedgehog feasibility and model-comparison study. Octopamine remains an alternative on an established visual model; dopamine–Doom is deferred until sensory and conditioning prerequisites pass. Its findings are integrated into both focused reports and Section 13 of the comprehensive report. The review involved literature and selected code inspection, with no new simulations or empirical replication.

## Rebuilding

Run `python3 reports/build_reports.py` from the workspace root. It rebuilds the comprehensive Markdown report from session-report-core.md and the original reviewed CSV, then records the current report hashes and audit references in build-manifest.json. Edit the core source and the standalone reports directly. The default command does not write either HTML file.

To reproduce the selected Hedgehog data extracts, download the workbook linked in [hedgehog-data-audit.json](hedgehog-data-audit.json) and run `python3 reports/extract_hedgehog_data.py /path/to/41467_2022_35527_MOESM3_ESM.xlsx`. The standard-library script checks the source hash before writing the CSVs and audit. The full workbook is not stored in this repository. Then rebuild the report manifest with the command above.

Only after an explicit presentation-update request, `python3 reports/build_reports.py --with-html` also rebuilds the HTML from fly-project-brief.template.html, the current comprehensive report, and the licensed font in assets/. The manifest records whether the HTML embeds the current report or an earlier snapshot.

Browser verification of the preserved presentation is recorded in verification-results.json. The download check now compares against the embedded snapshot hash in the manifest, allowing the written report to advance independently. The browser suite was not rerun for this report-only update; both HTML files retain their verified hashes. The verification script uses Playwright installed in the session's temporary build directory and the local Google Chrome executable; those paths need adjustment on another machine. Screenshots and the print check are development evidence under ../.impeccable/review/ and are not needed to share or open the HTML.

The Bricolage Grotesque font is redistributed under the SIL Open Font License 1.1. Its license is included beside the font and inside the HTML.
