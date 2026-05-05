# Law Firm Preview Pipeline

Target: Melbourne boutique law firms with existing but weak websites.

## Qualification

- Established firm or principal-led practice
- Clear practice areas and public contact details
- Existing website looks dated, cluttered, generic, or low-conversion
- Decision-maker likely reachable via LinkedIn

## Design system

This vertical uses Google Labs `design.md` as the machine-readable taste contract.

- Source spec: `DESIGN.md`
- Name: `W230 Legal Editorial`
- Tailwind export: `tailwind.theme.json`
- W3C/DTCG token export: `tokens.dtcg.json`

Validation/export commands:

```bash
cd professional/law-firms
npx -y @google/design.md lint DESIGN.md
npx -y @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.dtcg.json
python3 tests_design_system.py
```

Core taste rule: the matter router is the sale. Future previews should be client-intake-first, proof-led, mobile-first, and explicit about no affiliation.

## Build standard

- noindex preview
- public-source facts only
- no fabricated testimonials, awards, win rates, or client outcomes
- mobile-first layout
- clear practice-area routing
- strong credibility hierarchy
- partner/principal section only when sourced
- independent concept-preview disclaimer
- CSS should expose the W230 token aliases from `DESIGN.md`, e.g. `--w230-ink` and `--w230-gold`

## First preview

- `batten-sacks/` — concept preview based on publicly visible homepage information.
