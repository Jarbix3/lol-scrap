"""Convierte un .md de coach a PDF usando weasyprint.

Modos de uso:

1. Single file (PDF se guarda al lado del .md original):

    .venv/bin/python _build_coach_pdf.py reports/Manuchito-LAS/COACH_ANALYSIS.md

2. Batch sobre todos los reports/<player>/COACH_ANALYSIS.md
   (PDFs se guardan en reports/pdf_report/<player>.pdf):

    .venv/bin/python _build_coach_pdf.py --batch
    .venv/bin/python _build_coach_pdf.py --batch --reports-root reports

3. Single file con destino custom:

    .venv/bin/python _build_coach_pdf.py reports/X/COACH_ANALYSIS.md \\
        --output reports/pdf_report/X.pdf
"""
from __future__ import annotations

import argparse
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


def build_pdf(
    md_path: Path,
    out_path: Path | None = None,
    title_override: str | None = None,
) -> Path:
    """Convierte un archivo Markdown a PDF.

    Args:
        md_path: archivo .md a convertir.
        out_path: destino del PDF. Si es None, se guarda al lado del .md
            con extension .pdf (back-compat).
        title_override: titulo a usar como string-set y data-title del HTML.
            Si es None, usa md_path.stem (back-compat).

    Returns:
        Path absoluto del PDF generado.
    """
    md_text = md_path.read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    body_html = md.convert(md_text)

    title = title_override if title_override is not None else md_path.stem
    render_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    html_doc = f"""<!DOCTYPE html>
<html data-title="{title}" data-date="{render_date}">
<head><meta charset="utf-8"><title>{title}</title></head>
<body>
{body_html}
</body>
</html>"""

    if out_path is None:
        out_path = md_path.with_suffix(".pdf")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_doc, base_url=str(md_path.parent)).write_pdf(
        target=str(out_path),
        stylesheets=[CSS(string=CSS_STYLES)],
    )
    return out_path


def batch_render(
    reports_root: Path,
    output_dir: Path,
    md_filename: str = "COACH_ANALYSIS.md",
) -> list[tuple[Path, Path]]:
    """Renderiza todos los reports/<player>/<md_filename> a PDF.

    Cada PDF se guarda en output_dir con el nombre del directorio padre
    (ej. reports/Manuchito-LAS/COACH_ANALYSIS.md ->
         output_dir/Manuchito-LAS.pdf).

    Returns:
        Lista de tuplas (md_path, pdf_path) para cada conversion exitosa.
    """
    if not reports_root.is_dir():
        raise FileNotFoundError(f"reports_root no es directorio: {reports_root}")

    pairs: list[tuple[Path, Path]] = []
    for md_path in sorted(reports_root.glob(f"*/{md_filename}")):
        player_dir = md_path.parent.name
        pdf_path = output_dir / f"{player_dir}.pdf"
        title = f"COACH 360 - {player_dir.replace('_', ' ').replace('-', '#')}"
        build_pdf(md_path, out_path=pdf_path, title_override=title)
        pairs.append((md_path, pdf_path))
    return pairs


def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Convierte COACH_ANALYSIS.md a PDF (single o batch)."
    )
    p.add_argument(
        "md_file",
        nargs="?",
        help="Archivo .md a convertir (modo single). Omitir si usas --batch.",
    )
    p.add_argument(
        "--batch",
        action="store_true",
        help=(
            "Modo batch: itera sobre todos los <reports-root>/*/<filename> "
            "y guarda PDFs en --output-dir."
        ),
    )
    p.add_argument(
        "--reports-root",
        default="reports",
        help="Directorio raiz de reports (default: reports).",
    )
    p.add_argument(
        "--output-dir",
        default="reports/pdf_report",
        help=(
            "Carpeta destino para los PDFs en modo batch "
            "(default: reports/pdf_report)."
        ),
    )
    p.add_argument(
        "--filename",
        default="COACH_ANALYSIS.md",
        help="Nombre del archivo a buscar dentro de cada player dir.",
    )
    p.add_argument(
        "--output",
        help="Destino del PDF en modo single (default: <md>.pdf al lado del .md).",
    )
    return p


def _main(argv: list[str] | None = None) -> int:
    args = _build_arg_parser().parse_args(argv)

    if args.batch:
        reports_root = Path(args.reports_root).resolve()
        output_dir = Path(args.output_dir).resolve()
        try:
            pairs = batch_render(
                reports_root=reports_root,
                output_dir=output_dir,
                md_filename=args.filename,
            )
        except FileNotFoundError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
        if not pairs:
            print(
                f"No se encontro ningun {args.filename} bajo {reports_root}",
                file=sys.stderr,
            )
            return 1
        print(f"Generados {len(pairs)} PDFs en {output_dir}:")
        for md_path, pdf_path in pairs:
            try:
                rel = pdf_path.relative_to(Path.cwd())
            except ValueError:
                rel = pdf_path
            print(f"  - {rel}")
        return 0

    if not args.md_file:
        print(
            "Error: pasa <md_file> o usa --batch. Ver --help.",
            file=sys.stderr,
        )
        return 1

    md_file = Path(args.md_file).resolve()
    if not md_file.exists():
        print(f"No existe: {md_file}", file=sys.stderr)
        return 1

    out_path = Path(args.output).resolve() if args.output else None
    pdf_file = build_pdf(md_file, out_path=out_path)
    print(f"PDF generado: {pdf_file}")
    return 0


if __name__ == "__main__":
    sys.exit(_main())
