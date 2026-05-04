# resume

Rich HTML resume (`index.html`) plus an ATS-safe PDF build script.

## Layout

```
resume/
├── index.html              # source of truth — hand-edited
├── build/
│   └── build_ats_pdf.py    # HTML → ATS-safe PDF transformer
├── dist/                   # generated outputs (gitignored)
│   ├── Anil_Yamangil_Resume.pdf
│   └── index.ats.html      # only with --keep-html
├── archive/                # old versions kept for reference
├── requirements.txt
└── README.md
```

- **Source of truth:** `index.html` — rich portfolio version, styled for screen, shareable as a link.
- **Application PDF:** `dist/Anil_Yamangil_Resume.pdf` — regenerated from `index.html` by the build script. Do not hand-edit; regenerate.

## One-time setup

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
# macOS also needs pango/cairo from Homebrew (WeasyPrint uses them for text shaping):
brew install pango cairo
```

## Build the ATS PDF

Whenever `index.html` changes:

```bash
.venv/bin/python build/build_ats_pdf.py
# or with an inspection-friendly intermediate file:
.venv/bin/python build/build_ats_pdf.py --keep-html
```

Outputs:
- `dist/Anil_Yamangil_Resume.pdf` — the PDF to upload to applications
- `dist/index.ats.html` (only with `--keep-html`) — the transformed HTML used to render the PDF, handy for debugging

## What the script changes (from `index.html` → PDF)

All content is preserved — no bullets dropped, no sections cut. The transformations are formatting-only, targeting ATS reliability:

1. **Contact emojis → labels** (`📧` becomes `Email:`, etc.) and the row is flattened to a single plain line.
2. **Skill pill chips → comma-separated inline text** under bold category labels. Pills parse inconsistently across ATS; inline text is reliable.
3. **Multi-column grids → single column** everywhere.
4. **Special characters → ASCII** (`→` to `to`, smart quotes to straight quotes, em/en dashes to hyphens).
5. **Section headers renamed** to ATS-standard labels: `Core Competencies` → `Skills`, `Independent Fun & Technical Projects — Local Prototypes` → `Projects`.
6. **Cognos project title expanded** to include the descriptive name so ATS keyword matches land on both.
7. **Tailwind link dropped**, portfolio `<style>` block replaced with a minimal single-column ATS stylesheet.

## Why we don't trim content for ATS

ATS parsers index text; they don't count pages. Keyword density helps match scores. The portfolio HTML and the ATS PDF carry the same substance — only formatting differs. Length is whatever it needs to be.
