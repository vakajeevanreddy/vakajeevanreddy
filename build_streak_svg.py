"""
Animated GitHub Streak SVG — fire counter + live-looking streak display.
Uses SMIL animations only. Shows:
  - 🔥 Animated fire with pulsing glow
  - Streak counter counting up from 0
  - Weekly contribution bars rising
  - Total contributions counter
  - Clean dark card matching GitHub profile theme
"""

W  = 860
H  = 200

# Real data from the user's GitHub (from screenshots)
STREAK_DAYS        = 14     # visible recent streak from graph
TOTAL_CONTRIBUTIONS= 278    # "278 contributions in the last year"
LONGEST_STREAK     = 21
CURRENT_STREAK     = 14

# Weekly contribution data (approximate from screenshot, Mon-Sun pattern)
# Using 12 weeks of bars (3 months) for the animated chart
weeks = [2, 4, 1, 0, 3, 5, 2, 8, 6, 12, 15, 18]  # contributions per week
MAX_BAR = max(weeks)
BAR_W   = 20
BAR_GAP = 8
BARS_START_X = 430
BARS_Y_BASE  = 155

def make_bar(i, val):
    bar_h  = int((val / MAX_BAR) * 100) if MAX_BAR > 0 else 0
    x      = BARS_START_X + i * (BAR_W + BAR_GAP)
    y_top  = BARS_Y_BASE - bar_h
    delay  = 0.05 + i * 0.08
    # color: brighter = more contributions
    alpha  = 0.3 + 0.7 * (val / MAX_BAR) if MAX_BAR > 0 else 0.3
    color  = f"rgba(57,211,83,{alpha:.2f})"
    if val == 0:
        return f'<rect x="{x}" y="{BARS_Y_BASE - 4}" width="{BAR_W}" height="4" rx="2" fill="#2d333b"/>'
    return f'''<rect x="{x}" y="{BARS_Y_BASE}" width="{BAR_W}" height="0" rx="3" fill="{color}">
      <animate attributeName="height" from="0" to="{bar_h}" dur="0.9s" begin="{delay:.2f}s" fill="freeze"
        calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
      <animate attributeName="y" from="{BARS_Y_BASE}" to="{y_top}" dur="0.9s" begin="{delay:.2f}s" fill="freeze"
        calcMode="spline" keyTimes="0;1" keySplines="0.25 0.1 0.25 1"/>
    </rect>'''

bars_svg = "\n  ".join(make_bar(i, v) for i, v in enumerate(weeks))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Background -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#161b2e"/>
    </linearGradient>

    <!-- Fire glow filter -->
    <filter id="fireGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur"/>
      <feFlood flood-color="#FF6600" flood-opacity="0.7" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Number glow -->
    <filter id="numGlow">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4" result="blur"/>
      <feFlood flood-color="#39D353" flood-opacity="0.6" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- ── Background card ── -->
  <rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" rx="16" fill="none" stroke="#30363D" stroke-width="1"/>

  <!-- ── LEFT PANEL: Fire Streak ── -->
  <!-- Panel bg -->
  <rect x="12" y="12" width="200" height="{H-24}" rx="12" fill="#161B22" opacity="0.8"/>

  <!-- Fire emoji with glow + pulse -->
  <text x="112" y="80" text-anchor="middle" font-size="48" filter="url(#fireGlow)">
    🔥
    <animate attributeName="font-size" values="48;54;48" dur="1.5s" repeatCount="indefinite"
      calcMode="spline" keyTimes="0;0.5;1" keySplines="0.4 0 0.6 1;0.4 0 0.6 1"/>
    <animate attributeName="opacity"   values="0.9;1;0.9" dur="1.5s" repeatCount="indefinite"/>
  </text>

  <!-- Current streak number — counts up 0→{CURRENT_STREAK} -->
  <text x="112" y="125" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="36" font-weight="900"
        fill="#39D353" filter="url(#numGlow)" opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="0.8s" fill="freeze"/>
    {CURRENT_STREAK}
  </text>

  <!-- "day streak" label -->
  <text x="112" y="148" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="13" font-weight="600"
        fill="#8B949E">
    day streak
  </text>
  <!-- Title above -->
  <text x="112" y="30" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700"
        fill="#58A6FF" letter-spacing="1">
    🔥 CURRENT STREAK
  </text>

  <!-- ── MIDDLE PANEL: Stats ── -->
  <rect x="224" y="12" width="192" height="{H-24}" rx="12" fill="#161B22" opacity="0.8"/>

  <!-- Total contributions -->
  <text x="320" y="30" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700"
        fill="#58A6FF" letter-spacing="1">
    📊 CONTRIBUTIONS
  </text>

  <!-- Big count -->
  <text x="320" y="90" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="44" font-weight="900"
        fill="#FFFFFF" opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="0.5s" fill="freeze"/>
    {TOTAL_CONTRIBUTIONS}
  </text>
  <text x="320" y="112" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="13"
        fill="#8B949E">last 12 months</text>

  <!-- Divider -->
  <line x1="244" y1="130" x2="406" y2="130" stroke="#30363D" stroke-width="0.8"/>

  <!-- Longest streak -->
  <text x="272" y="155" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="800"
        fill="#F59E0B" opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="1.0s" fill="freeze"/>
    {LONGEST_STREAK}
  </text>
  <text x="272" y="172" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="#8B949E">
    longest streak
  </text>

  <!-- Repos -->
  <text x="368" y="155" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="22" font-weight="800"
        fill="#A78BFA" opacity="0">
    <animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="1.1s" fill="freeze"/>
    5+
  </text>
  <text x="368" y="172" text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="11" fill="#8B949E">
    active repos
  </text>

  <!-- ── RIGHT PANEL: Contribution Chart ── -->
  <rect x="428" y="12" width="{W - 428 - 12}" height="{H-24}" rx="12" fill="#161B22" opacity="0.8"/>

  <text x="{BARS_START_X + (len(weeks) * (BAR_W + BAR_GAP)) // 2}" y="34"
        text-anchor="middle"
        font-family="Segoe UI,Arial,sans-serif" font-size="12" font-weight="700"
        fill="#58A6FF" letter-spacing="1">
    📈 WEEKLY COMMITS (last 3 months)
  </text>

  <!-- Bars -->
  {bars_svg}

  <!-- Month labels -->
  <text x="{BARS_START_X}" y="178"
        font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#8B949E">Aug</text>
  <text x="{BARS_START_X + 4*(BAR_W+BAR_GAP)}" y="178"
        font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#8B949E">Sep</text>
  <text x="{BARS_START_X + 8*(BAR_W+BAR_GAP)}" y="178"
        font-family="Segoe UI,Arial,sans-serif" font-size="10" fill="#8B949E">Oct</text>

  <!-- baseline -->
  <line x1="{BARS_START_X - 5}" y1="{BARS_Y_BASE}" x2="{BARS_START_X + len(weeks)*(BAR_W+BAR_GAP) + 5}" y2="{BARS_Y_BASE}"
        stroke="#30363D" stroke-width="1"/>

</svg>'''

out = r"C:\Users\lenovo\OneDrive\Desktop\github_profile\streak_animated.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"✅  Streak SVG → {len(svg):,} bytes")
