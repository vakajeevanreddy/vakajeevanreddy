"""
Build Spider-Man SECTION DIVIDERS — full-width SVGs that go between each section.
Spider-Man swings from LEFT→RIGHT in divider 1, RIGHT→LEFT in divider 2, etc.
Each divider shows him at a different point in the swing so as you scroll it looks
like he's continuously swinging down the page.
"""
import math

W = 900
H = 100  # thin horizontal banner between sections

def web_bg(cx, cy, max_r, n_spokes, opacity):
    lines = []
    for s in range(n_spokes):
        angle = (s / n_spokes) * math.pi * 2
        x2 = cx + max_r * math.cos(angle)
        y2 = cy + max_r * math.sin(angle)
        lines.append(f'<line x1="{cx:.0f}" y1="{cy:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#C0C0C0" stroke-width="0.6" opacity="{opacity}"/>')
    for r in [0.4, 0.7, 1.0]:
        ring_r = max_r * r
        pts = []
        for s in range(n_spokes):
            angle = (s / n_spokes) * math.pi * 2
            x = cx + ring_r * math.cos(angle)
            y = cy + ring_r * math.sin(angle)
            pts.append(f"{x:.0f},{y:.0f}")
        pts.append(pts[0])
        lines.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#C0C0C0" stroke-width="0.4" opacity="{opacity}"/>')
    return "\n".join(lines)

# Spidey mini body for dividers (compact version)
def spidey_mini(cx, cy, facing_right=True, rope_angle_deg=-45):
    """Draw a small spider-man figure swinging on a rope"""
    flip = 1 if facing_right else -1
    # Rope from top
    rx = cx + flip * 20
    rope_len = 55
    rope_x2 = cx
    rope_y2 = cy - 30
    
    # Web line anchor at top
    anchor_x = cx - flip * 80
    anchor_y = cy - rope_len
    
    s = f'''
    <!-- Web rope -->
    <line x1="{anchor_x}" y1="{anchor_y}" x2="{cx}" y2="{cy - 28}" 
      stroke="#D0D0D0" stroke-width="1.8" opacity="0.85"/>
    <!-- Head -->
    <ellipse cx="{cx}" cy="{cy - 28}" rx="14" ry="16" fill="#CC0000"/>
    <!-- Eyes -->
    <ellipse cx="{cx - flip*4}" cy="{cy - 31}" rx="6" ry="5" fill="white" opacity="0.95"/>
    <ellipse cx="{cx + flip*4}" cy="{cy - 31}" rx="6" ry="5" fill="white" opacity="0.95"/>
    <!-- Torso -->
    <ellipse cx="{cx}" cy="{cy - 5}" rx="16" ry="22" fill="#CC0000"/>
    <!-- Blue sides -->
    <path d="M {cx - 16} {cy - 15} Q {cx - 22} {cy - 5} {cx - 16} {cy + 12} Q {cx - 8} {cy + 5} {cx} {cy - 5} Q {cx - 8} {cy - 16} {cx - 16} {cy - 15} Z" fill="#0033CC" opacity="0.9"/>
    <path d="M {cx + 16} {cy - 15} Q {cx + 22} {cy - 5} {cx + 16} {cy + 12} Q {cx + 8} {cy + 5} {cx} {cy - 5} Q {cx + 8} {cy - 16} {cx + 16} {cy - 15} Z" fill="#0033CC" opacity="0.9"/>
    <!-- Spider emblem -->
    <ellipse cx="{cx}" cy="{cy - 5}" rx="5" ry="7" fill="#111" opacity="0.8"/>
    <!-- Left arm (up, shooting web) -->
    <line x1="{cx - flip*14}" y1="{cy - 15}" x2="{cx - flip*35}" y2="{cy - 45}" stroke="#CC0000" stroke-width="6" stroke-linecap="round"/>
    <!-- Right arm (gripping rope) -->
    <line x1="{cx + flip*14}" y1="{cy - 20}" x2="{anchor_x}" y2="{anchor_y}" stroke="#CC0000" stroke-width="5" stroke-linecap="round" opacity="0.7"/>
    <!-- Left leg -->
    <line x1="{cx - 8}" y1="{cy + 17}" x2="{cx - flip*25}" y2="{cy + 50}" stroke="#0033CC" stroke-width="7" stroke-linecap="round"/>
    <!-- Right leg -->
    <line x1="{cx + 8}" y1="{cy + 17}" x2="{cx + flip*30}" y2="{cy + 45}" stroke="#0033CC" stroke-width="7" stroke-linecap="round"/>
    <!-- Boots -->
    <ellipse cx="{cx - flip*25}" cy="{cy + 52}" rx="10" ry="7" fill="#CC0000"/>
    <ellipse cx="{cx + flip*30}" cy="{cy + 47}" rx="10" ry="7" fill="#CC0000"/>
    <!-- Web from shooting hand -->
    <line x1="{cx - flip*35}" y1="{cy - 45}" x2="{cx - flip*120}" y2="{cy - 75}" 
      stroke="#D0D0D0" stroke-width="1.2" opacity="0.7"/>
    '''
    return s

