# AGENTS.md — Resume Judgment Layer

This repo maintains Anıl Yamangil's public resume and generated ATS/PDF variants.

- For mechanics, build commands, and file layout: `README.md`
- For current positioning decisions: `docs/current-resume-positioning.md`
- For tactical wording rules: `docs/resume-editing-rules.md`
- For pre-publish quality gates: `docs/red-team-checklist.md`

**Precedence when instructions conflict:** prefer `AGENTS.md` for reasoning posture, `README.md` for mechanics, and `docs/current-resume-positioning.md` for current resume facts.

## Core Principle

This resume must preserve a difficult balance:

> truthful but not timid
> technical but not opaque
> senior but not inflated
> market-readable but not generic
> human but not casual
> AI-aware but not AI-hype

Do not optimize for one reader at the expense of the others.

## Reader Model

Every meaningful edit must work for three readers:

1. **Recruiter / HR skim reader**
   They need role clarity, recognizable categories, and plain-English meaning.

2. **Senior engineer / hiring manager**
   They need evidence, ownership, implementation detail, and interview-defensible claims.

3. **ATS / parser**
   It needs standard keywords, clean structure, and parseable text.

Good resume language survives all three.

## Durable Positioning

Anıl is not only a Snowflake engineer, not only an AI evaluation engineer, and not only a data/analytics consultant.

The durable identity is:

> Senior AI/ML Engineer with a deep data engineering, enterprise analytics, and retail optimization foundation, now building applied AI systems and review/evaluation workflows on governed data platforms.

Snowflake/Cortex is a current evidence pillar, not the whole identity.

Invent Analytics is a serious formative chapter, not old filler.

Independent projects are local, fun technical prototypes. They show curiosity and range, but must not be framed as production SaaS.

## Editing Philosophy

Prefer surgical edits.

Do not rewrite for style alone if the current wording is truthful and defensible.

Do not make the resume more impressive by making it less true.

Do not make the resume safer by making real ownership sound junior.

The best wording is usually:

> plain-English category + exact technical implementation

Example:

- bad: `multi-surface semantic-diagnosis infrastructure`
- better: `separate scoring for data results, SQL logic, and answer quality`

## What To Protect

- factual dates, employers, titles, metrics, and scope
- current broad headline direction
- BlueCloud as one employer with sub-roles
- workstream hierarchy in the AI/ML role
- Invent as a major client-delivery / optimization chapter
- local/prototype framing for independent projects
- plain-English translations for vendor tools
- web vs ATS distinction

## What To Avoid

- AI influencer language
- vendor marketing language
- vague "transformation" language
- overclaiming architecture or production maturity
- unexplained vendor/product names
- passive verbs when ownership was real
- turning fun local projects into fake enterprise products
- bloating `AGENTS.md` with details that belong in the docs

## Git & Deployment Strategy

This repository relies on GitHub Pages "Classic Pages Config" to host the live resume directly from the `main` branch. 

**Rule: `main` is production.**
Every merge to `main` instantly triggers a deployment to `https://anilymngl.github.io/resume/`.

**Workflow:**
1. **Never edit `main` directly.** Always create a "story branch" detailing the intent of the changes (e.g., `feature/q2-2026-positioning-update` or `fix/remove-jargon`).
2. **Make granular, meaningful commits.** Do not just write "updated resume." Commit by logical change (e.g., `refactor(html): implement skills grid` or `content: dejargon BlueCloud bullets`).
3. **Merge via Pull Request.** Open a PR on GitHub to visualize the diff and perform the final `red-team-checklist.md` validation before publishing.

## Before Editing

Ask:

1. Is this a content, layout, build, or positioning change?
2. Which reader does it help?
3. Does it weaken another reader's understanding?
4. Is the claim interview-defensible?
5. Does a deeper doc already cover this?

## After Editing

Report:

- what changed
- why it changed
- whether content changed
- whether layout changed
- assumptions or facts needing confirmation

Never claim "assumptions remaining: none" unless scope, dates, ownership, and metrics were explicitly confirmed.
