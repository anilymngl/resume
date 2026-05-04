#!/usr/bin/env python3
"""
Build an ATS-safe PDF from the rich HTML resume.

Run from the project root:
    source .venv/bin/activate
    python build/build_ats_pdf.py

Or from anywhere:
    .venv/bin/python build/build_ats_pdf.py

Transformations applied to produce a text-extractable, ATS-friendly PDF:
  1. Contact-row emojis (📧 📞 📍 🔗) → plain labels ("Email:", "Phone:",
     "Location:", "LinkedIn:") and the row is flattened to a single line.
  2. Skill pill chips → comma-separated inline text under bold category
     labels. Pills parse inconsistently across ATS; inline text is reliable.
  3. 2-column skills grid → single column.
  4. Special characters (→, smart quotes) → plain ASCII equivalents.
  5. Section headers renamed to ATS-standard labels:
        "Core Competencies" → "Skills"
        "Independent Fun & Technical Projects — Local Prototypes" → "Projects"
  6. Cognos project title expanded to include the descriptive name:
        "Cognos Studio — Turkish-first thinking-game engine"
        → "Turkish LLM Judging Game (Cognos Studio) — Turkish-first thinking-game engine"
  7. Tailwind CDN link dropped and the portfolio <style> block replaced
     with a minimal single-column ATS stylesheet.

Content is NOT reduced. All experience, projects, bullets, and skills
survive. Length is whatever it needs to be; ATS indexes text, not pages.

The original index.html is never modified. Outputs:
  - dist/Anil_Yamangil_Resume.pdf   (upload this to applications)
  - dist/index.ats.html             (inspection copy, only if --keep-html)
"""

from __future__ import annotations

import argparse
import os
import platform
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# macOS / Apple Silicon: make sure weasyprint can find Homebrew's Pango.
# WeasyPrint uses dlopen() which doesn't search /opt/homebrew/lib by default.
# Setting DYLD_FALLBACK_LIBRARY_PATH before the weasyprint import fixes this.
# ---------------------------------------------------------------------------
if platform.system() == "Darwin":
    for brew_lib in ("/opt/homebrew/lib", "/usr/local/lib"):
        if os.path.isdir(brew_lib):
            existing = os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
            if brew_lib not in existing:
                os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = (
                    f"{brew_lib}:{existing}" if existing else brew_lib
                )

from bs4 import BeautifulSoup, NavigableString


# ---------------------------------------------------------------------------
# ATS-safe stylesheet. Self-contained: no Tailwind needed.
# ---------------------------------------------------------------------------
ATS_CSS = """
@page { size: Letter; margin: 0.6in 0.7in; }

body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.4;
  color: #000;
  margin: 0;
}

h1 {
  font-size: 18pt;
  margin: 0 0 0.1rem 0;
  text-align: left;
  letter-spacing: 0.02em;
}

.subtitle {
  font-size: 10.5pt;
  font-weight: normal;
  margin: 0 0 0.45rem 0;
  color: #000;
}

.contact-line {
  font-size: 10pt;
  margin: 0 0 0.7rem 0;
  text-align: left;
}

h2 {
  font-size: 11pt;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-bottom: 1px solid #000;
  padding-bottom: 0.1rem;
  margin: 0.8rem 0 0.4rem 0;
  page-break-after: avoid;
}

h3 {
  font-size: 11pt;
  margin: 0.45rem 0 0.1rem 0;
  font-weight: bold;
}

h4 {
  font-size: 10.5pt;
  margin: 0.25rem 0 0.1rem 0;
  font-weight: bold;
}

h4 span { font-weight: normal; color: #333; }

h5 {
  font-size: 10.5pt;
  margin: 0.35rem 0 0.15rem 0;
  font-weight: bold;
}

p { margin: 0.15rem 0; }

ul {
  margin: 0.15rem 0 0.35rem 0;
  padding-left: 1rem;
  page-break-inside: avoid;
}

li {
  margin-bottom: 0.22rem;
  line-height: 1.4;
}

.role-blurb {
  font-size: 10pt;
  color: #333;
  margin: 0.15rem 0 0.35rem 0;
}

.skill-category {
  margin: 0.15rem 0;
  font-size: 10.5pt;
}

.skill-category strong { font-weight: bold; }

.project-title { font-weight: bold; font-size: 10.5pt; margin: 0.35rem 0 0.1rem 0; }
.project-desc { margin: 0 0 0.1rem 0; }
.project-meta { margin: 0.05rem 0; font-size: 10pt; }
.project-meta strong { font-weight: bold; }

/* kill portfolio-only visuals that may leak in */
.shadow-md, .shadow-sm, .rounded-lg, .rounded-full { box-shadow: none; border-radius: 0; }
.bg-slate-50, .bg-slate-100, .bg-white { background: white; }
a { color: #000; text-decoration: none; }
"""


