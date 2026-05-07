---
version: beta
name: W230 Legal Editorial
description: >
  Premium legal editorial design system for W230 professional-services previews.
  Client-intake-first, evidence-gated, mobile-first, calm, credible, and suitable
  for boutique law firms and high-trust advisory firms.
systemIntent:
  primary: "Make the firm feel as credible online as it already is in the room."
  commercial: "Reveal the perception gap between the current website and a clearer client-intake experience."
  strategic: "Turn public credibility into structured client action."
  nonGoal: "Do not make the firm look trendy, cheap, AI-generated, or like a generic SaaS landing page."
principles:
  - "Client problem before firm taxonomy."
  - "Evidence before persuasion."
  - "One high-intent action per viewport."
  - "Mobile is the primary conversion surface."
  - "Calm authority beats decorative luxury."
  - "No invented proof. No fake outcomes. No synthetic credibility."
  - "The matter router is the product demonstration."
colors:
  ink: "#111111"
  charcoal: "#24211D"
  muted: "#6F6A61"
  ivory: "#F7F2EA"
  paper: "#FFFDF8"
  stone: "#D8CEC0"
  stoneLight: "#E8DED0"
  gold: "#B68A35"
  goldDark: "#7A581D"
  sage: "#879B88"
  paleBlue: "#DDE8EF"
  legalNavy: "#172232"
  danger: "#8F2E21"
  success: "#536B57"
colorRoles:
  backgroundPrimary: "{colors.ivory}"
  backgroundCard: "{colors.paper}"
  textPrimary: "{colors.ink}"
  textSecondary: "{colors.muted}"
  borderSubtle: "{colors.stone}"
  accentPremium: "{colors.gold}"
  panelDark: "{colors.legalNavy}"
  guidanceTint: "{colors.paleBlue}"
  auditOnly: "{colors.danger}"
typography:
  display:
    fontFamily: "Instrument Serif"
    fontSize:
      desktop: "5.2rem"
      tablet: "4rem"
      mobile: "3rem"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "-0.05em"
  h1:
    fontFamily: "Instrument Serif"
    fontSize:
      desktop: "4.4rem"
      tablet: "3.4rem"
      mobile: "2.65rem"
    fontWeight: 400
    lineHeight: 0.94
    letterSpacing: "-0.045em"
  h2:
    fontFamily: "Instrument Serif"
    fontSize:
      desktop: "2.8rem"
      tablet: "2.35rem"
      mobile: "2rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.025em"
  h3:
    fontFamily: "Inter"
    fontSize: "1.05rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Inter"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.65
  bodyLarge:
    fontFamily: "Inter"
    fontSize: "1.18rem"
    fontWeight: 400
    lineHeight: 1.7
  small:
    fontFamily: "Inter"
    fontSize: "0.84rem"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Inter"
    fontSize: "0.72rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "0.12em"
    textTransform: "uppercase"
grid:
  pageMaxWidth: "1240px"
  contentMaxWidth: "760px"
  narrowMaxWidth: "620px"
  columnsDesktop: 12
  columnsTablet: 8
  columnsMobile: 4
  gutterDesktop: "24px"
  gutterMobile: "16px"
  pagePaddingDesktop: "40px"
  pagePaddingTablet: "28px"
  pagePaddingMobile: "18px"
spacing:
  xs: "6px"
  sm: "10px"
  md: "16px"
  lg: "24px"
  xl: "36px"
  xxl: "56px"
  section: "96px"
  sectionMobile: "58px"
rounded:
  sm: "6px"
  md: "12px"
  lg: "22px"
  xl: "34px"
borders:
  subtle: "1px solid {colors.stone}"
  strong: "1px solid {colors.ink}"
  darkPanel: "1px solid rgba(247, 242, 234, 0.18)"
shadows:
  none: "none"
  paperLift: "0 18px 60px rgba(17, 17, 17, 0.07)"
  panelLift: "0 28px 90px rgba(17, 17, 17, 0.12)"
