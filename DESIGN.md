---
name: Firebird research reports
description: A readable systems worksheet for evidence and proposed experiments.
colors:
  ink: "#183d33"
  field: "#d6ed9e"
  field-ink: "#213d1c"
  purple: "#493663"
  lilac: "#efe9f6"
  paper: "#fafcf8"
  muted: "#486457"
  line: "#b7c9bc"
  soft: "#edf3e9"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Bricolage, Arial, sans-serif"
    fontSize: "clamp(44px, 5.2vw, 72px)"
    fontWeight: 650
    lineHeight: 1.12
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Bricolage, Arial, sans-serif"
    fontSize: "clamp(32px, 3.4vw, 46px)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Bricolage, Arial, sans-serif"
    fontSize: "25px"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.4
rounded:
  control: "6px"
  diagram-node: "8px"
  explorer: "12px"
spacing:
  compact: "8px"
  control: "16px"
  inset: "24px"
  panel: "30px"
  columns: "56px"
  section: "82px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
    typography: "{typography.label}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
    typography: "{typography.label}"
  search-input:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "11px 14px"
  explorer:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.explorer}"
---

# Design System: Firebird research reports

## Overview

**Creative North Star: "The systems worksheet"**

The report uses causal diagrams, comparison tables, and clear reading fields to explain relationships. Green establishes the principal worksheet; pine text and fine rules organize the reading surface.

Detail is available through native disclosures and a searchable directory. This document records the implemented report, not an organization-wide brand commitment.

**Key Characteristics:**
- Geometric causal diagrams with readable labels.
- Strong display type paired with simple body text.
- Tonal fields and rules instead of shadows.
- Native controls and progressive disclosure.

## Colors

Primary field green supports the hero, selected controls, selection highlighting, and the download action on dark ground. Pine ink carries text and primary controls. Paper, white, and soft green distinguish reading areas without elevation.

Purple and lilac identify added physiology and explanatory notes. Purple also appears in the suppressed-signal output and keyboard focus; it is not an exclusive scientific-status code. Text and shapes carry the meaning alongside color.

**The Redundant Signal Rule.** State and evidence distinctions must remain understandable from labels and shapes without color.

## Typography

Bricolage Grotesque is embedded as TrueType under the Open Font License. The CSS family is Bricolage. Arial and Helvetica provide the body stack. The frontmatter records the desktop hierarchy; local components have documented smaller type.

Body measure is capped at 70ch where the reading layout allows it. At 760px and below, body text is 16px, the main heading is 49px with 1.03 leading, and section headings are 35px. At 360px and below the main heading is 43px.

**The Heading Carries the Action Rule.** Put the action into the heading rather than adding an eyebrow above it. Supporting state text follows the result heading.

## Layout

The content wrapper is capped at 1220px, with 40px minimum side margins on the broad layout, 24px below 1100px, and 18px below 760px. The hero and section introductions use two columns on desktop and one on mobile. Standard sections use 82px vertical padding, reduced to 52px on phones.

The masthead stays at the top during reading; mobile navigation occupies a second row. Less essential navigation links disappear below 360px. The experiment panel stacks on phones, with its two control groups remaining side by side until 360px. The core condition table fits the phone width; larger technical tables may scroll horizontally.

## Elevation & Depth

The design is flat. Tonal fields, whitespace, and one-pixel borders separate regions. There are no box shadows or decorative glows.

**The Flat Surface Rule.** Use tonal separation and boundaries to organize the report rather than adding elevation.

## Shapes

Controls use gently rounded corners, diagram nodes use slightly larger corners, and the experiment container uses the largest documented radius. Crisp SVG paths draw the causal arrows and disclosure chevrons. Filled squares, outlined circles, and dashed shapes distinguish the evidence key.

## Components

Buttons have visible hover and focus states; the minimum default height is 44px. The masthead uses more compact mobile sizing. Inputs are white with a one-pixel border and visible labels. Radio controls preserve native semantics while their enclosing labels show selection with a field-green fill.

Native details/summary elements expose technical notes and repository entries. Authored SVG chevrons rotate when open. The directory disclosure encloses labeled search and category controls, an announced result count, and a clear empty state with a reset action.

The condition explorer announces its selected result politely. Its state labels describe published qualitative evidence. Print hides controls, expands technical details, keeps the complete condition matrix, and omits the long repository inventory. The embedded Markdown download contains that full inventory.

Focus uses a three-pixel outline with a five-pixel offset. Selection and caret colors belong to the palette. Smooth anchor scrolling is disabled when reduced motion is requested.

## Do's and Don'ts

- Do keep citations close to the claims they support.
- Do preserve native form and disclosure semantics.
- Do pair every color-coded distinction with meaningful text or geometry.
- Don't present the qualitative explorer as an executing neural simulation.
- Don't add external font or script dependencies to the shareable file.
- Don't encode state only through color.
