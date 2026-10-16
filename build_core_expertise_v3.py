"""
Core Expertise SVG — pure SMIL animations only (no CSS keyframes).
GitHub-safe: uses only <animate> SMIL which GitHub fully supports in <img> SVGs.
"""

W = 860
H = 320

skills = [
    ("🤖  LLM Agents & RAG",   95, "#00D9FF", "#005F8A"),
    ("🐍  Python & ML",         95, "#34D399", "#065F46"),
    ("🔗  LangChain/LangGraph", 90, "#A78BFA", "#4C1D95"),
    ("⚡  FastAPI / React",      80, "#FBBF24", "#92400E"),
    ("🧠  Deep Learning",        80, "#F472B6", "#831843"),
    ("☁️  Cloud & DevOps",       65, "#60A5FA", "#1E3A8A"),
]

LABEL_W    = 255
BAR_X      = LABEL_W + 12
BAR_MAX_W  = W - BAR_X - 75      # room for % text
ROW_H      = 42
START_Y    = 60

defs  = []
rows  = []

for i, (name, pct, c1, c2) in enumerate(skills):
    y      = START_Y + i * ROW_H
    bar_w  = int(BAR_MAX_W * pct / 100)
    delay  = i * 0.22            # stagger each bar
    gid    = f"g{i}"

    # ── gradient ──────────────────────────────────────────────────
    defs.append(f'''
    <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}" stop-opacity="0.8"/>
    </linearGradient>''')

    # ── track ─────────────────────────────────────────────────────
    track = f'<rect x="{BAR_X}" y="{y+11}" width="{BAR_MAX_W}" height="20" rx="10" fill="#1c2333"/>'

    # ── animated fill bar (SMIL only) ─────────────────────────────
    bar = f'''<rect x="{BAR_X}" y="{y+11}" width="0" height="20" rx="10" fill="url(#{gid})">
      <animate attributeName="width" from="0" to="{bar_w}"
        dur="1.4s" begin="{delay:.2f}s" fill="freeze"
        calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
    </rect>'''

    # ── shine ─────────────────────────────────────────────────────
    shine = f'''<rect x="{BAR_X}" y="{y+11}" width="0" height="9" rx="4" fill="white" opacity="0.18">
      <animate attributeName="width" from="0" to="{bar_w}"
        dur="1.4s" begin="{delay:.2f}s" fill="freeze"
        calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
    </rect>'''

    # ── sliding end-dot ───────────────────────────────────────────
    dot = f'''<circle r="7" cy="{y+21}" fill="{c1}">
      <animate attributeName="cx" from="{BAR_X}" to="{BAR_X + bar_w}"
        dur="1.4s" begin="{delay:.2f}s" fill="freeze"
        calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      <animate attributeName="opacity" from="0" to="1"
        dur="0.1s" begin="{delay:.2f}s" fill="freeze"/>
    </circle>'''

    # ── label (left, colored) ─────────────────────────────────────
    label = (f'<text x="{LABEL_W - 8}" y="{y+26}" text-anchor="end" '
             f'font-family="Segoe UI,Arial,sans-serif" font-size="13" '
             f'font-weight="700" fill="{c1}">{name}</text>')

    # ── pct text (right, fades in after bar) ─────────────────────
    pct_text = f'''<text x="{BAR_X + BAR_MAX_W + 9}" y="{y+26}"
      font-family="Segoe UI,Arial,sans-serif" font-size="13"
      font-weight="700" fill="{c1}" opacity="0">
      <animate attributeName="opacity" from="0" to="1"
        dur="0.3s" begin="{delay + 1.2:.2f}s" fill="freeze"/>
      {pct}%
    </text>'''

    rows.append(track + bar + shine + dot + label + pct_text)

# ── title ─────────────────────────────────────────────────────────
title = (f'<text x="{W//2}" y="36" text-anchor="middle" '
         f'font-family="Segoe UI,Arial,sans-serif" font-size="17" '
         f'font-weight="900" fill="#FFFFFF" letter-spacing="2" opacity="0.95">'
         f'🎯  CORE EXPERTISE</text>')
rule  = (f'<line x1="30" y1="46" x2="{W-30}" y2="46" '
         f'stroke="#FFFFFF" stroke-width="0.6" opacity="0.12"/>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#161b2e"/>
    </linearGradient>
    {''.join(defs)}
  </defs>

  <!-- background card -->
  <rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" rx="16" fill="none"
        stroke="#00D9FF" stroke-width="1" opacity="0.2"/>

  {title}
  {rule}

  {''.join(rows)}
</svg>'''

out = r"C:\Users\lenovo\OneDrive\Desktop\github_profile\core_expertise_animated.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"✅  Core Expertise SVG → {len(svg):,} bytes")
