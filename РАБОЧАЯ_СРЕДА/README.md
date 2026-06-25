# РАБОЧАЯ СРЕДА — сборка идей, документации, презентаций и текстов заявки

Самодостаточная среда, чтобы **строить реальные артефакты** проекта NBS-IA из
обычного Markdown: технические документы (DOCX/PDF), презентации (PPTX) и тексты
заявки (с проверкой лимитов слов/знаков). Кириллица поддерживается везде.

---

## 0. Что уже установлено (проверка)

```powershell
python tools\common.py        # самодиагностика среды
```

Должно показать `ВСЁ ГОТОВО ✓`. Под капотом:

| Инструмент | Назначение | Где |
|---|---|---|
| **Python 3.12** + библиотеки | движок всех скриптов | `%LOCALAPPDATA%\Programs\Python\Python312` |
| `pymupdf`, `pdfplumber` | чтение PDF (текст + таблицы) | pip |
| `python-docx`, `openpyxl` | чтение/запись Word, Excel | pip |
| `python-pptx` | сборка презентаций | pip |
| `markdown`, `jinja2` | разметка/шаблоны | pip |
| `matplotlib` + гео-стек | чертежи/графики (см. `../материалы/charts/`) | pip |
| **Pandoc 3.9** | Markdown → DOCX/PDF | `%LOCALAPPDATA%\Pandoc` |
| **Tectonic 0.16** | LaTeX-движок для PDF (кириллица) | `%LOCALAPPDATA%\Programs\tectonic` (в PATH) |

> Первый запуск сборки PDF: Tectonic докачивает пакеты LaTeX из интернета —
> это нормально и происходит один раз.

---

## 1. Структура

```
РАБОЧАЯ_СРЕДА/
├─ README.md               ← этот файл
├─ tools/                  инструменты (Python)
│   ├─ common.py           общая конфигурация + самодиагностика + лимиты NBS-IA
│   ├─ extract.py          PDF/DOCX/XLSX → Markdown
│   ├─ build_docx.py       Markdown → .docx
│   ├─ build_pdf.py        Markdown → .pdf (кириллица)
│   ├─ build_pptx.py       спек-Markdown → .pptx (фирменный стиль)
│   ├─ check_limits.py     проверка текстов заявки на лимиты слов/знаков
│   └─ pandoc/defaults.yaml настройки PDF (шрифт, поля, цвета)
├─ source_extracted/       РЕАЛЬНЫЕ шаблоны конкурса и PDF, извлечённые в .md
│   ├─ Application_Form.md          ← все поля формы + лимиты слов
│   ├─ LogFrame_Template.md         ← структура логфрейма
│   ├─ Budget_template.md           ← статьи бюджета
│   ├─ NBS-IA_Call_for_Proposals_Central_Asia.md  ← главные правила
│   └─ … (Explainer, SubgrantAgreement, тех-выжимки, JRC)
├─ ideas/                  проработанные идеи (рабочие .md)
├─ docs/                   техническая документация
├─ slides/                 исходники презентаций (спек-Markdown)
│   └─ _пример_слайдов.md  образец формата слайдов
├─ application/            ТЕКСТЫ ЗАЯВКИ
│   ├─ narratives/         нарративы 3.1–3.8, A_mandate, B_summary (стабы готовы)
│   ├─ logframe/           логфрейм проекта
│   └─ budget/             бюджет
└─ out/                    собранные DOCX/PDF/PPTX (генерируется)
```

> **Запускать скрипты из папки `РАБОЧАЯ_СРЕДА/`** (пути в примерах относительные).

---

## 2. Инструменты — как пользоваться

Везде `python` = `%LOCALAPPDATA%\Programs\Python\Python312\python.exe` (он первый в PATH).

### 2.1 Извлечь исходник в Markdown — `extract.py`
```powershell
python tools\extract.py "..\материалы\шаблоны_конкурса\Application_Form.docx"
python tools\extract.py "..\материалы\техника\04_Технические_выжимки_и_схемы.pdf"
python tools\extract.py --all          # все шаблоны конкурса разом → source_extracted\
```

