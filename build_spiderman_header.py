"""
Build Spider-Man themed animated SVG header/background for GitHub Profile README.
Features:
- Dark #0d1117 background with web patterns radiating from corners
- Animated web strand lines with CSS keyframes
- Spider-Man silhouette swinging from left to right across the top
- Red/blue color theme with web motifs
- Fits as a full-width header replacing or alongside the capsule-render banner
"""

W = 900
H = 180

# Spider-Man colors
RED = "#E02020"
BLUE = "#0038A8"
WEB_COLOR = "#C0C0C0"
DARK_RED = "#8B0000"

# Build web pattern (corner radiating lines)
def web_lines(cx, cy, max_r, n_rings, n_spokes, color, opacity):
    lines = []
    import math
    # Spokes
    for s in range(n_spokes):
        angle = (s / n_spokes) * math.pi * 2
        x2 = cx + max_r * math.cos(angle)
        y2 = cy + max_r * math.sin(angle)
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="0.5" opacity="{opacity}"/>')
    # Rings
    for r in range(1, n_rings + 1):
        ring_r = max_r * r / n_rings
        pts = []
        for s in range(n_spokes):
            angle = (s / n_spokes) * math.pi * 2
            x = cx + ring_r * math.cos(angle)
            y = cy + ring_r * math.sin(angle)
            pts.append(f"{x:.1f},{y:.1f}")
        pts.append(pts[0])  # close
        lines.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="0.4" opacity="{opacity}"/>')
    return "\n".join(lines)

import math

# Four corner web patterns
web_tl = web_lines(0, 0, 200, 5, 12, WEB_COLOR, 0.12)
web_tr = web_lines(W, 0, 200, 5, 12, WEB_COLOR, 0.12)
web_bl = web_lines(0, H, 140, 4, 10, WEB_COLOR, 0.08)
web_br = web_lines(W, H, 140, 4, 10, WEB_COLOR, 0.08)

# Animated swinging web strand (bezier curve) — the strand Spider-Man swings on
# Web strand: from top-left (50, -10) arcs to top-right (850, -10) via control point mid-screen
web_strand = """
  <!-- Animated web strand -->
  <path id="webStrand" d="M -50 0 Q 450 80 950 0" fill="none" stroke="#C8C8C8" stroke-width="1.5" opacity="0.35">
    <animate attributeName="d" 
      values="M -50 0 Q 450 80 950 0;M -50 10 Q 450 50 950 10;M -50 0 Q 450 80 950 0" 
      dur="4s" repeatCount="indefinite" calcMode="spline"
      keyTimes="0;0.5;1" keySplines="0.4 0 0.6 1;0.4 0 0.6 1"/>
  </path>
"""

