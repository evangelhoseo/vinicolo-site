# Vinícolo — Design System

Vinícolo is a Brazilian wine brand and retailer. Its stated purpose: help people **ampliar o repertório** (broaden their cultural repertoire) and rediscover the pleasure of trying new flavors, bringing them closer to the world of wine — driven by curiosity rather than label-following. The brand pairs quality and fair pricing with real product knowledge, positioning itself as a serious, approachable authority for wine at any budget.

**Values:** Transparência (honest guidance toward the best choice), Credibilidade (trust earned through study and expertise), Acessibilidade (wine as an everyday culture, not just special occasions), Paixão (genuine enthusiasm, rediscovering pleasure in new flavors).

## Source

Everything in this design system was taken directly from Vinícolo's public brand guide: **https://vinicolo.framer.website/** (a Framer site, "Guia da Marca" by Vínculo Design). No other codebase, Figma file, or product screens were provided — this is a print/brand-identity guide, not a UI or app spec. Because of that:

- Colors, logos, character illustrations, and patterns below are copied verbatim from that source.
- No digital product screens exist in the source, so **no UI kit was built**. The Components library (below) is a standard, brand-styled primitive set sized for a wine e-commerce/club use case — see "Intentional additions."
- Spacing, radius, shadow, and the type scale are not defined in the brand guide (which only shows font families and weights) — these were designed to match the brand's rounded, warm visual language and are flagged as such in `tokens/`.

## Intentional additions

The brand guide defines identity (logo, color, type, character, patterns) but no UI components. Per design-system convention, a standard component set was authored from scratch: Button, IconButton, Badge, Tag, Input, Select, Checkbox, Radio, Switch, Card, Dialog, Toast, Tooltip, Tabs. These are original UI work, styled with Vinícolo's tokens — not sourced from the brand guide.

## Fonts — substitution flagged

The brand's official typefaces are **Satoshi** (body/UI) and **Clash Display** (headings, used sparingly for standout phrases). Neither is available as a fetchable webfont from this environment (Fontshare's font API and CDN are not reachable here). They have been substituted with the closest Google Fonts matches:

- Satoshi → **Plus Jakarta Sans**
- Clash Display → **Bricolage Grotesque**

**Please provide the real Satoshi and Clash Display font files (woff2/ttf) so they can replace the substitutes in `tokens/fonts.css` and `assets/fonts/`.**

## Content fundamentals

- **Language:** Portuguese (Brazil). Copy is written in first person plural ("nós"), speaking as the brand — e.g. "A Vinícolo existe para auxiliar as pessoas a ampliar o repertório cultural."
- **Tone:** warm, knowledgeable, unpretentious. It leans into expertise ("estudo", "conhecimento", "paixão") but explicitly rejects wine snobbery — "não se deixar levar somente pelos rótulos" (not judging by label alone), wine "para qualquer bolso, para qualquer pessoa" (for any budget, any person).
- **Emphasis:** key phrases are bolded mid-sentence to carry the message: **ampliar o repertório**, **redescobrir o prazer**, **curiosidade**, **descobrir o novo**, **ama o que faz**.
- **No emoji, no exclamation-heavy copy.** Sentences are measured and a little literary/reflective rather than punchy or salesy.
- **Values copy pattern:** one-line, declarative, verb-first statements (e.g. "Auxiliar cada pessoa na sua melhor escolha, com honestidade").

## Visual foundations

- **Color:** Vinho Cabernet (`#5C0D33`) is the sole primary/priority color — deep wine red, used as the dominant color across materials. Four support colors — Laranja Terroir (`#EB5A43`), Lilás Bouquet (`#C3B9DC`), Azul Riviera (`#B7E0EE`), Bege Champagne (`#FCF3E3`) — exist explicitly for accents and dynamizing communication, **never as a material's priority color** (the brand guide states this directly). Bege Champagne reads as the warm neutral/background color in the guide's own layout.
- **Type:** Satoshi (body) paired with Clash Display (display), the latter reserved for titles or single standout phrases — not full paragraphs. No type scale, spacing, or UI grid is defined in the source; a 1.333 (perfect-fourth) scale and 4px spacing base were chosen here for digital use.
- **Logo system:** four lockups — Assinatura Horizontal, Assinatura Vertical, Símbolo, Logotipo — each with a "positiva" (light-surface) and "negativa" (dark-surface) version. A protection area is defined: a square of side *X*, where *X* is half the symbol's height in the full signature, or the height of the "V" when using the logotype alone.
- **Illustration:** a hand-drawn linework "personagem" (character) — a wine-enthusiast figure used as a secondary graphic device across applications, shown in ~10 poses/moments.
- **Patterns:** two custom repeating patterns, each recolored into the four support colors, for digital/print backgrounds.
- **Imagery (from guide examples):** warm-toned photography of wine, food, and lifestyle scenes; no heavy grain or black-and-white treatment observed.
- **No motion, hover, shadow, or blur system is defined** in the brand guide (it's a static identity guide) — the digital tokens (radius, shadow, hover states) added under `tokens/` are original choices in the brand's spirit, flagged inline in each file.

## Iconography

The brand guide contains no icon system, icon font, or SVG icon set — it only covers logo, color, type, character, and pattern. No icons were invented for this reason. When a UI needs icons, use a neutral, permissively-licensed set (e.g. Lucide) at a light stroke weight to match the brand's soft, hand-drawn linework — this is a suggestion, not a brand-sourced rule.

## Index

- `styles.css` — root stylesheet, imports every token file. Link this one file from any consuming project.
- `tokens/colors.css` — primary + 4 support colors (verbatim), derived neutral scale, semantic aliases.
- `tokens/typography.css` — font stacks, type scale, weights (scale is an original digital addition).
- `tokens/spacing.css` — spacing scale, radius, shadow (all original digital additions).
- `tokens/fonts.css` — `@font-face` rules for the Satoshi/Clash Display substitutes.
- `base.css` — minimal element resets (body, headings, links).
- `assets/logo/` — signature (horizontal/vertical), symbol, and logotype, each in default, `positiva/`, `negativa/`, and `protection-area/` variants.
- `assets/character/` — 10 character illustrations (personagem).
- `assets/patterns/` — 6 pattern fills across support colors.
- `assets/examples/`, `assets/hero.png`, `assets/intro-01.png`, `assets/intro-02.png` — reference imagery from the brand guide page itself.
- `assets/fonts/` — substitute webfont files (Plus Jakarta Sans, Bricolage Grotesque).
- `guidelines/` — foundation specimen cards (colors, type, spacing, brand assets) shown in the Design System tab.
- `components/core/` — Button, IconButton, Badge, Tag.
- `components/forms/` — Input, Select, Checkbox, Radio, Switch.
- `components/surfaces/` — Card, Dialog.
- `components/feedback/` — Toast, Tooltip.
- `components/navigation/` — Tabs.
- `SKILL.md` — portable skill file for use in Claude Code or other agent environments.

## Components

Badge, Button, Card, Checkbox, Dialog, IconButton, Input, Radio, Select, Switch, Tabs, Tag, Toast, Tooltip.
