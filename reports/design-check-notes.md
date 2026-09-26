# Design check notes

The Impeccable mechanical detector ran once on the generated HTML. It reported section-padding, line-height, tracking, and body-font warnings. Visual captures and browser-computed geometry were used to interpret these warnings rather than changing correct rendered CSS to satisfy a static parser.

The section containers use an inset .wrap (110px on a 1440px viewport; 18px on a 390px viewport). The reported line-height ratios of roughly 0.14–0.17 are inconsistent with the computed browser styles: desktop body text is 17px with a 28.05px line height; mobile body text is 16px with a 26.4px line height. Desktop display text is 72px with an 80.64px line height. The detector's reported -0.14em tracking is also inconsistent with the actual -0.025em display rule. The response heading is 31px with -0.775px spacing. Arial is intentionally the body fallback/workhorse face; the display face is embedded Bricolage Grotesque.

The first responsive pass identified a 320px navigation overflow. The final pass fixes it, improves phone diagram labels, and keeps the experiment's comparison table within the mobile viewport. All tested viewports pass. Close-up section screenshots temporarily make the sticky masthead static to prevent capture-tool artifacts; full-page and first-viewport screenshots retain the actual page layout.

No raster imagery ships. The diagram is semantic SVG geometry. The font is embedded as TrueType with its matching MIME/format and preserved OFL license.