# Spider-Man silhouette (simplified SVG path — simplified body shape)
# We'll use a group with CSS animation for swinging
# Simple stick figure with spider design elements
spidey_body = """
  <g id="spidey">
    <!-- Body circle (torso) -->
    <ellipse cx="0" cy="0" rx="14" ry="18" fill="#CC0000"/>
    <!-- Web pattern lines on chest -->
    <line x1="-14" y1="0" x2="14" y2="0" stroke="#8B0000" stroke-width="1" opacity="0.6"/>
    <line x1="0" y1="-18" x2="0" y2="18" stroke="#8B0000" stroke-width="1" opacity="0.6"/>
    <line x1="-10" y1="-14" x2="10" y2="14" stroke="#8B0000" stroke-width="0.7" opacity="0.5"/>
    <line x1="10" y1="-14" x2="-10" y2="14" stroke="#8B0000" stroke-width="0.7" opacity="0.5"/>
    <!-- Head -->
    <ellipse cx="0" cy="-25" rx="12" ry="13" fill="#CC0000"/>
    <!-- Eyes (white lenses) -->
    <ellipse cx="-5" cy="-27" rx="5" ry="4" fill="white" opacity="0.95"/>
    <ellipse cx="5" cy="-27" rx="5" ry="4" fill="white" opacity="0.95"/>
    <!-- Blue mask border -->
    <ellipse cx="-5" cy="-27" rx="5" ry="4" fill="none" stroke="#0038A8" stroke-width="1"/>
    <ellipse cx="5" cy="-27" rx="5" ry="4" fill="none" stroke="#0038A8" stroke-width="1"/>
    <!-- Blue sides of costume -->
    <path d="M -14 -5 Q -20 5 -14 18 Q -6 10 0 0 Q -6 -10 -14 -5" fill="#0038A8"/>
    <path d="M 14 -5 Q 20 5 14 18 Q 6 10 0 0 Q 6 -10 14 -5" fill="#0038A8"/>
    <!-- Arms up (web-slinging pose) -->
    <line x1="-12" y1="-5" x2="-35" y2="-25" stroke="#CC0000" stroke-width="5" stroke-linecap="round"/>
    <line x1="12" y1="-5" x2="35" y2="-25" stroke="#0038A8" stroke-width="5" stroke-linecap="round"/>
    <!-- Legs -->
    <line x1="-5" y1="18" x2="-15" y2="40" stroke="#CC0000" stroke-width="5" stroke-linecap="round"/>
    <line x1="5" y1="18" x2="15" y2="40" stroke="#0038A8" stroke-width="5" stroke-linecap="round"/>
    <!-- Web lines from hands -->
    <line x1="-35" y1="-25" x2="-80" y2="-10" stroke="#C8C8C8" stroke-width="0.8" opacity="0.6"/>
    <line x1="35" y1="-25" x2="80" y2="-10" stroke="#C8C8C8" stroke-width="0.8" opacity="0.6"/>
  </g>
"""

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Main dark background gradient -->
    <linearGradient id="bgMain" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="50%" stop-color="#0d0f1a"/>
      <stop offset="100%" stop-color="#110d17"/>
    </linearGradient>
    <!-- Red glow for header accent -->
    <radialGradient id="redGlow" cx="50%" cy="0%" r="60%">
      <stop offset="0%" stop-color="#CC0000" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#CC0000" stop-opacity="0"/>
    </radialGradient>
    <!-- Blue glow -->
    <radialGradient id="blueGlow" cx="50%" cy="100%" r="60%">
      <stop offset="0%" stop-color="#0038A8" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#0038A8" stop-opacity="0"/>
    </radialGradient>
    <!-- Spider silhouette filter for glow -->
    <filter id="spideyGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4" result="blur"/>
      <feFlood flood-color="#CC0000" flood-opacity="0.6" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="shadow"/>
      <feMerge><feMergeNode in="shadow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- Web strand filter -->
    <filter id="webGlow">
      <feGaussianBlur stdDeviation="1.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <!-- CSS Animations -->
    <style>
      #spideyGroup {{
        animation: swingAcross 6s ease-in-out infinite;
        transform-origin: 450px 0px;
      }}
      @keyframes swingAcross {{
        0%   {{ transform: translateX(-120px) translateY(10px) rotate(-5deg); }}
        25%  {{ transform: translateX(200px) translateY(-15px) rotate(3deg); }}
        50%  {{ transform: translateX(450px) translateY(5px) rotate(-2deg); }}
        75%  {{ transform: translateX(700px) translateY(-10px) rotate(4deg); }}
        100% {{ transform: translateX(1020px) translateY(10px) rotate(-5deg); }}
      }}
      #webStrand1 {{
        animation: webSway1 3s ease-in-out infinite;
      }}
      @keyframes webSway1 {{
        0%, 100% {{ d: path("M 0 20 Q 150 70 300 30 Q 450 -10 600 40 Q 750 80 900 20"); }}
        50%       {{ d: path("M 0 30 Q 150 50 300 20 Q 450 -20 600 30 Q 750 60 900 30"); }}
      }}
      #webStrand2 {{
        animation: webSway2 4s ease-in-out 1s infinite;
      }}
      @keyframes webSway2 {{
        0%, 100% {{ d: path("M 0 60 Q 225 10 450 50 Q 675 90 900 50"); }}
        50%       {{ d: path("M 0 50 Q 225 20 450 60 Q 675 80 900 40"); }}
      }}
      .webPulse {{
        animation: webPulse 2s ease-in-out infinite;
      }}
      @keyframes webPulse {{
        0%, 100% {{ opacity: 0.15; }}
        50%       {{ opacity: 0.25; }}
      }}
      #spiderTitle {{
        animation: titleFade 1.5s ease-out forwards;
      }}
      @keyframes titleFade {{
        from {{ opacity: 0; transform: translateY(-10px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
      }}
    </style>
  </defs>

  <!-- === BACKGROUND === -->
  <rect width="{W}" height="{H}" fill="url(#bgMain)"/>
  <!-- Color glow overlays -->
  <rect width="{W}" height="{H}" fill="url(#redGlow)"/>
  <rect width="{W}" height="{H}" fill="url(#blueGlow)"/>

  <!-- === WEB PATTERNS (corners) === -->
  <g class="webPulse">
    {web_tl}
  </g>
  <g class="webPulse" style="animation-delay: 1s">
    {web_tr}
  </g>
  <g class="webPulse" style="animation-delay: 0.5s">
    {web_bl}
  </g>
  <g class="webPulse" style="animation-delay: 1.5s">
    {web_br}
  </g>

  <!-- === ANIMATED WEB STRANDS === -->
  <path id="webStrand1" d="M 0 20 Q 150 70 300 30 Q 450 -10 600 40 Q 750 80 900 20"
    fill="none" stroke="#C0C0C0" stroke-width="1.2" opacity="0.3" filter="url(#webGlow)"/>
  <path id="webStrand2" d="M 0 60 Q 225 10 450 50 Q 675 90 900 50"
    fill="none" stroke="#C0C0C0" stroke-width="0.8" opacity="0.2" filter="url(#webGlow)"/>

  <!-- === SPIDERMAN SWINGING === -->
  <g id="spideyGroup" filter="url(#spideyGlow)">
    <g transform="translate(100, 55)">
      {spidey_body}
    </g>
  </g>

  <!-- === TITLE TEXT === -->
  <g id="spiderTitle">
    <!-- Main name -->
    <text x="{W//2}" y="80" text-anchor="middle"
      font-family="'Segoe UI',Arial,sans-serif" font-size="42" font-weight="900"
      fill="white" letter-spacing="3" opacity="0.95">
      VAKA JEEVAN REDDY
    </text>
    <!-- Spider web underline decoration -->
    <line x1="200" y1="92" x2="{W-200}" y2="92" stroke="#CC0000" stroke-width="1.5" opacity="0.6"/>
    <!-- Subtitle -->
    <text x="{W//2}" y="118" text-anchor="middle"
      font-family="'Segoe UI',Arial,sans-serif" font-size="17" font-weight="600"
      fill="#00D9FF" letter-spacing="5">
      AI / ML ENGINEER  ·  LLM ARCHITECT  ·  RAG SPECIALIST
    </text>
    <!-- Small spider icon (⬡ shaped web) each side -->
    <text x="180" y="82" font-size="22" fill="#CC0000" opacity="0.7">🕷</text>
    <text x="{W-200}" y="82" font-size="22" fill="#CC0000" opacity="0.7">🕷</text>
  </g>

  <!-- === BOTTOM BORDER === -->
  <line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="#CC0000" stroke-width="2" opacity="0.4"/>
  <line x1="0" y1="{H-1}" x2="{W}" y2="{H-1}" stroke="#0038A8" stroke-width="1" opacity="0.2" stroke-dasharray="20 10"/>

</svg>"""

out = r"C:\Users\lenovo\OneDrive\Desktop\github_profile\spiderman_header.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg_content)
print(f"Saved: {out} ({len(svg_content)} bytes)")