def make_divider(n, spidey_x, facing_right=True, web_left=True, label=""):
    """Build one divider SVG"""
    
    web1 = web_bg(0 if web_left else W, 0, 140, 10, 0.1)
    web2 = web_bg(W if web_left else 0, H, 120, 8, 0.09)

    # Animated web strand
    ctrl_y = 50 if facing_right else 30
    web_strand = f'<path d="M 0 {H//2} Q {W//2} {ctrl_y} {W} {H//2}" fill="none" stroke="#C0C0C0" stroke-width="1" opacity="0.2"/>'

    # A second strand
    web_strand2 = f'<path d="M 0 {H//3} Q {W//3} {H*2//3} {W*2//3} {H//4} Q {W*4//5} 10 {W} {H//3}" fill="none" stroke="#C0C0C0" stroke-width="0.7" opacity="0.15"/>'

    anim_dir = "leftRight" if facing_right else "rightLeft"
    
    spidey = spidey_mini(spidey_x, 65, facing_right)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="divBg{n}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#CC0000" stop-opacity="0.07"/>
      <stop offset="50%" stop-color="#0d1117" stop-opacity="1"/>
      <stop offset="100%" stop-color="#0033CC" stop-opacity="0.07"/>
    </linearGradient>
    <filter id="spideyGlow{n}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="blur"/>
      <feFlood flood-color="#CC0000" flood-opacity="0.5" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      #spideyDiv{n} {{
        animation: swing{n} 0.8s ease-in-out infinite alternate;
        transform-origin: {spidey_x}px 10px;
      }}
      @keyframes swing{n} {{
        from {{ transform: rotate(-4deg); }}
        to   {{ transform: rotate(4deg); }}
      }}
      .divWebPulse{n} {{
        animation: pulse{n} 2.5s ease-in-out infinite;
      }}
      @keyframes pulse{n} {{
        0%, 100% {{ opacity: 0.1; }}
        50%       {{ opacity: 0.2; }}
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#divBg{n})"/>
  
  <!-- Horizontal center line -->
  <line x1="0" y1="{H//2}" x2="{W}" y2="{H//2}" stroke="#CC0000" stroke-width="0.5" opacity="0.15" stroke-dasharray="8 6"/>

  <!-- Web corner patterns -->
  <g class="divWebPulse{n}">{web1}</g>
  <g class="divWebPulse{n}" style="animation-delay: 1.2s">{web2}</g>

  <!-- Web strands -->
  {web_strand}
  {web_strand2}

  <!-- Spider-Man character -->
  <g id="spideyDiv{n}" filter="url(#spideyGlow{n})">
    {spidey}
  </g>

  <!-- Top & bottom border lines -->
  <line x1="0" y1="0" x2="{W}" y2="0" stroke="#CC0000" stroke-width="1.5" opacity="0.35"/>
  <line x1="0" y1="{H}" x2="{W}" y2="{H}" stroke="#0033CC" stroke-width="1.5" opacity="0.25"/>
</svg>'''
    return svg

# ── Generate 5 dividers (one between each major section) ──────────────────────
dividers = [
    (1,  150, True,  True),   # Section 1→2: After header, swings from left
    (2,  650, False, False),  # Section 2→3: After About Me, swings right→left
    (3,  200, True,  True),   # Section 3→4: After Key Skills
    (4,  700, False, False),  # Section 4→5: After Experience
    (5,  300, True,  True),   # Section 5→6: After Projects
]

for n, x, facing, web_left in dividers:
    svg = make_divider(n, x, facing, web_left)
    out = fr"C:\Users\lenovo\OneDrive\Desktop\github_profile\spidey_divider_{n}.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Saved divider {n}: {out}")

print("All dividers done!")