EMOJI_LABELS = {
    "📧": "Email:",
    "📞": "Phone:",
    "📍": "Location:",
    "🔗": "LinkedIn:",
}

# ASCII swaps for characters that some ATS parsers mangle.
CHAR_SWAPS = [
    ("→", "to"),
    ("\u2014", "-"),        # em dash
    ("\u2013", "-"),        # en dash
    ("\u2018", "'"),        # left single quote
    ("\u2019", "'"),        # right single quote / apostrophe
    ("\u201c", '"'),        # left double quote
    ("\u201d", '"'),        # right double quote
    ("\u00a0", " "),        # non-breaking space
    ("\u00b7", "-"),        # middle dot (used as separator in workstream titles)
]

SECTION_RENAMES = {
    "Core Competencies": "Skills",
    "Independent Fun & Technical Projects — Local Prototypes": "Projects",
    "Independent Fun & Technical Projects - Local Prototypes": "Projects",
}


# ---------------------------------------------------------------------------
# Transformations
# ---------------------------------------------------------------------------
def drop_tailwind(soup: BeautifulSoup) -> None:
    for link in soup.find_all("link", href=re.compile(r"tailwindcss")):
        link.decompose()


def replace_style_block(soup: BeautifulSoup) -> None:
    for style in soup.find_all("style"):
        style.decompose()
    head = soup.find("head")
    if head is None:
        return
    new_style = soup.new_tag("style")
    new_style.string = ATS_CSS
    head.append(new_style)


def rebuild_contact_line(soup: BeautifulSoup) -> None:
    """Find the contact row and flatten to a single plain line."""
    for div in soup.find_all("div"):
        links = div.find_all("a", recursive=False)
        if not any("mailto:" in (a.get("href") or "") for a in links):
            continue
        parts = []
        for child in div.find_all(["a", "div"], recursive=False):
            text = child.get_text(" ", strip=True)
            if not text:
                continue
            for emoji, label in EMOJI_LABELS.items():
                text = text.replace(emoji, label + " ")
            text = re.sub(r"\s+", " ", text).strip()
            parts.append(text)
        new_p = soup.new_tag("p")
        new_p["class"] = "contact-line"
        new_p.string = " | ".join(parts)
        div.replace_with(new_p)
        return


def mark_subtitle(soup: BeautifulSoup) -> None:
    """Tag the headline paragraph as .subtitle so the simple stylesheet can style it."""
    for p in soup.find_all("p"):
        classes = p.get("class") or []
        if "text-lg" in classes:
            p["class"] = ["subtitle"]
            return


def strip_emojis_remaining(soup: BeautifulSoup) -> None:
    """Safety net: drop any emoji still left after the contact-line rebuild."""
    for text in list(soup.find_all(string=True)):
        if not isinstance(text, NavigableString):
            continue
        new_text = str(text)
        for emoji, label in EMOJI_LABELS.items():
            new_text = new_text.replace(emoji, label + " ")
        if new_text != text:
            text.replace_with(new_text)