motion:
  allowed:
    - "Subtle opacity transition"
    - "Small translateY under 8px"
    - "Matter router active-state change"
    - "Mobile sticky CTA entrance"
  forbidden:
    - "Sparkles"
    - "Neon glow"
    - "Parallax for its own sake"
    - "AI shimmer"
    - "Bouncy SaaS motion"
  duration:
    fast: "140ms"
    medium: "220ms"
    slow: "360ms"
breakpoints:
  mobile: "0-767px"
  tablet: "768-1023px"
  desktop: "1024px+"
components:
  disclaimerStrip:
    required: true
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ivory}"
    typography: "{typography.label}"
    padding: "10px 16px"
    contentRules:
      - "Must state that the preview is an independent W230 concept."
      - "Must avoid implying affiliation, appointment, or endorsement."
      - "Must be visible before the hero."
  headerBar:
    backgroundColor: "{colors.ivory}"
    borderBottom: "{borders.subtle}"
    layout: "Firm name left, W230 concept-preview label right."
    contentRules:
      - "Use the real public firm name only if sourced."
      - "Never use fake partner names."
      - "Never add badges unless publicly verifiable."
  hero:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.ink}"
    layout: "Editorial two-column on desktop, single-column on mobile."
    requiredElements:
      - "Outcome-led headline"
      - "Short client-facing subheading"
      - "Primary CTA"
      - "Secondary low-pressure action"
      - "One proof summary or intake promise"
    headlineRules:
      - "Must describe the client outcome, not W230's creativity."
      - "Must avoid generic claims such as 'modern legal solutions'."
      - "Must not promise legal outcomes."
  proofRail:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    border: "{borders.subtle}"
    shadow: "{shadows.paperLift}"
    padding: "24px"
    requiredElements:
      - "Proof label"
      - "Fact"
      - "Source name"
      - "Source URL"
      - "Date accessed if available"
    rules:
      - "Use public-source facts only."
      - "Do not infer awards, specialties, rankings, or outcomes from vague copy."
      - "If a fact cannot be sourced, remove it."
      - "Maximum 4 proof items per rail."
  decisionCards:
    backgroundColor: "{colors.paper}"
    rounded: "{rounded.lg}"
    border: "{borders.subtle}"
    padding: "24px"
    maxCards: 4
    cardRule: "Each card maps to a client problem, not an internal practice category."
    examples:
      - "Buying or selling property"
      - "Business contract or dispute"
      - "Family or relationship issue"
      - "Visa or migration pathway"
  matterRouter:
    backgroundColor: "{colors.paper}"
    activeBackgroundColor: "{colors.paleBlue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    border: "{borders.subtle}"
    padding: "24px"
    required: true
    requiredStates:
      - "Default"
      - "Selected matter type"
      - "Guided next step"
      - "Firm handoff summary"
    contentRules:
      - "Must ask plain-language intake questions."
      - "Must not provide legal advice."
      - "Must route to contact, consultation request, document upload, or callback."
      - "Must show what the firm receives internally."
  intakePanel:
    backgroundColor: "{colors.legalNavy}"
    textColor: "{colors.ivory}"
    rounded: "{rounded.xl}"
    border: "{borders.darkPanel}"
    shadow: "{shadows.panelLift}"
    padding: "28px"
    requiredElements:
      - "Client matter summary"
      - "Urgency"
      - "Documents required"
      - "Recommended next action"
      - "Internal partner or admin view"
    rules:
      - "Must be clearly marked as a mock preview."
      - "Must not imply the firm currently has this system."
  mobileStickyCta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ivory}"
    rounded: "{rounded.lg}"
    padding: "12px"
    position: "fixed bottom on mobile only"
    requiredElements:
      - "Primary action"
      - "Call or enquiry shortcut"
    rules:
      - "Only visible after hero."
      - "Must not cover form controls."
      - "Must be dismissible if it obscures content."
  auditWarning:
    backgroundColor: "{colors.danger}"
    textColor: "#FFFFFF"
    rounded: "{rounded.sm}"
    padding: "12px"
    visibility: "W230-facing only"
    contentRules:
      - "Use for internal preview risks."
      - "Do not show public criticism of the target firm."
      - "Do not shame current-site issues."
