# -*- coding: utf-8 -*-
"""
Геопривязанный план площадки: Малый Талдыколь как ливневый накопитель + парк.
Контур озера и дороги — из OpenStreetMap (osmnx); подложка — спутник (contextily);
вмешательства (приток, forebay, болотные края, парковое кольцо, выпуск) вычисляются
от реальной геометрии озера. Север + масштабная линейка. Иллюстративно-концептуально.

Выход: PDF/SVG/PNG в этой же папке.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import osmnx as ox
import contextily as cx

ox.settings.use_cache = True
ox.settings.log_console = False
plt.rcParams.update({"font.family": "DejaVu Sans"})

CENTER = (51.10922, 71.3948)   # Барыс Арена (lat, lon)
DIST   = 2600                  # радиус запроса OSM, м
TEAL, GREEN, RED, BLUE, PURP, GOLD = "#0f766e", "#16a34a", "#dc2626", "#2563eb", "#7c3aed", "#d97706"

def to3857(lat, lon):
    return gpd.GeoSeries([Point(lon, lat)], crs=4326).to_crs(3857).iloc[0]

# ---------- 1. Озеро из OSM ----------
lake = None
try:
    w = ox.features_from_point(CENTER, tags={"natural": "water"}, dist=DIST).to_crs(3857)
    w = w[w.geom_type.isin(["Polygon", "MultiPolygon"])].copy()
    bx = to3857(*CENTER).x
    # «озеро» = крупнейший водоём западнее Барыс Арены
    w["area"] = w.geometry.area
    west = w[w.geometry.centroid.x < bx]
    cand = (west if len(west) else w).sort_values("area", ascending=False)
    geom = cand.iloc[0].geometry
    lake = max(geom.geoms, key=lambda g: g.area) if geom.geom_type == "MultiPolygon" else geom
    all_water = w
    print(f"OSM: водоёмов {len(w)}, площадь озера {lake.area*np.cos(np.radians(CENTER[0]))**2/1e4:,.1f} га (прибл.)")
except Exception as e:
    print("OSM water failed:", e)

if lake is None:   # запасной приблизительный контур
    approx = Polygon([(71.3855,51.1155),(71.3905,51.1135),(71.3920,51.1090),
                      (71.3905,51.1045),(71.3860,51.1035),(71.3835,51.1080),(71.3840,51.1125)])
    lake = gpd.GeoSeries([approx], crs=4326).to_crs(3857).iloc[0]
    all_water = gpd.GeoDataFrame(geometry=[lake], crs=3857)
    print("Использован запасной контур озера (OSM недоступен)")

C = lake.centroid
minx, miny, maxx, maxy = lake.bounds
coslat = np.cos(np.radians(CENTER[0]))

# ---------- 2. Дороги из OSM ----------
roads = None
try:
    roads = ox.features_from_point(CENTER, tags={"highway": ["primary","secondary","tertiary","trunk"]},
                                   dist=DIST).to_crs(3857)
    roads = roads[roads.geom_type.isin(["LineString","MultiLineString"])]
except Exception as e:
    print("OSM roads failed:", e)

# ---------- 3. Геометрия вмешательств от контура озера ----------
def shore_point(direction_deg):
    """точка берега в заданном направлении от центра озера"""
    a = np.radians(direction_deg)
    d = np.array([np.cos(a), np.sin(a)])
    far = Point(C.x + d[0]*4000, C.y + d[1]*4000)
    ray = LineString([C, far])
    inter = ray.intersection(lake.boundary)
    if inter.is_empty:
        return Point(C.x + d[0]*300, C.y + d[1]*300), d
    pts = list(inter.geoms) if inter.geom_type.startswith("Multi") else [inter]
    pts = [p for p in pts if p.geom_type == "Point"]
    p = max(pts, key=lambda p: p.distance(C)) if pts else Point(C.x+d[0]*300, C.y+d[1]*300)
    return p, d

inflow_dirs = [60, 5, -75]          # СВ (жильё), В (Барыс/школа), Ю (WEST SIDE)
forebays, arrows = [], []
for ang in inflow_dirs:
    sp, d = shore_point(ang)
    start = (sp.x + d[0]*230, sp.y + d[1]*230)
    arrows.append((start, (sp.x, sp.y)))
    forebays.append(sp)

outlet, od = shore_point(-110)       # выпуск на юг
park_ring = lake.buffer(110).boundary
# болотные края: восточная часть берега
ext = lake.exterior if lake.geom_type == "Polygon" else max(lake.geoms, key=lambda g:g.area).exterior
fr = np.array(ext.coords)
east_mask = fr[:,0] > C.x
fringe = fr[east_mask]

# ---------- 4. Рисуем ----------
fig, ax = plt.subplots(figsize=(11, 9))
pad = max(maxx-minx, maxy-miny) * 0.42 + 150
ax.set_xlim(minx - pad, maxx + pad)
ax.set_ylim(miny - pad*0.9, maxy + pad*0.9)
ax.set_aspect("equal")

# дороги
if roads is not None and len(roads):
    roads.plot(ax=ax, color="white", linewidth=2.4, alpha=0.55, zorder=2)

# озеро
gpd.GeoSeries([lake], crs=3857).plot(ax=ax, facecolor="#38bdf8", edgecolor="#0369a1",
                                     linewidth=2, alpha=0.45, zorder=3)
# болотные края
if len(fringe) > 2:
    ax.plot(fringe[:,0], fringe[:,1], color=GREEN, lw=6, alpha=0.85, solid_capstyle="round", zorder=4)
# парковое кольцо
gpd.GeoSeries([park_ring], crs=3857).plot(ax=ax, color=GREEN, linewidth=2.2,
                                          linestyle=(0,(7,5)), zorder=4)
# притоки + forebay
for (s, e) in arrows:
    ax.annotate("", xy=e, xytext=s, zorder=6,
                arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=3.2, mutation_scale=22))
for fb in forebays:
    ax.add_patch(Rectangle((fb.x-26, fb.y-26), 52, 52, facecolor=GOLD, edgecolor="#7c2d12",
                           lw=1.2, zorder=7))
# выпуск
ax.annotate("", xy=(outlet.x+od[0]*210, outlet.y+od[1]*210), xytext=(outlet.x, outlet.y),
            zorder=6, arrowprops=dict(arrowstyle="-|>", color="#0369a1", lw=3.2, mutation_scale=22))

# маркеры объектов
def marker(lat, lon, label, color, dy=40):
    p = to3857(lat, lon)
    ax.scatter([p.x],[p.y], s=90, color=color, edgecolor="white", lw=1.5, zorder=8)
    ax.annotate(label, (p.x, p.y), xytext=(0, dy), textcoords="offset points",
                ha="center", fontsize=10, fontweight="bold", color="white", zorder=9,
                bbox=dict(boxstyle="round,pad=0.25", fc=color, ec="none", alpha=0.9))
marker(51.10922, 71.3948, "Барыс Арена", GOLD)
marker(51.1048, 71.4010, "Астана Арена", GOLD)
# Зерде — между озером и Барыс Ареной
zx = (to3857(51.10922,71.3948).x + (maxx)) / 2
ax.scatter([zx],[C.y+120], s=90, color=PURP, edgecolor="white", lw=1.5, zorder=8)
ax.annotate("Зерде школа №9", (zx, C.y+120), xytext=(0,40), textcoords="offset points",
            ha="center", fontsize=10, fontweight="bold", color="white", zorder=9,
            bbox=dict(boxstyle="round,pad=0.25", fc=PURP, ec="none", alpha=0.92))

# подписи элементов
ax.annotate("оз. Малый Талдыколь", (C.x, C.y), ha="center", fontsize=14, fontweight="bold",
            color="white", zorder=9, bbox=dict(boxstyle="round,pad=0.3", fc="#0369a1", ec="none", alpha=0.85))
mid = arrows[0][0]
ax.annotate("городской + талый сток", mid, xytext=(8,12), textcoords="offset points",
            fontsize=11, fontweight="bold", color=BLUE, zorder=9,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=BLUE, alpha=0.85))
ax.annotate("регулируемый выпуск → ливнёвка", (outlet.x+od[0]*210, outlet.y+od[1]*210),
            xytext=(6,-14), textcoords="offset points", fontsize=9.5, fontweight="bold",
            color="#0369a1", zorder=9, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#0369a1", alpha=0.85))

# ---------- 5. Подложка-спутник ----------
try:
    cx.add_basemap(ax, crs="EPSG:3857", source=cx.providers.Esri.WorldImagery, zoom=16, attribution_size=6)
except Exception as e:
    print("basemap failed:", e)
    try: cx.add_basemap(ax, crs="EPSG:3857", source=cx.providers.OpenStreetMap.Mapnik, zoom=15)
    except Exception as e2: print("basemap2 failed:", e2)

# ---------- 6. Север + масштабная линейка ----------
ax.annotate("С", xy=(0.045,0.95), xytext=(0.045,0.86), xycoords="axes fraction",
            ha="center", fontsize=14, fontweight="bold", color="white",
            arrowprops=dict(arrowstyle="-|>", color="white", lw=2.5, mutation_scale=20))
bar_m = 500.0
bar_len = bar_m / coslat                      # коррекция искажения Web Mercator на 51° с.ш.
x0 = minx - pad + (maxx-minx+2*pad)*0.06
y0 = miny - pad*0.9 + (maxy-miny+1.8*pad)*0.05
ax.add_patch(Rectangle((x0, y0), bar_len, 22, facecolor="white", edgecolor="black", lw=1, zorder=10))
ax.add_patch(Rectangle((x0, y0), bar_len/2, 22, facecolor="black", edgecolor="black", lw=1, zorder=10))
ax.text(x0+bar_len/2, y0+40, "500 м", ha="center", fontsize=10, fontweight="bold",
        color="white", zorder=10)

ax.set_axis_off()
ax.set_title("План площадки: Малый Талдыколь — ливневый накопитель + парк (концепт)",
             fontsize=14, fontweight="bold", color="#0f4c45", pad=14)

# легенда
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
leg = [
    Patch(fc="#38bdf8", ec="#0369a1", alpha=0.6, label="озеро-накопитель"),
    Line2D([0],[0], color=GREEN, lw=6, label="болотные края (доочистка)"),
    Line2D([0],[0], color=GREEN, lw=2.2, ls="--", label="парковое кольцо (тропы)"),
    Line2D([0],[0], color=BLUE, lw=3, marker=">", label="приток стока района"),
    Patch(fc=GOLD, ec="#7c2d12", label="forebay/седиментация"),
]
ax.legend(handles=leg, loc="lower right", framealpha=0.92, fontsize=9.5, edgecolor="#e5e7eb")

ax.text(0.011, 0.012, "Контур озера и дороги: © OpenStreetMap · подложка: Esri World Imagery · "
        "вмешательства — концептуально, к уточнению (Design-фаза)",
        transform=ax.transAxes, fontsize=7.2, color="white", va="bottom",
        bbox=dict(boxstyle="round,pad=0.2", fc="#0f4c45", ec="none", alpha=0.5))

fig.tight_layout()
for ext_ in ("pdf", "svg", "png"):
    fig.savefig(f"site_plan_maly_taldykol.{ext_}", dpi=170, bbox_inches="tight")
print("OK: site_plan_maly_taldykol.{pdf,svg,png}")
