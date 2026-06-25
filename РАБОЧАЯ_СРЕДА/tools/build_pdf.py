"""
build_pdf.py — Markdown → .pdf (Pandoc + Tectonic/XeTeX, поддержка кириллицы).

Шрифт по умолчанию — Times New Roman (есть на Windows, содержит кириллицу).
Настройки берутся из tools/pandoc/defaults.yaml.

Примеры:
    python tools/build_pdf.py docs/концепт.md
    python tools/build_pdf.py ideas/идея.md -o out/идея.pdf
    python tools/build_pdf.py docs/концепт.md --toc
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

import common


def build(src: Path, dst: Path | None, toc: bool = False) -> Path:
    if not common.PANDOC:
        raise SystemExit("Pandoc не найден.")
    if not common.TECTONIC:
        raise SystemExit("Tectonic не найден (нужен как PDF-движок).")
    if dst is None:
        dst = common.OUT / (src.stem + ".pdf")
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [common.PANDOC, str(src), "-o", str(dst),
           "--from", "gfm+tex_math_dollars",
           "--defaults", str(common.PANDOC_DEFAULTS),
           f"--pdf-engine={common.TECTONIC}"]
    if toc:
        cmd += ["--toc", "--toc-depth=2"]
    print("· сборка PDF (первый запуск Tectonic докачивает пакеты LaTeX — это нормально)")
    subprocess.run(cmd, check=True)
    print(f"✓ PDF → {dst}")
    return dst


def main():
    ap = argparse.ArgumentParser(description="Markdown → PDF (кириллица)")
    ap.add_argument("source", help="входной .md")
    ap.add_argument("-o", "--out", help="выходной .pdf (по умолчанию out/<имя>.pdf)")
    ap.add_argument("--toc", action="store_true", help="добавить оглавление")
    args = ap.parse_args()
    build(Path(args.source).resolve(),
          Path(args.out).resolve() if args.out else None, toc=args.toc)


if __name__ == "__main__":
    sys.exit(main())
