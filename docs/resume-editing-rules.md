# Resume Editing Rules

Tactical wording guidance. When in doubt, open this file before writing.

For reasoning posture, see `AGENTS.md`.
For what the current resume looks like, see `current-resume-positioning.md`.

---

## Voice

Should sound: confident · specific · plain · human · technical · non-hype.

Should not sound like: AI influencer branding · generic consultant résumé · vendor marketing · underclaimed junior contributor · overclaimed architect profile.

---

## Verbs

### Prefer

built · delivered · maintained · improved · defined · introduced · authored · implemented · led · shipped · designed · deployed

### Avoid

revolutionary · cutting-edge · AI transformation · enterprise AI visionary · leveraged · production-grade (when describing local prototypes) · core components (when ownership was deeper than "components")

### Hedging verbs — audit carefully

contributed to · supported · assisted · helped · participated in · served as

Any of these signal possibly-adjacent work. Use only when ownership was genuinely limited; otherwise rewrite to claim the exact part owned.

Examples:

| Weak | Strong |
|---|---|
| Contributed to an evaluation harness… | Built scoring, review, and failure-classification workflows for a Cortex Analyst evaluation harness… |
| Supported reliability… | Maintained and improved reliability for Snowflake and Databricks analytics pipelines… |
| Contributed to measurable outcomes over roughly one year… | Delivered a production inventory optimization system with measured outcomes over roughly one year… |
| Built core components of client-facing evaluation tooling… | Built the benchmark design, deterministic retrieval scoring, Snowflake persistence layer, and TruLens/Snowsight observability integration for a client-facing Cortex Search evaluation framework. |

---

## AI Fog

Technical terms are allowed. Invented labels, noun-stacks, and agent-generated shorthand are fog.

| Fog | Plain technical equivalent |
|---|---|
| multi-surface scoring | separate scoring for data results, SQL logic, and answer quality |
| confidence-gated overrides | override rules that apply only when judge confidence is high |
| four-category attribution taxonomy | four failure categories: benchmark, evaluator, service, and workflow |
| tuning-backlog output model | structured tuning backlog for Semantic View fixes |
| dual-provider LLM bridge | provider layer for switching between Gemini and local Ollama |
| rubric-aware scoring gates | scoring rules tied to rubric thresholds |
| latency-aware reasoning-step UI | UI that shows judging steps during slow local inference |
| raw-payload-to-draft traceability | every AI output can be traced back to its original source post |
| deterministic anchor-consistency story-repair algorithm | rule-based anchor-consistency logic for repairing story groups |
| Agentic Root-Cause Analysis | Agent-assisted failure analysis |
| Pydantic-typed LLM Outputs | Typed LLM outputs with Pydantic |

Test: if a phrase needs another phrase to explain it, simplify.

---

## Vendor Fog

Use exact vendor product names, but give a plain-English translation on first use. Later mentions stay product-named.

| Product | First-use translation |
|---|---|
| Cortex Analyst | Snowflake's text-to-SQL engine over Semantic Views |
| Cortex Search | Snowflake's managed fuzzy/semantic search and retrieval service |
| Snowflake Semantic Views | the metric and relationship layer used by Cortex Analyst |
| Cortex Code Agent SDK | agent/tooling SDK for read-only SQL workflows inside Snowflake |
| TruLens / Snowflake AI Observability | client-side SDK exporting traces and custom metrics to Snowflake Event Tables |

Do not write "Snowflake Cortex" alone when a specific product is meant.

---

## Independent Research And Local Projects

Coding Agent Acceptance Lab is **independent research and open-source engineering**, not a local prototype. Use:

- independent technical report
- open-source research release
- reproducible evaluation system
- public research suite

Do not call it peer-reviewed, academic publication, production SaaS, or a universal benchmark leaderboard.

Use exact denominators when citing the headline result:

- 33 coding scenarios
- 391 retained attempts
- sparse false-green rate: 84 / 194 = 43.3%
- contract-visible false-green rate: 17 / 191 = 8.9%

## Local Projects

Allowed scope language:

- local prototype
- laptop-local workbench
- personal project
- case study

Forbidden scope claims for these projects:

- SaaS
- production deployment
- multi-user persistence
- commercial readiness
- server deployment
- enterprise-grade

Each project uses this layout in the HTML:

```
Project Title
Plain-English "what it is" sentence.
Stack: technical specifics.
Architecture / Tests / Result: additional labeled lines as warranted.
```

Keep titles honest — if the folder name is `cognos-game`, the web title can be `Cognos Studio — Turkish-first thinking-game engine`, but the ATS PDF should expand it to `Turkish LLM Judging Game (Cognos Studio)` for disambiguation.

---

## Section Names

| Web form | ATS PDF form | Why |
|---|---|---|
| Core Competencies | Skills | ATS section taxonomy standard |
| Selected Technical Work | Projects | ATS friendly; local/prototype scope belongs in item text |
| Technical Writing | Technical Writing | truthful label; do not inflate to Publications unless public publication scope changes |
| Professional Experience | Professional Experience | already standard |
| Education | Education | already standard |

When a section name changes in `index.html`, also update `SECTION_RENAMES` in `build/build_ats_pdf.py`.

---

## Format Rules for Both Variants

- Special characters that leak into PDF text: avoid `→` (use `to`), curly quotes (straight quotes), non-breaking spaces, middle dots when they're not meant to be read as separators.
- Emojis belong only in the web header's contact row; the build script strips them and replaces with labels.
- Bullet lists are real `<ul>` / `<li>` — don't fake bullets with `•` glyphs in plain text.
- Dates use `Mon YYYY – Mon YYYY` or `Mon YYYY – Present`.
- Skills use compact grouped text in the web resume and flatten to inline category lines in the ATS PDF; avoid rebuilding a dense chip wall.

---

## Write for Three Readers at Once

On every bullet, silently ask:

1. Does an HR reader understand the category?
2. Does an engineer see evidence of ownership and implementation?
3. Does the ATS extract the right keywords in the right section?

If a line passes only one, rewrite.
