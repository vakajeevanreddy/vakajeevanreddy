import os
os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")

# ---- Core Expertise SVG ------------------------------------------------
W, H = 860, 320
skills = [
    ("LLM Agents & RAG",   95, "#00D9FF", "#005F8A"),
    ("Python & ML",        95, "#34D399", "#065F46"),
    ("LangChain/LangGraph",90, "#A78BFA", "#4C1D95"),
    ("FastAPI / React",    80, "#FBBF24", "#92400E"),
    ("Deep Learning",      80, "#F472B6", "#831843"),
    ("Cloud & DevOps",     65, "#60A5FA", "#1E3A8A"),
]
LABEL_W, BAR_X = 250, 265
BAR_MAX_W = W - BAR_X - 75
ROW_H, START_Y = 42, 60

defs, rows = [], []
for i, (name, pct, c1, c2) in enumerate(skills):
    y, bw, d = START_Y + i * ROW_H, int(BAR_MAX_W * pct / 100), i * 0.22
    defs.append(
        f'<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{c1}"/>'
        f'<stop offset="100%" stop-color="{c2}" stop-opacity="0.8"/>'
        f'</linearGradient>'
    )
    spline = 'calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"'
    track  = f'<rect x="{BAR_X}" y="{y+11}" width="{BAR_MAX_W}" height="20" rx="10" fill="#1c2333"/>'
    bar    = (f'<rect x="{BAR_X}" y="{y+11}" width="0" height="20" rx="10" fill="url(#g{i})">'
              f'<animate attributeName="width" from="0" to="{bw}" dur="1.4s" begin="{d:.2f}s" fill="freeze" {spline}/>'
              f'</rect>')
    shine  = (f'<rect x="{BAR_X}" y="{y+11}" width="0" height="9" rx="4" fill="white" opacity="0.18">'
              f'<animate attributeName="width" from="0" to="{bw}" dur="1.4s" begin="{d:.2f}s" fill="freeze" {spline}/>'
              f'</rect>')
    dot    = (f'<circle r="7" cy="{y+21}" fill="{c1}">'
              f'<animate attributeName="cx" from="{BAR_X}" to="{BAR_X+bw}" dur="1.4s" begin="{d:.2f}s" fill="freeze" {spline}/>'
              f'<animate attributeName="opacity" from="0" to="1" dur="0.1s" begin="{d:.2f}s" fill="freeze"/>'
              f'</circle>')
    label  = (f'<text x="{BAR_X - 10}" y="{y+26}" text-anchor="end" '
              f'font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" fill="{c1}">{name}</text>')
    ptxt   = (f'<text x="{BAR_X+BAR_MAX_W+9}" y="{y+26}" '
              f'font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" fill="{c1}" opacity="0">'
              f'<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{d+1.2:.2f}s" fill="freeze"/>'
              f'{pct}%</text>')
    rows.append(track + bar + shine + dot + label + ptxt)

title = (f'<text x="{W//2}" y="36" text-anchor="middle" '
         f'font-family="Segoe UI,Arial,sans-serif" font-size="17" '
         f'font-weight="900" fill="#FFFFFF" letter-spacing="2">CORE EXPERTISE</text>')
rule = f'<line x1="30" y1="46" x2="{W-30}" y2="46" stroke="#FFFFFF" stroke-width="0.6" opacity="0.12"/>'

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
       f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
       f'<stop offset="0%" stop-color="#0d1117"/><stop offset="100%" stop-color="#161b2e"/>'
       f'</linearGradient>{"".join(defs)}</defs>'
       f'<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>'
       f'<rect width="{W}" height="{H}" rx="16" fill="none" stroke="#00D9FF" stroke-width="1" opacity="0.2"/>'
       f'{title}{rule}{"".join(rows)}</svg>')

