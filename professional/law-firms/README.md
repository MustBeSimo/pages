# Law Firm Preview Pipeline

Target: Melbourne boutique law firms with existing but weak websites.

## Qualification

- Established firm or principal-led practice
- Clear practice areas and public contact details
- Existing website looks dated, cluttered, generic, or low-conversion
- Decision-maker likely reachable via LinkedIn

## Style contract

This vertical consumes the general W230 style registry. It does not own the visual system.

- Source style: `../styles/legal-editorial/DESIGN.md`
- Style name: `W230 Legal Editorial`
- Tailwind export: `../styles/legal-editorial/tailwind.theme.json`
- W3C/DTCG token export: `../styles/legal-editorial/tokens.dtcg.json`

Validation/export commands:

```bash
npx -y @google/design.md lint professional/styles/legal-editorial/DESIGN.md
npx -y @google/design.md export --format tailwind professional/styles/legal-editorial/DESIGN.md > professional/styles/legal-editorial/tailwind.theme.json
npx -y @google/design.md export --format dtcg professional/styles/legal-editorial/DESIGN.md > professional/styles/legal-editorial/tokens.dtcg.json
python3 professional/tests_style_registry.py
python3 professional/law-firms/tests_design_system.py
python3 professional/law-firms/tests_law_preview.py
```

Core taste rule: the matter router is the sale. Future previews should be client-intake-first, proof-led, mobile-first, and explicit about no affiliation.

## Legal preview guardrails

- Use `noindex,nofollow` on every preview page.
- Use public-source facts only.
- Include an independent W230 concept-preview disclaimer.
- No fabricated testimonials, awards, win rates, client outcomes, accreditation, guarantees, or lawyer biographies.
- No typo-shaming or public spelling-jab framing.
- Partner/principal sections only when sourced.
- Outreach rules live outside the style file and require user approval before sending.

## Build standard

- mobile-first layout
- clear practice-area routing
- strong credibility hierarchy
- CSS should expose the W230 token aliases from `../styles/legal-editorial/DESIGN.md`, e.g. `--w230-ink` and `--w230-gold`

## First preview

- `batten-sacks/` — concept preview based on publicly visible homepage information.
