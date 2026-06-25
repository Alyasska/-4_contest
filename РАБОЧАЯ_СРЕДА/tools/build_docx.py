"""
build_docx.py — Markdown → .docx (через Pandoc).

Подходит для документации, приложений к заявке, текстов нарративов в Word.
Можно передать reference.docx для фирменного стиля.

Примеры:
    python tools/build_docx.py docs/концепт.md
    python tools/build_docx.py application/narratives/3.2_описание.md -o out/3.2.docx
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

import common


def build(src: Path, dst: Path | None, reference: Path | None) -> Path:
    if not common.PANDOC:
        raise SystemExit("Pandoc не найден. Установите Pandoc.")
    if dst is None:
        dst = common.OUT / (src.stem + ".docx")
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [common.PANDOC, str(src), "-o", str(dst),
           "--from", "gfm+tex_math_dollars", "--standalone"]
    if reference and reference.exists():
        cmd += ["--reference-doc", str(reference)]
    print("·", " ".join(Path(c).name if "\\" in c or "/" in c else c for c in cmd))
    subprocess.run(cmd, check=True)
    print(f"✓ DOCX → {dst}")
    return dst


def main():
    ap = argparse.ArgumentParser(description="Markdown → DOCX")
    ap.add_argument("source", help="входной .md")
    ap.add_argument("-o", "--out", help="выходной .docx (по умолчанию out/<имя>.docx)")
    ap.add_argument("--reference", help="reference.docx для стиля")
    args = ap.parse_args()
    build(Path(args.source).resolve(),
          Path(args.out).resolve() if args.out else None,
          Path(args.reference).resolve() if args.reference else None)


if __name__ == "__main__":
    sys.exit(main())
