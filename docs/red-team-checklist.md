# Red-Team Checklist

Run before publishing any change to `index.html` or regenerating the ATS PDF.

For reasoning posture, see `AGENTS.md`.
For what's been decided, see `current-resume-positioning.md`.
For wording rules, see `resume-editing-rules.md`.

---

## Three-Reader Pass

### HR / Recruiter

- [ ] Headline is recognizable and scannable in under five seconds.
- [ ] Every vendor product name has a plain-English translation on first use.
- [ ] Section names are standard or intentionally mapped for ATS (`Professional Experience`, `Education`, `Skills`, `Projects`).
- [ ] No dense jargon or noun-stacks in the first 20% of the page.
- [ ] Local projects are clearly scoped as prototypes / workbenches / case studies, while Coding Agent Acceptance Lab is scoped as independent research.

### Senior Engineer / Hiring Manager

- [ ] Every claim is interview-defensible.
- [ ] Ownership verbs are strong but accurate — no "contributed to / supported / served as" hiding real work.
- [ ] Each workstream or project names the specific surfaces, stacks, or metrics involved.
- [ ] No invented labels ("multi-surface", "agentic root-cause", "dual-provider LLM bridge") without plain technical context.
- [ ] Skill groups are backed by at least one bullet, project, or research entry.

### ATS / Parser

- [ ] Section headers match standard labels (verify in generated PDF, not HTML).
- [ ] No emojis in PDF text output.
- [ ] No `→` arrows, smart quotes, or non-breaking spaces leaking through.
- [ ] Contact info flattens to a single plain line in the PDF.
- [ ] Skills flatten to inline text under bold category labels.
- [ ] Key terms present and extractable: `Cortex Analyst`, `Cortex Search`, `Snowflake Semantic Views`, `PySpark`, `Databricks`, `hidden acceptance testing`, tested metrics.

---

## Content Gates

- [ ] Dates, titles, employers, and client references unchanged (unless explicitly confirmed in the session).
- [ ] Metrics unchanged (unless explicitly confirmed).
- [ ] No claim that makes real ownership sound adjacent.
- [ ] No claim that makes partial ownership sound total.
- [ ] Snowflake/Cortex is framed as a current evidence pillar, not the whole identity.
- [ ] Coding Agent Acceptance Lab is prominent but not framed as peer-reviewed academic publication or a universal benchmark.
- [ ] Invent Analytics retains multiple-clients + inventory-optimization + measured-outcomes framing.
- [ ] Independent projects retain local/prototype framing — no SaaS or production claims.

---

## Build Gates

- [ ] `index.html` opens cleanly in a browser with no layout breakage.
- [ ] `build/build_ats_pdf.py` runs without errors.
- [ ] Generated `dist/Anil_Yamangil_Resume.pdf` opens and renders correctly.
- [ ] If a section name, skill chip, or special character was changed, the corresponding constant in `build_ats_pdf.py` was also updated.

---

## Session Reporting Gate

- [ ] Did not claim "assumptions remaining: none" unless scope, dates, ownership, and metrics were all explicitly confirmed.
- [ ] Reported content changes vs layout changes separately.
- [ ] Flagged any surgical edits that may have unintended reader-model side-effects.

---

## When a Check Fails

1. Fix it before publishing.
2. If the fix touches positioning or tone, update `current-resume-positioning.md` or `resume-editing-rules.md` accordingly so the next session doesn't reopen the same question.
3. If the fix is build-mechanical, update `README.md` or the script, not this checklist.
