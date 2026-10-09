"""
Rebuild Core Expertise SVG — GitHub-safe, no external filters, 
colorful gradient animated progress bars clearly showing skills.
"""

W = 840
H = 300

skills = [
    ("🤖 LLM Agents & RAG",    95, "#00D9FF", "#0080CC"),
    ("🐍 Python & ML",          95, "#34D399", "#059669"),
    ("🔗 LangChain/LangGraph",  90, "#A78BFA", "#6D28D9"),
    ("⚡ FastAPI / React",       80, "#FBBF24", "#D97706"),
    ("🧠 Deep Learning",         80, "#F472B6", "#BE185D"),
    ("☁️ Cloud & DevOps",        65, "#60A5FA", "#2563EB"),
]

LABEL_W = 240
BAR_X = LABEL_W + 15
BAR_TOTAL_W = W - BAR_X - 80
ROW_H = 40
START_Y = 60

rows = []
defs_content = []

for i, (name, pct, c1, c2) in enumerate(skills):
    y = START_Y + i * ROW_H
    bar_w = int(BAR_TOTAL_W * pct / 100)
    delay = i * 0.2

    # Gradient definition
    defs_content.append(f'''
    <linearGradient id="grad{i}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}" stop-opacity="0.75"/>
    </linearGradient>''')

    # Background track
    track = f'<rect x="{BAR_X}" y="{y+10}" width="{BAR_TOTAL_W}" height="20" rx="10" fill="#1A2035"/>'

    # Filled bar (animates width)
    bar = f'''<rect x="{BAR_X}" y="{y+10}" width="0" height="20" rx="10" fill="url(#grad{i})">
      <animate attributeName="width" from="0" to="{bar_w}" dur="1.5s" begin="{delay:.1f}s" fill="freeze"/>
    </rect>'''

    # Shine on bar
    shine = f'''<rect x="{BAR_X}" y="{y+10}" width="0" height="9" rx="4" fill="white" opacity="0.15">
      <animate attributeName="width" from="0" to="{bar_w}" dur="1.5s" begin="{delay:.1f}s" fill="freeze"/>
    </rect>'''

    # Skill label
    label = f'<text x="{LABEL_W - 10}" y="{y+25}" text-anchor="end" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="600" fill="{c1}">{name}</text>'

    # Percentage label
    pct_text = f'''<text x="{BAR_X + BAR_TOTAL_W + 10}" y="{y+25}" font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="700" fill="{c1}" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay + 1.3:.1f}s" fill="freeze"/>
      {pct}%
    </text>'''

    # End dot
    dot = f'''<circle cx="{BAR_X}" cy="{y+20}" r="6" fill="{c1}">
      <animate attributeName="cx" from="{BAR_X}" to="{BAR_X + bar_w}" dur="1.5s" begin="{delay:.1f}s" fill="freeze"/>
      <animate attributeName="opacity" values="0;1" dur="0.2s" begin="{delay + 1.0:.1f}s" fill="freeze"/>
    </circle>'''

    rows.append(track + bar + shine + label + pct_text + dot)

title_text = '''
  <text x="420" y="35" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif"
    font-size="18" font-weight="900" fill="white" letter-spacing="2" opacity="0.95">
    🎯 CORE EXPERTISE
  </text>
  <line x1="40" y1="44" x2="800" y2="44" stroke="white" stroke-width="0.5" opacity="0.12"/>
'''

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    {''.join(defs_content)}
    <linearGradient id="bgG" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#161b2e"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" rx="16" fill="url(#bgG)"/>
  <rect width="{W}" height="{H}" rx="16" fill="none" stroke="#00D9FF" stroke-width="1" opacity="0.2"/>

  {title_text}

  {''.join(rows)}
</svg>'''

out = r"C:\Users\lenovo\OneDrive\Desktop\github_profile\core_expertise_animated.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Saved: {out} ({len(svg)} bytes)")