### 2.2 Markdown → Word — `build_docx.py`
```powershell
python tools\build_docx.py docs\концепт.md
python tools\build_docx.py application\narratives\3.2_описание.md -o out\3.2.docx
python tools\build_docx.py docs\концепт.md --reference style.docx   # фирменный стиль
```

### 2.3 Markdown → PDF (кириллица) — `build_pdf.py`
```powershell
python tools\build_pdf.py ideas\идея.md
python tools\build_pdf.py docs\концепт.md --toc          # с оглавлением
```
Шрифт/поля/цвета — в `tools\pandoc\defaults.yaml` (по умолчанию Times New Roman,
поля 2.2 см, teal-ссылки).

### 2.4 Презентация — `build_pptx.py`
Формат спека (слайды разделяются строкой `---`):
```markdown
# Заголовок титульного слайда
## подзаголовок / авторы

---
# Заголовок слайда
- тезис
- тезис
    - под-тезис (отступ ≥ 2 пробела)

---
# Слайд с картинкой
![](../../материалы/charts/site_plan_maly_taldykol.png)
- подпись справа от картинки
```
```powershell
python tools\build_pptx.py slides\_пример_слайдов.md
```
Палитра teal `#0E7C7B` + red `#D7263D`, 16:9. Картинки — по пути **относительно файла спека**.

### 2.5 Проверка лимитов заявки — `check_limits.py`
Файлы в `application\narratives\` должны начинаться с кода секции
(`3.1_…`, `B_summary…`). Скрипт считает слова/знаки без markdown-разметки и
сравнивает с лимитом NBS-IA.
```powershell
python tools\check_limits.py                       # вся папка narratives
python tools\check_limits.py application\narratives\3.2_описание.md
```

| Секция | Лимит |
|---|---|
| A. Мандат заявителя | 100 слов |
| B. Резюме | 2000 знаков |
| 3.1 Климат-контекст | 700 слов |
| 3.2 Описание | 1500 слов |
| 3.3 Схема реализации | 1000 слов |
| 3.4 Нац. политики (NDC/NAP/SDG) | 500 слов |
| 3.5 Инновация · 3.6 Масштаб · 3.7 Финплан · 3.8 MRV | по 500 слов |

---

## 3. Рабочий процесс заявки (рекомендация)

1. **Опора на реальную форму** — `source_extracted/Application_Form.md` (поля,
   guiding questions, лимиты) и `…Call_for_Proposals…md` (правила).
2. Пишем нарративы в `application/narratives/` (по-английски — язык подачи).
3. `check_limits.py` — держим лимиты.
4. Логфрейм по `source_extracted/LogFrame_Template.md` → `application/logframe/`;
   бюджет по `Budget_template.md` → `application/budget/` (Excel заполняем в
   `../материалы/шаблоны_конкурса/Budget_template.xlsx`).
5. Чертежи/карты — `../материалы/charts/` (matplotlib, воспроизводимо).
6. Сборка приложений: `build_docx.py` / `build_pdf.py`; колода — `build_pptx.py`.
7. Финал подаётся онлайн в Tally (текст из нарративов) + DOCX/XLSX-приложения.

---

## 4. Памятка (cheat sheet)

```powershell
python tools\common.py                       # «всё работает?»
python tools\extract.py --all                # обновить source_extracted\
python tools\check_limits.py                 # лимиты заявки
python tools\build_pdf.py  docs\X.md         # → out\X.pdf
python tools\build_docx.py docs\X.md         # → out\X.docx
python tools\build_pptx.py slides\X.md       # → out\X.pptx
```

> Что финансирует грант, eligibility, потолки бюджета, дедлайн (30.06.2026) —
> в `../ПРАВИЛА_конкурса.md` и `source_extracted/NBS-IA_Call_for_Proposals_Central_Asia.md`.