buttons:
  primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ivory}"
    hoverBackgroundColor: "{colors.goldDark}"
    rounded: "{rounded.sm}"
    padding: "14px 18px"
    fontFamily: "Inter"
    fontWeight: 700
    minHeight: "46px"
  secondary:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.ink}"
    border: "{borders.subtle}"
    hoverBackgroundColor: "{colors.paper}"
    rounded: "{rounded.sm}"
    padding: "14px 18px"
    fontFamily: "Inter"
    fontWeight: 700
    minHeight: "46px"
evidencePolicy:
  allowedSources:
    - "Firm website"
    - "Public regulator records"
    - "Public legal directory profile"
    - "Google Business profile if publicly accessible"
    - "LinkedIn company page"
    - "Published articles or public media"
  disallowedSources:
    - "Invented client reviews"
    - "Unsourced awards"
    - "Assumed practice strengths"
    - "Private emails"
    - "Unverified social comments"
    - "Case outcomes unless publicly and safely sourced"
  requiredForEachClaim:
    - "Exact claim text"
    - "Source name"
    - "Source URL"
    - "Confidence level: verified, inferred, or removed"
  defaultActionWhenUnsure: "Remove the claim."
legalSafety:
  forbidden:
    - "Do not provide legal advice."
    - "Do not promise outcomes."
    - "Do not imply solicitor-client relationship."
    - "Do not create fake testimonials."
    - "Do not claim no-win-no-fee unless public and sourced."
    - "Do not invent response times or availability."
  required:
    - "Use 'concept preview' language."
    - "Use 'general information' language where relevant."
    - "Separate design critique from public-facing copy."
    - "Make all mock workflows visibly conceptual."
qualityGate:
  passCriteria:
    - "The first screen explains the client outcome."
    - "The proof rail contains only sourced facts."
    - "The matter router is visible without deep scrolling."
    - "Mobile CTA is obvious and usable."
    - "There is only one primary action per viewport."
    - "The page feels like editorial infrastructure, not a template."
    - "No claim would embarrass W230 if challenged by the firm."
  failCriteria:
    - "Looks like generic SaaS."
    - "Uses purple gradients or AI gloss."
    - "Mirrors the firm's existing service taxonomy without simplification."
    - "Uses decorative sections with no conversion or trust job."
    - "Includes fake awards, fake reviews, fake lawyer names, or fake outcomes."
    - "Requires desktop to understand the value."
---
# W230 Legal Editorial

## 1. Overview

W230 Legal Editorial is the design contract for premium website rebuild concepts for boutique law firms and professional-service firms.
Its job is not to make a law firm look fashionable. Its job is to make the firm's credibility legible, structured, and actionable.

The system is client-intake-first. A stressed visitor should understand three things within seconds:

1. They are in the right place.
2. Their matter has a clear pathway.
3. There is a low-friction next step.

The preview must show that W230 understands the firm's website problem better than the current site does. The strongest proof is not decoration. The strongest proof is a better intake logic.

## 2. Strategic Positioning

The design should communicate:

| Layer | Meaning |
|---|---|
| Surface | Calm, editorial, premium, restrained |
| UX | Client problem first, firm taxonomy second |
| Commercial | Better website equals better matter routing |
| Proof | Public facts only |
| Product | Matter router plus intake handoff |
| Risk control | No invented legal credibility |

The page should feel like a legal intake conversation, not a brochure.

## 3. Audience

**Primary audience:**
- Managing partners
- Practice owners
- Boutique firm principals
- Operations managers
- Marketing decision-makers inside professional-service firms

