"""Convierte un .md de coach a PDF usando weasyprint.

Uso:
    .venv/bin/python _build_coach_pdf.py reports/<archivo>_coach.md
"""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import markdown
from weasyprint import HTML, CSS

CSS_STYLES = """
@page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @top-left {
        content: string(doc-title);
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-size: 9pt;
        color: #555;
    }
    @top-right {
        content: 'Render: ' string(render-date);
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-size: 9pt;
        color: #555;
    }
    @bottom-center {
        content: counter(page) ' / ' counter(pages);
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-size: 9pt;
        color: #555;
    }
}

html {
    string-set: doc-title attr(data-title), render-date attr(data-date);
}

body {
    font-family: 'Helvetica', 'Arial', sans-serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #1a1a1a;
}

h1 {
    string-set: doc-title content();
    font-size: 20pt;
    color: #0f4c81;
    border-bottom: 2px solid #0f4c81;
    padding-bottom: 4pt;
    margin-top: 0;
}

h2 {
    font-size: 14pt;
    color: #0f4c81;
    margin-top: 18pt;
    margin-bottom: 6pt;
    border-bottom: 1px solid #ccc;
    padding-bottom: 2pt;
    page-break-after: avoid;
}

h3 {
    font-size: 12pt;
    color: #1f6db7;
    margin-top: 12pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
}

p, li {
    margin: 4pt 0;
}

ul, ol {
    margin: 4pt 0;
    padding-left: 22pt;
}

li {
    margin: 2pt 0;
}

strong {
    color: #0d3a64;
}

em {
    color: #444;
}

code {
    font-family: 'Menlo', 'Consolas', monospace;
    background: #f3f3f3;
    padding: 1pt 3pt;
    border-radius: 3pt;
    font-size: 9.5pt;
}

blockquote {
    border-left: 3px solid #0f4c81;
    padding: 4pt 10pt;
    margin: 8pt 0;
    background: #f5f8fc;
    color: #333;
    font-style: italic;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 12pt 0;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 8pt 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #ccc;
    padding: 4pt 6pt;
    text-align: left;
    vertical-align: top;
}

th {
    background: #0f4c81;
    color: white;
    font-weight: bold;
}

tbody tr:nth-child(odd) {
    background: #f7faff;
}

tbody tr:nth-child(even) {
    background: white;
}

td:first-child {
    font-weight: 600;
}

/* Truncado con ellipsis para celdas demasiado grandes - desactivado */

/* Header del documento */
.doc-meta {
    color: #555;
    font-size: 9.5pt;
    margin-bottom: 12pt;
}
"""


def build_pdf(md_path: Path) -> Path:
    md_text = md_path.read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    body_html = md.convert(md_text)

    title = md_path.stem
    render_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    html_doc = f"""<!DOCTYPE html>
<html data-title="{title}" data-date="{render_date}">
<head><meta charset="utf-8"><title>{title}</title></head>
<body>
{body_html}
</body>
</html>"""

    out_path = md_path.with_suffix(".pdf")
    HTML(string=html_doc, base_url=str(md_path.parent)).write_pdf(
        target=str(out_path),
        stylesheets=[CSS(string=CSS_STYLES)],
    )
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python _build_coach_pdf.py <archivo.md>", file=sys.stderr)
        sys.exit(1)
    md_file = Path(sys.argv[1]).resolve()
    if not md_file.exists():
        print(f"No existe: {md_file}", file=sys.stderr)
        sys.exit(1)
    pdf_file = build_pdf(md_file)
    print(f"PDF generado: {pdf_file}")
