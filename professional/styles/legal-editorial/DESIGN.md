---
version: alpha
name: W230 Legal Editorial
description: Premium legal editorial system for W230 professional-services previews. Client-intake-first, evidence-gated, mobile-first, and calm enough for boutique law firms.
colors:
  primary: "#111111"
  secondary: "#6F6A61"
  tertiary: "#B68A35"
  ink: "#111111"
  ivory: "#F7F2EA"
  paper: "#FFFDF8"
  stone: "#D8CEC0"
  muted: "#6F6A61"
  gold: "#B68A35"
  goldDark: "#7A581D"
  sage: "#879B88"
  paleBlue: "#DDE8EF"
  legalNavy: "#172232"
  danger: "#8F2E21"
typography:
  display:
    fontFamily: Instrument Serif
    fontSize: 4.75rem
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: "-0.045em"
  h1:
    fontFamily: Instrument Serif
    fontSize: 4rem
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: "-0.04em"
  h2:
    fontFamily: Instrument Serif
    fontSize: 2.6rem
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.025em"
  h3:
    fontFamily: Inter
    fontSize: 1.05rem
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
  body-lg:
    fontFamily: Inter
    fontSize: 1.18rem
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: Inter
    fontSize: 0.72rem
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "0.12em"
spacing:
  xs: 6px
  sm: 10px
  md: 16px
  lg: 24px
  xl: 36px
  xxl: 56px
  section: 96px
rounded:
  sm: 6px
  md: 12px
  lg: 22px
  xl: 34px
components:
  disclaimer-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ivory}"
    typography: "{typography.label}"
    padding: 10px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ivory}"
    rounded: "{rounded.sm}"
    padding: 14px
  button-primary-hover:
    backgroundColor: "{colors.goldDark}"
  button-secondary:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 14px
  proof-rail:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  proof-rail-muted:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: 16px
  matter-router-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  matter-router-active:
    backgroundColor: "{colors.paleBlue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  evidence-card:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 18px
  intake-panel:
    backgroundColor: "{colors.legalNavy}"
    textColor: "{colors.ivory}"
    rounded: "{rounded.xl}"
    padding: 28px
  mobile-sticky-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ivory}"
    rounded: "{rounded.lg}"
    padding: 12px
  audit-warning:
    backgroundColor: "{colors.danger}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: 12px
---

## Overview

W230 Legal Editorial is the design contract for premium website rebuilds for boutique professional firms and the previews that sell them. It exists so agents can apply the same calm editorial authority across different professional-service previews without copying vibes.

The system should make a firm look as credible online as it is in the room. The interface is client-intake-first: stressed visitors should see their legal problem, choose the right pathway, and understand the next action without decoding a firm’s internal practice taxonomy.

The commercial job is perception-gap proof. Each preview should show that W230 understands the firm’s website problem better than the current site does. That means real public proof signals, a visible matter router, mobile-first conversion, and no invented claims.

## Colors

- **Ink (#111111):** Pure black authority. Use for headlines, primary text, and high-emphasis CTAs.
- **Ivory (#F7F2EA):** Warm legal paper. Use as the main page background when the page needs calm authority.
- **Paper (#FFFDF8):** Clean card surface for proof rails, intake summaries, and decision cards.
- **Stone (#D8CEC0):** Thin rules, dividers, table borders, and low-emphasis geometry.
- **Muted (#6F6A61):** Secondary copy. Never use for primary legal promises.
- **Gold (#B68A35):** Warm premium accent. Use sparingly for proof labels, active router states, and small folio marks.
- **Sage (#879B88):** Calm trust accent for secondary panels and archive-style metadata.
- **Pale blue (#DDE8EF):** Low-pressure informational tint for client guidance states.
- **Legal navy (#172232):** Deep contrast panel for mocked intake, partner view, or operational handoff.
- **Danger (#8F2E21):** Only for audit warnings inside W230-facing materials. Do not use as public shame language.

## Typography

Use an editorial serif for authority, not fake luxury. Use a clean sans for instructions and intake controls.

- **Display / H1 / H2:** Instrument Serif. Large, tight, calm. Avoid stacked marketing slogans.
- **Body / labels / controls:** Inter. Plain, readable, fast to scan.
- **Labels:** All-caps, small, letter-spaced. Use for proof labels like `PUBLIC PROOF SIGNAL`, not for shouting.

Hierarchy rule: one meaningful H1 per page. Slider H1s, repeated service headings, and generic “Welcome” hero language are the exact failure modes these previews should repair.

## Layout

Pages should read like a legal intake conversation, not a brochure.

Preferred sequence:

1. Independent concept disclaimer.
2. Firm name plus W230 concept-preview label.
3. Outcome-led hero.
4. Proof rail using only public-source facts.
5. Four-or-fewer client decision cards.
6. One real matter router for the highest-intent path.
7. Mobile-first demonstration.
8. Mock intake and partner-view panel.
9. Before/current vs preview direction.
10. Contact section using public contact details.

Use generous whitespace, thin dividers, folio-style panels, and one high-emphasis CTA per viewport. Every section needs a job. Remove decorative sections that do not improve trust, routing, or conversion.

## Elevation & Depth

Keep depth physical and editorial, not SaaS-glossy.

- Use subtle 1px borders in Stone.
- Use layered paper panels with small offsets.
- Use restrained shadows only where hierarchy needs separation.
- Avoid glassmorphism, neon glows, purple gradients, plastic AI shine, and animated sparkle motifs.

## Shapes

Shapes should feel like legal stationery and archive cards.

- Cards: 22px radius maximum.
- Buttons: 6px radius, mostly rectangular.
- Intake panels: larger radius allowed because they represent a product surface.
- Dividers: thin, black/stone, editorial.

Avoid pill overload. Rounded shapes should not make a law firm look like a consumer SaaS app.

## Components

Core reusable components:

- `disclaimer-strip`: visible no-affiliation statement. Mandatory on unsolicited previews.
- `proof-rail`: source-attributed credibility strip. Use public facts only.
- `matter-router-card`: the strategic core. Collapse internal legal taxonomy into user problems.
- `intake-panel`: mocked operational handoff. Shows what the firm receives, not just what the client sees.
- `mobile-sticky-cta`: mobile sticky CTA and mobile-first proof that high-intent users can act immediately.
- `button-primary`: one primary action per screen.
- `button-secondary`: lower-emphasis action for review/learn-more links.

The matter router is the sale. If the page only has static service cards, it has failed the W230 professional-services standard.

## Do's and Don'ts

Do:

- Ground every proof signal in public source material.
- Use client language: buying property, starting a business, family issue, visa pathway.
- Show the mobile flow as a first-class artifact.
- Preserve real credibility signals if they are public.
- Make the next step obvious without legal overclaiming.
- Treat DESIGN.md as the taste contract for future agents.

Don't:

- Do not invent awards, testimonials, outcomes, reviews, lawyers, case results, or availability claims.
- Do not call out typos or spelling mistakes in public-facing outreach or previews.
- Do not use purple AI slop, fake luxury, startup gradients, or overanimated agency design.
- Do not lead with price or cheap-web-design positioning.
- Do not mirror the firm’s long internal practice taxonomy as the main UX.
