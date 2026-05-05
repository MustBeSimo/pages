# W230 style registry

Reusable `DESIGN.md` style contracts live here. A style is visual/taste infrastructure, not a vertical, lead, or outreach rulebook.

## Available styles

| Style | Path | Use when |
|---|---|---|
| W230 Legal Editorial | `legal-editorial/DESIGN.md` | Premium editorial authority for boutique professional-services previews: law, advisory, property, consulting. |

## Rules

- Put visual tokens, typography, spacing, shape, and reusable components in the style `DESIGN.md`.
- Put vertical compliance and outreach rules in that vertical's README, template, and tests.
- Export every style to `tailwind.theme.json` and `tokens.dtcg.json`.
- Future styles should be siblings, for example `trade-premium/`, `archive-editorial/`, or `saas-minimal/`.

## Commands

```bash
npx -y @google/design.md lint professional/styles/legal-editorial/DESIGN.md
npx -y @google/design.md export --format tailwind professional/styles/legal-editorial/DESIGN.md > professional/styles/legal-editorial/tailwind.theme.json
npx -y @google/design.md export --format dtcg professional/styles/legal-editorial/DESIGN.md > professional/styles/legal-editorial/tokens.dtcg.json
```
