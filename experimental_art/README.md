# experimental_art — distilled journey art

Throwaway design experiments. **None of these are the source of truth.** None are consumed by `build/build_ats_pdf.py`. They all mirror the content truth in `docs/current-resume-positioning.md` but distill it radically and present it as visual metaphor rather than full resume.

## The six variants

| file                 | metaphor            | vibe                                                        |
| -------------------- | ------------------- | ----------------------------------------------------------- |
| `subway.html`        | transit map          | three colored lines (Retail · Data · AI) with interchanges  |
| `ridgeline.html`     | landscape silhouette | peaks = shipped outcomes, valleys = transitions             |
| `constellation.html` | star map             | stars = roles/projects, lines = shared substrate            |
| `broadsheet.html`    | one-page zine        | pure typographic art, pull quote, curved journey arrow      |
| `datasheet.html`     | IC component datasheet | ultra-precise, anti-verbose, tables and pin diagram only  |
| `field-notes.html`   | first-person letter  | warm palette, serif, credits collaborators, quiet practice notes |

## How to preview

Open any file directly in a browser. No build step, no external JS, no runtime dependency beyond Google Fonts. Everything is inline HTML/CSS/SVG.

## Picking a winner

1. Open each in the target browser (Safari + Chrome).
2. Run a three-reader pass (HR, engineer, ATS — ATS is advisory only here; these are not built into the PDF).
3. Resize to 1440 / 1024 / 768 / 420 px. Confirm SVGs and typography hold.
4. Compare against `docs/red-team-checklist.md` content gates.
5. Decide: promote one to `index.html` (follow AGENTS.md story-branch + PR workflow), keep favorites as a portfolio gallery, or archive/delete the rest.

## Rules these files obey

- Three-reader model from `AGENTS.md`.
- Voice rules from `docs/resume-editing-rules.md` (no AI fog, vendor names translated on first use).
- Positioning invariants from `docs/current-resume-positioning.md` (BlueCloud = one employer, two sub-roles; Invent as serious formative chapter; local projects stay prototypes).
- Header comment in each file states "experimental, not source of truth, not consumed by build script."