**Secondary audience:**
- High-intent clients arriving from mobile search
- Referral clients checking credibility before contacting
- Existing clients looking for contact or matter information

**Design implication:** the preview must impress the firm while making the client journey simpler.

## 4. Visual Direction

Use calm editorial authority.

The system should feel closer to:
- Legal stationery
- Archival folders
- Premium editorial publishing
- Quiet institutional trust
- Boutique advisory practice

It should not feel like:
- Consumer SaaS
- Crypto landing page
- AI tool website
- Cheap agency template
- Luxury perfume campaign
- Over-designed startup homepage

## 5. Colour System

| Token | Hex | Use |
|---|---:|---|
| Ink | #111111 | Headlines, primary copy, CTAs |
| Charcoal | #24211D | Secondary dark text |
| Muted | #6F6A61 | Supporting copy |
| Ivory | #F7F2EA | Main background |
| Paper | #FFFDF8 | Cards and proof surfaces |
| Stone | #D8CEC0 | Borders and dividers |
| Stone Light | #E8DED0 | Low-emphasis surfaces |
| Gold | #B68A35 | Premium accent only |
| Gold Dark | #7A581D | CTA hover state |
| Sage | #879B88 | Calm trust accent |
| Pale Blue | #DDE8EF | Guidance and active states |
| Legal Navy | #172232 | Intake and internal handoff panels |
| Danger | #8F2E21 | Internal audit warnings only |

### Colour rules

Use gold sparingly. If gold appears everywhere, the preview becomes fake luxury.

Use Legal Navy for operational depth: intake summary, partner view, handoff panel, or system preview.

Use Danger only in internal W230 audit materials. Never use it to publicly shame the current firm website.

## 6. Typography

Use serif for authority and sans for clarity.

| Role | Font | Function |
|---|---|---|
| Display | Instrument Serif | Major editorial statement |
| H1 | Instrument Serif | Main page promise |
| H2 | Instrument Serif | Section themes |
| H3 | Inter | Functional headings |
| Body | Inter | Plain explanation |
| Label | Inter uppercase | Proof labels, audit labels, metadata |

### Typography rules

One meaningful H1 per page.

Avoid:
- "Welcome to"
- "Your trusted legal partner"
- "Modern legal solutions"
- Repeated hero slogans
- Over-stacked service headings

The headline must describe the client pathway or perception gap, not generic professionalism.

**Good headline pattern:**
```
A clearer first step for clients facing property, business, family, or migration matters.
```

**Bad headline pattern:**
```
Boutique legal solutions for a changing world.
```

## 7. Layout System

The page should move from trust to action.

**Required sequence:**

| Order | Section | Purpose |
|---|---|---|
| 1 | Disclaimer strip | No-affiliation clarity |
| 2 | Header bar | Firm identity plus W230 preview label |
| 3 | Hero | Outcome-led positioning |
| 4 | Proof rail | Public credibility signals |
| 5 | Decision cards | Collapse practice taxonomy into client problems |
| 6 | Matter router | Interactive intake logic |
| 7 | Mobile-first demo | Show conversion surface |
| 8 | Intake panel | Show what the firm receives |
| 9 | Before vs preview | Explain the perception gap |
| 10 | Contact | Public contact details and next action |

Every section must perform one of four jobs:
1. Build trust.
2. Reduce confusion.
3. Route the matter.
4. Trigger contact.

If a section does none of these, remove it.

## 8. Grid and Spacing

Use a restrained editorial grid.

| Context | Rule |
|---|---|
| Desktop | 12-column grid, max width 1240px |
| Tablet | 8-column grid |
| Mobile | 4-column grid |
| Main content width | 620px to 760px |
| Section spacing desktop | 96px |
| Section spacing mobile | 58px |
| Page padding desktop | 40px |
| Page padding mobile | 18px |

Use whitespace as a credibility signal. Do not fill every section with cards.

## 9. Component Rules

### 9.1 Disclaimer Strip

Mandatory for unsolicited previews.

