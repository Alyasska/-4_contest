# -*- coding: utf-8 -*-
"""
Гидрограф срезки пика паводка водно-болотным накопителем (Малый Талдыколь, R-02).
Модель: линейный резервуар  dS/dt = Q_in - Q_out,  S = K * Q_out.
Иллюстративно (форма притока — синтетический гидрограф). Точные значения — Design-фаза.

Запуск:
  python hydrograph_peak_shaving.py
Выход: PDF (вектор) + SVG + PNG в этой же папке.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# ---------- стиль ----------
plt.rcParams.update({
    "font.family": "DejaVu Sans",   # поддерживает кириллицу
    "font.size": 11,
    "axes.edgecolor": "#374151",
    "axes.linewidth": 1.0,
    "axes.grid": True,
    "grid.color": "#e5e7eb",
    "grid.linewidth": 0.8,
    "figure.dpi": 150,
})
TEAL, RED, FILL = "#0f766e", "#dc2626", "#86efac"

# ---------- входные параметры (иллюстративные) ----------
tp   = 8.0      # время до пика притока, ч
n    = 4.0      # форма (SCS-подобный безразмерный гидрограф)
Qpk  = 25.0     # пик притока, м3/с
K    = 6.0      # константа накопителя (время добегания), ч  -> регулирует срезку
dt   = 0.05     # шаг, ч
t    = np.arange(0, 60 + dt, dt)

# приток: Q = Qpk * (t/tp)^n * exp(n (1 - t/tp))
with np.errstate(divide="ignore", invalid="ignore"):
    Qin = Qpk * (t / tp) ** n * np.exp(n * (1 - t / tp))
Qin = np.nan_to_num(Qin)

# маршрутизация через линейный резервуар (Эйлер): dQout/dt = (Qin - Qout)/K
Qout = np.zeros_like(t)
for i in range(1, len(t)):
    Qout[i] = Qout[i-1] + dt / K * (Qin[i-1] - Qout[i-1])

# ---------- метрики ----------
peak_in, peak_out = Qin.max(), Qout.max()
t_peak_in, t_peak_out = t[Qin.argmax()], t[Qout.argmax()]
reduction = (peak_in - peak_out) / peak_in * 100.0
lag = t_peak_out - t_peak_in
# задержанный объём = интеграл(Qin - Qout) при Qin>Qout, ч*м3/с -> м3 (x3600)
stored_volume = np.trapezoid(np.clip(Qin - Qout, 0, None), t) * 3600.0

# ---------- график ----------
fig, ax = plt.subplots(figsize=(9.2, 5.2))
ax.fill_between(t, Qin, Qout, where=(Qin > Qout), color=FILL, alpha=0.55,
                label="Задержанный объём (хранение в озере)", zorder=1)
ax.plot(t, Qin,  color=RED,  lw=2.6, label="Приток (без накопителя)", zorder=3)
ax.plot(t, Qout, color=TEAL, lw=2.6, label="Сброс (с накопителем)",   zorder=3)

# линии пиков
ax.axhline(peak_in,  color=RED,  ls="--", lw=1.0, alpha=0.7)
ax.axhline(peak_out, color=TEAL, ls="--", lw=1.0, alpha=0.7)
ax.annotate("", xy=(2.2, peak_in), xytext=(2.2, peak_out),
            arrowprops=dict(arrowstyle="<->", color="#0f4c45", lw=1.8))
ax.text(2.8, (peak_in + peak_out) / 2,
        f"срезка пика\n−{reduction:.0f}%", color="#0f4c45",
        fontsize=12, fontweight="bold", va="center")

# подписи пиков
ax.scatter([t_peak_in, t_peak_out], [peak_in, peak_out], color=[RED, TEAL], zorder=4, s=28)
ax.annotate(f"{peak_in:.1f} м³/с", (t_peak_in, peak_in), textcoords="offset points",
            xytext=(6, 6), color=RED, fontsize=10, fontweight="bold")
ax.annotate(f"{peak_out:.1f} м³/с  (+{lag:.1f} ч)", (t_peak_out, peak_out),
            textcoords="offset points", xytext=(8, 6), color=TEAL, fontsize=10, fontweight="bold")

ax.set_xlim(0, 48)
ax.set_ylim(0, peak_in * 1.18)
ax.xaxis.set_major_locator(MultipleLocator(6))
ax.set_xlabel("Время, ч")
ax.set_ylabel("Расход, м³/с")
ax.set_title("Срезка пика паводка водно-болотным накопителем (Малый Талдыколь, R-02)",
             fontsize=12.5, fontweight="bold", color="#0f4c45", pad=12)
ax.legend(loc="upper right", framealpha=0.95, edgecolor="#e5e7eb")

# плашка с параметрами
txt = (f"Модель: линейный резервуар (S = K·Q), K = {K:g} ч\n"
       f"Задержанный объём ≈ {stored_volume/1000:,.0f} тыс. м³  ·  лаг пика +{lag:.1f} ч\n"
       f"Иллюстративно: форма притока синтетическая, параметры — к уточнению (Design-фаза)")
ax.text(0.013, -0.205, txt, transform=ax.transAxes, fontsize=8.4, color="#6b7280",
        va="top", ha="left")

fig.tight_layout(rect=[0, 0.02, 1, 1])
for ext in ("pdf", "svg", "png"):
    fig.savefig(f"hydrograph_peak_shaving.{ext}", bbox_inches="tight")
print(f"OK | пик {peak_in:.1f}->{peak_out:.1f} м3/с | срезка {reduction:.1f}% | объём {stored_volume:,.0f} м3 | лаг {lag:.1f} ч")
