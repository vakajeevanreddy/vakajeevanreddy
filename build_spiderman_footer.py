"""
Build Spider-Man themed footer SVG — bottom wave with web pattern and spider icon.
Matches the header theme.
"""
import math

W = 900
H = 80
WEB_COLOR = "#C0C0C0"

def web_corner(cx, cy, max_r, n_rings, n_spokes, opacity):
    lines = []
    for s in range(n_spokes):
        angle = (s / n_spokes) * math.pi * 2
        x2 = cx + max_r * math.cos(angle)
        y2 = cy + max_r * math.sin(angle)
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{WEB_COLOR}" stroke-width="0.5" opacity="{opacity}"/>')
    for r in range(1, n_rings + 1):
        ring_r = max_r * r / n_rings
        pts = []
        for s in range(n_spokes):
            angle = (s / n_spokes) * math.pi * 2
            x = cx + ring_r * math.cos(angle)
            y = cy + ring_r * math.sin(angle)
            pts.append(f"{x:.1f},{y:.1f}")
        pts.append(pts[0])
        lines.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{WEB_COLOR}" stroke-width="0.4" opacity="{opacity}"/>')
    return "\n".join(lines)

web_bl = web_corner(0, H, 120, 4, 10, 0.12)
web_br = web_corner(W, H, 120, 4, 10, 0.12)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="footerBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#110d17"/>
    </linearGradient>
    <style>
      .footerWeb {{
        animation: footerPulse 3s ease-in-out infinite;
      }}
      @keyframes footerPulse {{
        0%, 100% {{ opacity: 0.12; }}
        50%       {{ opacity: 0.22; }}
      }}
    </style>
  </defs>
  <!-- Background -->
  <rect width="{W}" height="{H}" fill="url(#footerBg)"/>
  <!-- Top wave (mirrored) -->
  <path d="M 0 0 Q 225 50 450 30 Q 675 10 900 0 L 900 {H} L 0 {H} Z"
    fill="#CC0000" opacity="0.06"/>
  <path d="M 0 10 Q 225 55 450 35 Q 675 15 900 10 L 900 {H} L 0 {H} Z"
    fill="#0038A8" opacity="0.05"/>
  <!-- Web patterns -->
  <g class="footerWeb">{web_bl}</g>
  <g class="footerWeb" style="animation-delay: 1.5s">{web_br}</g>
  <!-- Top border -->
  <line x1="0" y1="0" x2="{W}" y2="0" stroke="#CC0000" stroke-width="2" opacity="0.4"/>
  <line x1="0" y1="0" x2="{W}" y2="0" stroke="#0038A8" stroke-width="1" opacity="0.2" stroke-dasharray="20 10"/>
  <!-- Center spider icon -->
  <text x="{W//2}" y="50" text-anchor="middle" font-size="28" opacity="0.55">🕷️</text>
  <!-- Made with text -->
  <text x="{W//2}" y="68" text-anchor="middle" font-family="'Segoe UI',sans-serif"
    font-size="11" fill="#666" letter-spacing="1">Built with ❤️ by Vaka Jeevan Reddy · AI/ML Engineer</text>
</svg>"""

out = r"C:\Users\lenovo\OneDrive\Desktop\github_profile\spiderman_footer.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Saved: {out} ({len(svg)} bytes)")
