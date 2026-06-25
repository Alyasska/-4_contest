"""
common.py — общая конфигурация рабочей среды NBS-IA.

Содержит автоопределение путей к инструментам (Python, Pandoc, Tectonic),
шрифты для кириллицы в PDF и каталоги проекта. Импортируется остальными
скриптами. Можно запустить напрямую для самодиагностики:

    python tools/common.py
"""
from __future__ import annotations
import os
import shutil
import sys
from pathlib import Path

# Принудительно UTF-8 для вывода (Windows-консоль по умолчанию cp1251/cp866
# не умеет кириллицу и символы ✓/✗). Действует на все скрипты, т.к. они
# импортируют common.
for _stream in ("stdout", "stderr"):
    try:
        getattr(sys, _stream).reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

# ── Каталоги ──────────────────────────────────────────────────────────────
TOOLS_DIR = Path(__file__).resolve().parent
ENV_ROOT = TOOLS_DIR.parent                      # РАБОЧАЯ_СРЕДА/
PROJECT_ROOT = ENV_ROOT.parent                   # конкурс/
MATERIALS = PROJECT_ROOT / "материалы"
TEMPLATES = MATERIALS / "шаблоны_конкурса"

IDEAS = ENV_ROOT / "ideas"
DOCS = ENV_ROOT / "docs"
SLIDES = ENV_ROOT / "slides"
APPLICATION = ENV_ROOT / "application"
NARRATIVES = APPLICATION / "narratives"
SOURCE_EXTRACTED = ENV_ROOT / "source_extracted"
OUT = ENV_ROOT / "out"

# ── Шрифт для кириллицы в PDF (через Tectonic/XeTeX) ───────────────────────
# Times New Roman есть на любой Windows и содержит кириллицу.
PDF_MAINFONT = "Times New Roman"
PDF_SANSFONT = "Arial"
PDF_MONOFONT = "Consolas"


def _find_exe(*candidates: str) -> str | None:
    """Ищет исполняемый файл по PATH и по известным путям установки."""
    for c in candidates:
        found = shutil.which(c)
        if found:
            return found
    # известные локации
    local = Path(os.environ.get("LOCALAPPDATA", ""))
    known = {
        "tectonic": [local / "Programs" / "tectonic" / "tectonic.exe"],
        "pandoc": [local / "Pandoc" / "pandoc.exe"],
    }
    for c in candidates:
        for p in known.get(c, []):
            if p.exists():
                return str(p)
    return None


PANDOC = _find_exe("pandoc")
TECTONIC = _find_exe("tectonic")
PYTHON = sys.executable

PANDOC_DEFAULTS = TOOLS_DIR / "pandoc" / "defaults.yaml"

# ── Лимиты заявки NBS-IA (Application Form) ────────────────────────────────
# unit: "words" или "chars"; limit — максимум.
NBS_LIMITS = {
    "A_mandate":      {"unit": "words", "limit": 100,  "title": "A. Мандат заявителя"},
    "B_summary":      {"unit": "chars", "limit": 2000, "title": "B. Резюме проекта"},
    "3.1":            {"unit": "words", "limit": 700,  "title": "3.1 Климат-контекст"},
    "3.2":            {"unit": "words", "limit": 1500, "title": "3.2 Описание проекта"},
    "3.3":            {"unit": "words", "limit": 1000, "title": "3.3 Схема реализации"},
    "3.4":            {"unit": "words", "limit": 500,  "title": "3.4 Соответствие нац. политикам (NDC/NAP/SDG)"},
    "3.5":            {"unit": "words", "limit": 500,  "title": "3.5 Инновация"},
    "3.6":            {"unit": "words", "limit": 500,  "title": "3.6 Масштаб/тиражирование"},
    "3.7":            {"unit": "words", "limit": 500,  "title": "3.7 Финансовый план"},
    "3.8":            {"unit": "words", "limit": 500,  "title": "3.8 MRV"},
}


def diagnose() -> int:
    ok = True
    print("РАБОЧАЯ СРЕДА NBS-IA — самодиагностика\n" + "=" * 44)
    print(f"Project root : {PROJECT_ROOT}")
    print(f"Env root     : {ENV_ROOT}")
    print(f"Python       : {PYTHON}  ({sys.version.split()[0]})")
    for name, path in (("Pandoc", PANDOC), ("Tectonic", TECTONIC)):
        mark = "OK " if path else "MISSING"
        if not path:
            ok = False
        print(f"{name:<13}: [{mark}] {path or '— не найден —'}")
    print("\nПитон-библиотеки:")
    for mod in ("fitz", "pdfplumber", "docx", "pptx", "openpyxl", "markdown",
                "jinja2", "matplotlib"):
        try:
            __import__(mod)
            print(f"  [OK ] {mod}")
        except Exception as e:  # noqa: BLE001
            ok = False
            print(f"  [!! ] {mod}: {e}")
    print("\nКаталоги:")
    for d in (IDEAS, DOCS, SLIDES, APPLICATION, SOURCE_EXTRACTED, OUT, TEMPLATES):
        print(f"  {'OK ' if d.exists() else '—  '} {d.relative_to(PROJECT_ROOT) if PROJECT_ROOT in d.parents or d == PROJECT_ROOT else d}")
    print("\n" + ("ВСЁ ГОТОВО ✓" if ok else "ЕСТЬ ПРОБЛЕМЫ — см. выше ✗"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(diagnose())