**Purpose:** protect W230 from implying affiliation.

**Required content:**
```
Independent W230 concept preview. Not affiliated with or endorsed by the firm shown.
```

**Rules:**
- Must appear before the hero.
- Must be visible and plain.
- Must not be hidden in footer copy.

### 9.2 Proof Rail

The proof rail is the credibility spine.

Each proof item must include:

| Field | Required |
|---|---|
| Claim | Yes |
| Source name | Yes |
| Source URL | Yes |
| Confidence | Yes |
| Date accessed | Preferred |

**Allowed claim types:**
- Years in operation if public
- Office locations if public
- Practice areas if public
- Public directory listings
- Published articles
- Public reviews only if directly sourced
- Public accreditation only if directly sourced

**Forbidden claim types:**
- "Award-winning" without source
- "Leading firm" without source
- "Trusted by thousands" without source
- Case results unless public and appropriate
- Fake testimonials
- Assumed specialisation

**Default rule:** if a claim cannot be sourced, remove it.

### 9.3 Decision Cards

Decision cards translate legal taxonomy into client language.

**Maximum:** 4 cards.

**Good labels:**
- Buying or selling property
- Starting or restructuring a business
- Family or relationship issue
- Visa or migration pathway

**Bad labels:**
- Commercial Law
- Conveyancing
- Family Law
- Migration Law

The card can include the formal practice name, but only as secondary text.

### 9.4 Matter Router

The matter router is the sale.

It must show how the new website helps the firm capture better enquiries.

**Required states:**

| State | Purpose |
|---|---|
| Default | Ask the user what they need help with |
| Matter selected | Show relevant pathway |
| Guidance | Clarify urgency and documents |
| Handoff | Show what the firm receives |

The router must not provide legal advice. It should only route, clarify, and prepare the next step.

**Example logic:**
```
What do you need help with?
- Property
- Business
- Family
- Migration

Selected: Property
Next questions:
- Are you buying, selling, leasing, or resolving a dispute?
- Is there a contract deadline?
- Do you already have documents?
- Would you prefer a call or form submission?

Firm receives:
- Matter type
- Urgency
- Client details
- Documents available
- Recommended next action
```

### 9.5 Intake Panel

The intake panel shows the operational value.

It should answer:
- What does the client submit?
- What does the firm receive?
- Who should respond?
- What documents are needed?
- What is the next action?

This is where the preview moves from "nice website" to "better business system."

### 9.6 Mobile Sticky CTA

Mobile is the primary legal conversion surface.

**Rules:**
- Appears only after hero scroll.
- Uses one primary action.
- Includes call or enquiry shortcut.
- Does not cover form fields.
- Must be dismissible if it blocks content.

**Example:**
```
[Start enquiry]  [Call firm]
```

## 10. Mobile-First Rules

The mobile view must not be a compressed desktop layout.

**Priority order on mobile:**
1. Disclaimer
2. Firm name
3. Outcome-led headline
4. Primary CTA
5. Matter router
6. Proof summary
7. Contact

Do not place long partner bios, decorative images, or generic service grids before the matter router on mobile.

**Mobile failure mode:**
> User lands on phone, sees a large decorative hero, scrolls through vague services, and still does not know what to do.

**Mobile success mode:**
> User lands on phone, sees their problem, selects a matter type, and can contact the firm in under 30 seconds.

## 11. Evidence Protocol

Every public proof signal needs a source.

Use this table internally while building each preview:

| Claim | Source | URL | Confidence | Keep? |
|---|---|---|---|---|
| Firm has office in X | Firm website | Full URL | Verified | Yes |
| Firm specialises in Y | Firm website | Full URL | Verified | Yes |
| Firm is award-winning | Unknown | None | Unverified | No |
| Partner is expert in Z | Directory | Full URL | Verified if direct | Maybe |

**Claim labels:**

