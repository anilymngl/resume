# Current Resume Positioning

> **Living state, not permanent truth.** This file captures the current resume positioning as of May 2026. Update it whenever Anıl changes role, target market, project maturity, headline, or public-safe claim boundaries. Treat past decisions recorded here as defaults, not as eternal rules.

The living decision state for the resume in its current form. Update this file when identity, headline, or section shape changes.

For the reasoning posture behind these decisions, see `AGENTS.md`.
For tactical wording rules, see `resume-editing-rules.md`.

---

## Core Identity

> Senior AI/ML Engineer with a deep data engineering, enterprise analytics, and retail optimization foundation, now building applied AI systems, evaluation/review workflows, and decision-support tooling.

Career arc:

1. **Invent Analytics** — retail optimization, forecasting, replenishment, production decision logic, client delivery, squad leadership.
2. **BlueCloud / JLL Technologies** — Snowflake, Databricks, ETL/ELT, governed metrics, Tableau, reliability, schema standards, data quality patterns.
3. **BlueCloud AI/ML** — Cortex Analyst, Cortex Search, Snowflake Semantic Views, retrieval evaluation, text-to-SQL evaluation, Streamlit review tooling, client-facing research, and documentation.
4. **Independent research** — Coding Agent Acceptance Lab, a public open-source research release on coding-agent acceptance reliability.
5. **Selected local projects** — prototypes exploring RAG, LLM judging, local/cloud model workflows, traceability, and structured outputs.

---

## Current Headline

> Senior AI/ML Engineer | Applied AI, Data Engineering & Enterprise Analytics

Why this headline:

- broader than Snowflake-only framings
- clearer than "Decision Systems" (tested; too abstract for HR skim)
- less narrow than "RAG" or "evaluation"
- honors the data engineering and enterprise analytics foundation

Do not narrow the profile to any single label: Snowflake engineer, Cortex specialist, AI evaluation engineer, RAG engineer, dashboard developer, retail optimization consultant. Each is true in part; none is the whole identity.

---

## Current Resume Shape

The current version is a disciplined edit of V3, not a full identity redesign or manifesto.

Order:

1. Header
2. Three-sentence professional summary
3. Professional Experience
   - current BlueCloud AI/ML role
   - Independent Research & Open-Source Engineering as a sibling block immediately after the current role
   - BlueCloud / JLL Technologies
   - Invent Analytics
   - earlier work
4. Selected Technical Work
5. Core Competencies
6. Education

Rationale:

- preserve V3's personality and career continuity
- avoid turning the resume into a grand unifying theory
- elevate Coding Agent Acceptance Lab without letting it swallow the professional record
- keep independent research visibly separate from BlueCloud employer work
- keep the headline stable until the body works

## Professional Experience — Structure

### BlueCloud (one employer, two sub-roles)

- **Senior AI/ML Engineer I** — Jan 2026 – Present
- **Senior Analytics Consultant & Engineer** — Client: JLL Technologies, Aug 2022 – Dec 2025

Header and resume body use the market-normalized `Senior AI/ML Engineer` without the official level suffix. Restore `Senior AI/ML Engineer I` only if title precision is more important than skim readability for a given version.

### AI/ML workstreams

The current role is grouped by problem area, not internal project inventory:

1. **AI Evaluation Systems**
2. **Semantic Systems & Governed Context**
3. **Technical Investigation & Client Enablement**

This preserves Cortex Analyst, Cortex Search, Semantic Views, Streamlit review tooling, benchmark design, and client-facing research while reducing the "internal project inventory" feeling.

### Coding Agent Acceptance Lab — independent research

Positioned directly after the current AI/ML role as its own `Independent Research & Open-Source Engineering` block, not nested under BlueCloud. This avoids implying that the research was a BlueCloud assignment.

Claim boundary:

- independent technical report and open-source research release
- not peer-reviewed academic publication
- not a public benchmark leaderboard
- evidence is specific to the harness, scenarios, prompt lanes, models, and runtime conditions

Keep visible:

- reproducible coding-agent evaluation harness
- visible CI vs hidden acceptance distinction
- false-green / trust-gap framing
- 33 scenarios and 391 retained attempts
- sparse false-green rate 84 / 194 = 43.3%
- contract-visible false-green rate 17 / 191 = 8.9%
- public research site, technical report, evidence matrix, and GitHub repository links

Do not add a standalone Technical Writing section for this single report. Restore that section only when there is a second strong, public-safe writing item.

### Invent Analytics — protected content

Must remain a serious formative chapter. Not generic analytics consulting.

Keep visible:

- multiple retail clients
- inventory optimization
- forecasting and replenishment
- custom production decision logic
- Python/SQL ETL, ML, and simulation pipelines
- UAT / rollout / production support
- squads of 2–4 people
- measured electronics retailer outcome (~3% lost-sales reduction, 7%+ availability improvement, ~10% inventory-turnover improvement)

### Skills section — current shape

Compact text groups, not chip walls:

1. AI Evaluation
2. Data & Semantic Systems
3. Decision Systems
4. Engineering & Delivery

---

## Selected Technical Work

Section title: **Selected Technical Work.**

Projects and naming:

- **RAG Glassbox / Local RAG Case Study** — combines the productized workbench and its antecedent case study.
- **Turkish LLM Judging Game (Cognos Studio)** — for the ATS PDF. Disambiguates from IBM Cognos.
- **Signal Ledger — source-traceable editorial pipeline prototype** — keep only when space allows; explicitly local/prototype.

Each project uses this layout:

```
Project Title
Plain-English "what it is" sentence.
Stack: technical specifics.
Architecture / Tests / Result: additional labeled lines as warranted.
```

---

## Web vs ATS/PDF

Two formats, one source of truth.

- **Web `index.html`** carries rich structure: role hierarchy, research/project links, compact skill groups, visual layout, personality.
- **ATS PDF** flattens to parser-safe formatting: plain contact line, inline comma-separated skills, ASCII-safe characters, standard section names (`Skills`, `Projects`).

Content is maintained once in `index.html`; the PDF is regenerated by `build/build_ats_pdf.py`, never hand-edited. Transformation list lives in `README.md`.

---

## Current Risks to Watch

- **Jan 2026 – Present AI/ML role** is still recent; avoid overclaiming volume or tenure. Workstream framing earns the seniority signal without padding.
- **JLL has no quantified metrics** (intentionally parked). Resume body must stay credible on verbs and scope alone until metrics are added.
- **Coding Agent Acceptance Lab** is serious independent research, but must not be framed as peer-reviewed academic publication or universal model benchmark.
- **Cognos name collision** with IBM Cognos. Web version keeps "Cognos Studio — Turkish-first thinking-game engine"; ATS PDF expands to "Turkish LLM Judging Game (Cognos Studio)".
- **Signal Ledger scope.** Keep local/prototype framing; do not let it compete with the Coding Agent Acceptance Lab research signal.
