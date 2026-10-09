"""
Build Core Expertise animated SVG — colorful gradient progress bars with glow effects.
Each bar animates from 0 to its target width on load.
"""

W = 840
H = 280
PADDING_X = 30
ROW_H = 36
START_Y = 50
LABEL_W = 210
BAR_X = LABEL_W + PADDING_X + 20
BAR_TOTAL_W = W - BAR_X - PADDING_X - 80  # leave room for % text

skills = [
    ("LLM Agents & RAG",    95, "#00D9FF", "#0095FF"),
    ("Python & ML",          95, "#34D399", "#059669"),
    ("LangChain/LangGraph",  90, "#A78BFA", "#7C3AED"),
    ("FastAPI / React",      80, "#FBBF24", "#F59E0B"),
    ("Deep Learning",        80, "#F472B6", "#EC4899"),
    ("Cloud & DevOps",       65, "#60A5FA", "#3B82F6"),
]

def make_bar(i, name, pct, color1, color2):
    y = START_Y + i * ROW_H
    bar_w = int(BAR_TOTAL_W * pct / 100)
    grad_id = f"g{i}"
    glow_id = f"glow{i}"
    delay = i * 0.18  # stagger each bar

    gradient = f"""
    <linearGradient id="{grad_id}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{color1}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{color2}" stop-opacity="0.8"/>
    </linearGradient>"""

    # Glow filter
    filt = f"""
    <filter id="{glow_id}" x="-5%" y="-50%" width="110%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>"""

    # Background track
    track = f'<rect x="{BAR_X}" y="{y + 8}" width="{BAR_TOTAL_W}" height="18" rx="9" fill="#1e2535" opacity="0.8"/>'

    # Animated fill bar using stroke-dashoffset trick on a rect
    anim_id = f"bar_anim_{i}"
    fill_bar = f"""<rect id="{anim_id}" x="{BAR_X}" y="{y + 8}" width="{bar_w}" height="18" rx="9"
      fill="url(#{grad_id})" filter="url(#{glow_id})">
      <animate attributeName="width" from="0" to="{bar_w}" dur="1.4s" begin="{delay:.2f}s" fill="freeze" calcMode="spline"
        keyTimes="0;1" keySplines="0.4 0 0.2 1"/>
    </rect>"""

    # Shine overlay
    shine = f"""<rect x="{BAR_X}" y="{y + 8}" width="{bar_w}" height="8" rx="4"
      fill="white" opacity="0.1">
      <animate attributeName="width" from="0" to="{bar_w}" dur="1.4s" begin="{delay:.2f}s" fill="freeze" calcMode="spline"
        keyTimes="0;1" keySplines="0.4 0 0.2 1"/>
    </rect>"""

    # Dot marker at end of bar
    dot_x = BAR_X + bar_w
    dot = f"""<circle cx="{dot_x}" cy="{y + 17}" r="5" fill="{color1}">
      <animate attributeName="cx" from="{BAR_X}" to="{dot_x}" dur="1.4s" begin="{delay:.2f}s" fill="freeze" calcMode="spline"
        keyTimes="0;1" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="{delay + 1.1:.2f}s" fill="freeze"/>
      <animate attributeName="r" values="5;8;5" dur="0.6s" begin="{delay + 1.3:.2f}s" fill="freeze"/>
    </circle>"""

    # Label (left)
    label_fill = color1
    label = f"""<text x="{PADDING_X}" y="{y + 21}" font-family="'Segoe UI',sans-serif" font-size="13"
      font-weight="600" fill="{label_fill}">{name}</text>"""

    # % text (right of bar)
    pct_x = BAR_X + BAR_TOTAL_W + 10
    pct_text = f"""<text x="{pct_x}" y="{y + 21}" font-family="'Segoe UI',sans-serif" font-size="13"
      font-weight="700" fill="{color1}" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.4s" begin="{delay + 1.2:.2f}s" fill="freeze"/>
      {pct}%
    </text>"""

    return gradient, filt, track + fill_bar + shine + dot + label + pct_text

gradients = []
filters = []
bars = []
for i, (name, pct, c1, c2) in enumerate(skills):
    g, f, b = make_bar(i, name, pct, c1, c2)
    gradients.append(g)
    filters.append(f)
    bars.append(b)

# Title
title_y = 28
title = f"""<text x="{W//2}" y="{title_y}" text-anchor="middle" font-family="'Segoe UI',sans-serif"
  font-size="17" font-weight="700" fill="#ffffff" letter-spacing="1">
  🎯 CORE EXPERTISE
</text>"""

# Decorative line under title
deco = f'<line x1="30" y1="36" x2="{W-30}" y2="36" stroke="#ffffff" stroke-width="0.5" opacity="0.1"/>'

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    {''.join(gradients)}
    {''.join(filters)}
    <!-- Bg gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#161b2e"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="{W}" height="{H}" rx="16" fill="url(#bgGrad)"/>
  <!-- Border glow -->
  <rect width="{W}" height="{H}" rx="16" fill="none" stroke="#00D9FF" stroke-width="1" opacity="0.25"/>

  {title}
  {deco}

  {''.join(bars)}

</svg>"""

out = r"C:\Users\lenovo\OneDrive\Desktop\github_profile\core_expertise_animated.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Saved: {out} ({len(svg)} bytes)")