| Label | Meaning |
|---|---|
| Verified | Directly supported by a public source |
| Inferred | Reasonable but not directly stated |
| Unverified | Not safe to use |
| Removed | Excluded from preview |

Only **Verified** claims should appear in the public-facing design.

## 12. Copywriting Rules

Write like a calm legal intake specialist, not an agency copywriter.

**Good tone:**
```
Start with the matter. We'll guide you to the right next step.
```

**Bad tone:**
```
Transform your legal journey with innovative digital solutions.
```

**Good W230-facing language:**
```
The current site hides the client pathway behind internal practice labels.
```

**Bad public-facing language:**
```
The current website is confusing and outdated.
```

## 13. Before vs Preview Section

This section should be strategic, not insulting.

Use neutral comparisons:

| Current pattern | Preview direction |
|---|---|
| Practice areas listed as internal categories | Client problems grouped by intent |
| Contact details sit low on mobile | Sticky high-intent contact path |
| Proof scattered across pages | Public-source proof rail |
| Enquiry form is generic | Matter-specific intake flow |

Avoid public shame language.

**Do not say:**
```
The current website fails.
```

**Say:**
```
The current experience makes high-intent clients work harder than they need to.
```

## 14. Interaction Model

**Allowed interactions:**
- Matter selection
- Active card state
- Intake summary update
- Mobile CTA reveal
- Source drawer or proof expansion
- Before vs preview toggle

**Forbidden interactions:**
- Decorative animation with no conversion purpose
- Fake chatbot pretending to be the firm
- AI assistant that gives legal advice
- Popups that interrupt reading
- Auto-playing videos with sound

## 15. Accessibility Rules

**Minimum requirements:**

| Area | Rule |
|---|---|
| Text contrast | WCAG AA minimum |
| Buttons | Minimum 44px tap target |
| Labels | Never rely on colour alone |
| Forms | Every input needs a visible label |
| Motion | Avoid essential motion |
| Mobile | CTA must not block content |
| Sources | URLs must be readable or accessible |

## 16. Image Direction

Use imagery only when it increases trust.

**Allowed:**
- Abstract legal stationery
- Office texture
- Paper, folders, documents
- Architectural interior details
- Calm portrait treatment if real and sourced
- Archival or editorial framing

**Avoid:**
- Gavels
- Scales of justice clichés
- Stock handshake imagery
- Fake courthouse drama
- AI-generated lawyer portraits
- Purple gradients
- Futuristic holograms
- Overly glossy luxury props

If no strong image exists, use typography and layout instead.

## 17. Agent Instructions

When generating a preview using this system, the agent must:

1. Identify the firm and confirm public source material.
2. Extract only verified proof signals.
3. Translate practice areas into client problems.
4. Build the hero around the client's first action.
5. Create a matter router before decorative service sections.
6. Show mobile-first conversion.
7. Include a mock intake handoff.
8. Mark all conceptual features as concept preview.
9. Remove any unsourced claim.
10. Run the quality gate before output.

## 18. Quality Gate

A preview passes only if all of the following are true:

| Test | Pass condition |
|---|---|
| First screen | Client understands what action to take |
| Proof | Every credibility claim is sourced |
| Router | Matter router is present and useful |
| Mobile | Primary action is reachable fast |
| Tone | Calm, professional, non-generic |
| Safety | No fake awards, reviews, outcomes, or affiliations |
| Design | Editorial, not SaaS or AI-glossy |
| Commercial | Shows why W230 improves the business system |

## 19. Rejection Tests

Reject the design if it contains:

- Purple AI gradients
- Fake testimonials
- Fake lawyers
- Fake awards
- Fake case results
- Generic "trusted legal partner" copy
- A service grid before client-intent routing
- Desktop-only conversion logic
- Decorative animation without functional purpose
- A chatbot that implies legal advice
- Any claim without source support

## 20. Final Standard

The page should make the firm think:
```
This is not just a redesign.
This is a clearer way for clients to enter the firm.
```

And it should make the client think:
```
I know where to start.
```
