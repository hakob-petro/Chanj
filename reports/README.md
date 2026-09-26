# Session reports

Two deliverables:

- [session-research-report.md](session-research-report.md) — comprehensive research synthesis, proposed experiment, validation plan, and all 96 reviewed repository entries.
- [fly-project-brief.html](fly-project-brief.html) — shareable briefing for a mixed technical audience. Open it in a modern browser. The single file includes its font, styles, diagram, qualitative evidence explorer, searchable repository directory, and a downloadable copy of the full Markdown report.

The HTML works offline. External citations need internet access. Its Print button supports printing or saving the briefing as PDF; the full 96-entry directory is omitted from that print layout and remains available in the Markdown report. The interactive explorer summarizes published qualitative findings and does not run a neural simulation.

Research snapshot: September 25, 2026. Compilation: September 26, 2026. The original source audits remain in ../research/.

## Rebuilding

Run `python3 reports/build_reports.py` from the workspace root. It uses the reviewed CSV, session-report-core.md, fly-project-brief.template.html, and the licensed font in assets/. The two deliverables are generated; edit their source files before rebuilding.

Browser verification is recorded in verification-results.json. The verification script uses Playwright installed in the session's temporary build directory and the local Google Chrome executable; those paths need adjustment on another machine. Screenshots and the print check are development evidence under ../.impeccable/review/ and are not needed to share or open the HTML.

The Bricolage Grotesque font is redistributed under the SIL Open Font License 1.1. Its license is included beside the font and inside the HTML.
