import xml.etree.ElementTree as ET

W = 460
H = 260

skills = [
    ("LLM Agents & RAG", 95, "#00D9FF", "#007799"),
    ("Python & ML Systems", 95, "#34D399", "#057A55"),
    ("LangChain & LangGraph", 90, "#A78BFA", "#6D28D9"),
    ("FastAPI & Microservices", 85, "#FBBF24", "#D97706"),
    ("Deep Learning & PyTorch", 80, "#F472B6", "#DB2777"),
    ("Cloud & MLOps (AWS/Docker)", 75, "#60A5FA", "#2563EB"),
]

ROW_H = 34
START_Y = 40
BAR_X = 185
MAX_BAR_W = 205

defs_list = [
    '<linearGradient id="cardBg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0%" stop-color="#161B22"/>'
    '<stop offset="100%" stop-color="#0D1117"/>'
    '</linearGradient>'
]

rows = []
for i, (name, pct, c1, c2) in enumerate(skills):
    y = START_Y + i * ROW_H
    bw = int(MAX_BAR_W * pct / 100)
    delay = 0.1 + i * 0.15
    gid = f"g{i}"
    
    # Escape & for XML
    safe_name = name.replace("&", "&amp;")
    
    defs_list.append(
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{c1}"/>'
        f'<stop offset="100%" stop-color="{c2}"/>'
        f'</linearGradient>'
    )
    
    # Track
    track = f'<rect x="{BAR_X}" y="{y+4}" width="{MAX_BAR_W}" height="14" rx="7" fill="#21262D"/>'
    
    # Animated fill
    fill = (
        f'<rect x="{BAR_X}" y="{y+4}" width="0" height="14" rx="7" fill="url(#{gid})">'
        f'<animate attributeName="width" from="0" to="{bw}" dur="1.2s" begin="{delay:.2f}s" fill="freeze" '
        f'calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>'
        f'</rect>'
    )
    
    # Animated shine
    shine = (
        f'<rect x="{BAR_X}" y="{y+4}" width="0" height="6" rx="3" fill="#ffffff" opacity="0.2">'
        f'<animate attributeName="width" from="0" to="{bw}" dur="1.2s" begin="{delay:.2f}s" fill="freeze" '
        f'calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>'
        f'</rect>'
    )
    
    # Glow dot
    dot = (
        f'<circle r="5" cy="{y+11}" fill="{c1}">'
        f'<animate attributeName="cx" from="{BAR_X}" to="{BAR_X+bw}" dur="1.2s" begin="{delay:.2f}s" fill="freeze" '
        f'calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.2s" begin="{delay:.2f}s" fill="freeze"/>'
        f'</circle>'
    )
    
    # Label
    label = (
        f'<text x="{BAR_X - 10}" y="{y+15}" text-anchor="end" '
        f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="11" font-weight="600" fill="{c1}">{safe_name}</text>'
    )
    
    # Percentage
    pct_text = (
        f'<text x="{BAR_X + MAX_BAR_W + 8}" y="{y+15}" '
        f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="11" font-weight="700" fill="{c1}" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{delay + 0.9:.2f}s" fill="freeze"/>'
        f'{pct}%</text>'
    )
    
    rows.append(track + fill + shine + dot + label + pct_text)

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
    f'<defs>\n' + '\n'.join(defs_list) + '\n</defs>\n'
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#cardBg)" stroke="#30363D" stroke-width="1.5"/>\n'
    f'<text x="16" y="24" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
    f'font-size="12" font-weight="700" fill="#00D9FF" letter-spacing="1">⚡ PRODUCTION COMPETENCIES</text>\n'
    f'<line x1="16" y1="30" x2="{W-16}" y2="30" stroke="#30363D" stroke-width="1"/>\n'
    + '\n'.join(rows) +
    f'\n</svg>'
)

with open("core_expertise_animated.svg", "w", encoding="utf-8") as f:
    f.write(svg)

# Strictly validate XML
tree = ET.parse("core_expertise_animated.svg")
print("SUCCESS: core_expertise_animated.svg is strictly valid XML!")