def flatten_skills(soup: BeautifulSoup) -> None:
    grid = soup.find(class_="skills-grid")
    if grid is None:
        return
    lines = []
    for category in grid.find_all("div", recursive=False):
        h3 = category.find("h3")
        if h3 is None:
            continue
        label = h3.get_text(" ", strip=True)
        chips = [s.get_text(" ", strip=True) for s in category.find_all("span")]
        chips = [c for c in chips if c]
        if not chips:
            continue
        p = soup.new_tag("p")
        p["class"] = ["skill-category"]
        strong = soup.new_tag("strong")
        strong.string = f"{label}:"
        p.append(strong)
        p.append(f" {', '.join(chips)}")
        lines.append(p)
    if not lines:
        return
    container = soup.new_tag("div")
    for p in lines:
        container.append(p)
    grid.replace_with(container)


def rename_sections(soup: BeautifulSoup) -> None:
    for h in soup.find_all(["h2", "h3", "h4", "h5"]):
        text = h.get_text(" ", strip=True)
        if text in SECTION_RENAMES:
            h.clear()
            h.append(SECTION_RENAMES[text])


def rewrite_cognos_title(soup: BeautifulSoup) -> None:
    for el in soup.find_all(class_="project-title"):
        text = el.get_text(" ", strip=True)
        if "Cognos Studio" in text and "Turkish LLM Judging Game" not in text:
            tail = text.split("Cognos Studio", 1)[1]
            el.clear()
            el.append(f"Turkish LLM Judging Game (Cognos Studio){tail}")


def swap_special_chars(soup: BeautifulSoup) -> None:
    for text in list(soup.find_all(string=True)):
        if not isinstance(text, NavigableString):
            continue
        # Don't rewrite content inside <style> or <script>
        if text.parent.name in ("style", "script"):
            continue
        new_text = str(text)
        for a, b in CHAR_SWAPS:
            new_text = new_text.replace(a, b)
        if new_text != text:
            text.replace_with(new_text)


def transform(html_path: Path) -> str:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    # Content transforms first (while structure is still rich)
    rebuild_contact_line(soup)
    strip_emojis_remaining(soup)
    mark_subtitle(soup)
    flatten_skills(soup)
    rewrite_cognos_title(soup)
    rename_sections(soup)
    swap_special_chars(soup)
    # Then strip portfolio styling and swap in the ATS stylesheet
    drop_tailwind(soup)
    replace_style_block(soup)
    return str(soup)


def render_pdf(html_str: str, base_url: Path, output_path: Path) -> None:
    from weasyprint import HTML
    HTML(string=html_str, base_url=str(base_url)).write_pdf(str(output_path))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = PROJECT_ROOT / "index.html"
DEFAULT_OUTPUT = PROJECT_ROOT / "dist" / "Anil_Yamangil_Resume.pdf"
DEFAULT_ATS_HTML = PROJECT_ROOT / "dist" / "index.ats.html"


def main() -> int:
    ap = argparse.ArgumentParser(description="Build an ATS-safe PDF from the rich HTML resume.")
    ap.add_argument("--input", default=str(DEFAULT_INPUT),
                    help=f"source HTML (default: {DEFAULT_INPUT.relative_to(PROJECT_ROOT)})")
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT),
                    help=f"PDF output path (default: {DEFAULT_OUTPUT.relative_to(PROJECT_ROOT)})")
    ap.add_argument("--keep-html", action="store_true",
                    help=f"also save transformed HTML to {DEFAULT_ATS_HTML.relative_to(PROJECT_ROOT)}")
    args = ap.parse_args()

    src = Path(args.input).resolve()
    if not src.exists():
        print(f"Input not found: {src}", file=sys.stderr)
        return 1

    transformed = transform(src)

    out = Path(args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.keep_html:
        ats_html = DEFAULT_ATS_HTML
        ats_html.parent.mkdir(parents=True, exist_ok=True)
        ats_html.write_text(transformed, encoding="utf-8")
        print(f"Wrote transformed HTML: {ats_html.relative_to(PROJECT_ROOT)}")

    render_pdf(transformed, base_url=src.parent, output_path=out)
    try:
        rel = out.relative_to(PROJECT_ROOT)
    except ValueError:
        rel = out
    print(f"Wrote PDF: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