with open("core_expertise_animated.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("Core Expertise SVG:", len(svg), "bytes")

# ---- Streak SVG --------------------------------------------------------
W2, H2 = 860, 200
STREAK, TOTAL, LONGEST = 14, 278, 21
weeks = [2, 4, 1, 0, 3, 5, 2, 8, 6, 12, 15, 18]
MAX_B = max(weeks)
BAR_W2, BAR_GAP = 20, 8
BSX, BSY = 432, 155

bars = []
for i, v in enumerate(weeks):
    bh = int((v / MAX_B) * 100) if v > 0 else 0
    x, yt, d2 = BSX + i * (BAR_W2 + BAR_GAP), BSY - bh, 0.05 + i * 0.08
    alpha = max(0.3, 0.3 + 0.7 * (v / MAX_B))
    sp = 'calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"'
    if v == 0:
        bars.append(f'<rect x="{x}" y="{BSY-4}" width="{BAR_W2}" height="4" rx="2" fill="#2d333b"/>')
    else:
        bars.append(
            f'<rect x="{x}" y="{BSY}" width="{BAR_W2}" height="0" rx="3" fill="#39D353" opacity="{alpha:.2f}">'
            f'<animate attributeName="height" from="0" to="{bh}" dur="0.9s" begin="{d2:.2f}s" fill="freeze" {sp}/>'
            f'<animate attributeName="y" from="{BSY}" to="{yt}" dur="0.9s" begin="{d2:.2f}s" fill="freeze" {sp}/>'
            f'</rect>'
        )

# fire emoji as text (unicode safe)
fire = "&#x1F525;"

svg2_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" viewBox="0 0 {W2} {H2}">',
    f'<defs>',
    f'<linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">',
    f'<stop offset="0%" stop-color="#0d1117"/><stop offset="100%" stop-color="#161b2e"/></linearGradient>',
    f'<filter id="fg"><feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur"/>',
    f'<feFlood flood-color="#FF6600" flood-opacity="0.7" result="color"/>',
    f'<feComposite in="color" in2="blur" operator="in" result="glow"/>',
    f'<feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
    f'</defs>',
    f'<rect width="{W2}" height="{H2}" rx="16" fill="url(#bg2)"/>',
    f'<rect width="{W2}" height="{H2}" rx="16" fill="none" stroke="#30363D" stroke-width="1"/>',
    # Left panel
    f'<rect x="12" y="12" width="200" height="{H2-24}" rx="12" fill="#161B22" opacity="0.8"/>',
    f'<text x="112" y="30" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700" fill="#58A6FF">CURRENT STREAK</text>',
    f'<text x="112" y="82" text-anchor="middle" font-size="44" filter="url(#fg)">{fire}<animate attributeName="font-size" values="44;50;44" dur="1.4s" repeatCount="indefinite"/></text>',
    f'<text x="112" y="125" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="36" font-weight="900" fill="#39D353" opacity="0">{STREAK}<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="0.8s" fill="freeze"/></text>',
    f'<text x="112" y="148" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#8B949E">day streak</text>',
    # Middle panel
    f'<rect x="224" y="12" width="192" height="{H2-24}" rx="12" fill="#161B22" opacity="0.8"/>',
    f'<text x="320" y="30" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700" fill="#58A6FF">CONTRIBUTIONS</text>',
    f'<text x="320" y="90" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="44" font-weight="900" fill="#FFFFFF" opacity="0">{TOTAL}<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.5s" fill="freeze"/></text>',
    f'<text x="320" y="112" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="13" fill="#8B949E">last 12 months</text>',
    f'<line x1="244" y1="130" x2="406" y2="130" stroke="#30363D" stroke-width="0.8"/>',
    f'<text x="272" y="155" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="800" fill="#F59E0B" opacity="0">{LONGEST}<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="1.0s" fill="freeze"/></text>',
    f'<text x="272" y="172" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="#8B949E">longest streak</text>',
    f'<text x="368" y="155" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="800" fill="#A78BFA" opacity="0">5+<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="1.1s" fill="freeze"/></text>',
    f'<text x="368" y="172" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="#8B949E">active repos</text>',
    # Right panel
    f'<rect x="428" y="12" width="{W2-440}" height="{H2-24}" rx="12" fill="#161B22" opacity="0.8"/>',
    f'<text x="{BSX + (len(weeks)*(BAR_W2+BAR_GAP))//2}" y="34" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700" fill="#58A6FF">WEEKLY COMMITS (3 months)</text>',
] + bars + [
    f'<text x="{BSX}" y="178" font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#8B949E">Aug</text>',
    f'<text x="{BSX+4*(BAR_W2+BAR_GAP)}" y="178" font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#8B949E">Sep</text>',
    f'<text x="{BSX+8*(BAR_W2+BAR_GAP)}" y="178" font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#8B949E">Oct</text>',
    f'<line x1="{BSX-5}" y1="{BSY}" x2="{BSX+len(weeks)*(BAR_W2+BAR_GAP)+5}" y2="{BSY}" stroke="#30363D" stroke-width="1"/>',
    f'</svg>',
]

svg2 = "\n".join(svg2_parts)
with open("streak_animated.svg", "w", encoding="utf-8") as f:
    f.write(svg2)
print("Streak SVG:", len(svg2), "bytes")
