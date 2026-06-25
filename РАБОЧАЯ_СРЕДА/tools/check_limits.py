"""
check_limits.py — проверка текстов заявки на лимиты слов/знаков NBS-IA.

Сканирует application/narratives/ и сопоставляет файлы с секциями по имени:
файл должен начинаться с кода секции, напр.:
    3.1_климат.md        → лимит 700 слов
    3.2_описание.md      → 1500 слов
    B_summary.md         → 2000 знаков
    A_mandate.md         → 100 слов
(коды: A_mandate, B_summary, 3.1, 3.2, 3.3, 3.5, 3.6, 3.7, 3.8)

Markdown-разметка (#, *, -, ссылки) исключается из подсчёта.

Примеры:
    python tools/check_limits.py
    python tools/check_limits.py application/narratives/3.2_описание.md
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

import common


def strip_markdown(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)  # html-комментарии-инструкции
    text = re.sub(r"`{1,3}[^`]*`{1,3}", " ", text)          # код
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)        # картинки
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)     # ссылки → текст
    text = re.sub(r"[#>*_~|-]", " ", text)                   # разметка
    text = re.sub(r"^\s*\d+\.\s", " ", text, flags=re.MULTILINE)  # нумерация
    return re.sub(r"\s+", " ", text).strip()


def count(text: str, unit: str) -> int:
    clean = strip_markdown(text)
    if unit == "chars":
        return len(clean)
    return len(clean.split()) if clean else 0


def match_section(name: str) -> str | None:
    stem = name.lower()
    # пробуем коды от длинных к коротким, чтобы 3.1 не путать с 3
    for code in sorted(common.NBS_LIMITS, key=len, reverse=True):
        c = code.lower()
        if stem.startswith(c) or stem.startswith(c.replace(".", "_")) or stem.startswith(c.replace(".", "")):
            return code
    return None


def report(files: list[Path]) -> int:
    rows = []
    worst = 0
    for f in files:
        code = match_section(f.name)
        if not code:
            rows.append((f.name, "—", "?", "не распознан код секции"))
            continue
        spec = common.NBS_LIMITS[code]
        n = count(f.read_text(encoding="utf-8"), spec["unit"])
        limit = spec["limit"]
        pct = round(100 * n / limit)
        status = "OK" if n <= limit else "ПРЕВЫШЕНИЕ"
        if n > limit:
            worst = max(worst, 1)
        rows.append((f.name, f"{n}/{limit} {spec['unit']}", f"{pct}%", f"{spec['title']} — {status}"))

    w0 = max((len(r[0]) for r in rows), default=4)
    w1 = max((len(r[1]) for r in rows), default=6)
    print("Проверка лимитов NBS-IA")
    print("=" * (w0 + w1 + 40))
    print(f"{'файл':<{w0}}  {'объём':<{w1}}  доля  секция/статус")
    print("-" * (w0 + w1 + 40))
    for name, vol, pct, note in rows:
        flag = "⚠ " if "ПРЕВЫШ" in note else "  "
        print(f"{flag}{name:<{w0}}  {vol:<{w1}}  {pct:>4}  {note}")
    if not rows:
        print("(нет файлов нарративов — положите их в application/narratives/)")
    return worst


def main():
    ap = argparse.ArgumentParser(description="Проверка лимитов текстов заявки")
    ap.add_argument("files", nargs="*", help="конкретные .md (по умолчанию вся папка narratives)")
    args = ap.parse_args()
    if args.files:
        files = [Path(f).resolve() for f in args.files]
    else:
        files = sorted(common.NARRATIVES.glob("*.md"))
    sys.exit(report(files))


if __name__ == "__main__":
    main()
