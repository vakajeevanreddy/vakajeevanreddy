print("Rebuilding Pixel-Perfect Animated GitHub Analytics Dashboard SVG...")

W, H = 820, 240

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<style>
  @keyframes dash {{
    0% {{ stroke-dashoffset: 600; }}
    50% {{ stroke-dashoffset: 0; }}
    100% {{ stroke-dashoffset: 0; }}
  }}
  @keyframes pulseGlow {{
    0%, 100% {{ filter: drop-shadow(0 0 2px rgba(0, 217, 255, 0.4)); }}
    50% {{ filter: drop-shadow(0 0 8px rgba(0, 217, 255, 0.8)); }}
  }}
  @keyframes spinDonut {{
    0% {{ stroke-dashoffset: 300; }}
    50% {{ stroke-dashoffset: 65; }}
    100% {{ stroke-dashoffset: 65; }}
  }}
  @keyframes barGrow1 {{ 0% {{ width: 0; }} 100% {{ width: 145px; }} }}
  @keyframes barGrow2 {{ 0% {{ width: 0; }} 100% {{ width: 105px; }} }}
  @keyframes barGrow3 {{ 0% {{ width: 0; }} 100% {{ width: 65px; }} }}
  @keyframes barGrow4 {{ 0% {{ width: 0; }} 100% {{ width: 40px; }} }}
  
  .chart-line {{
    stroke-dasharray: 600;
    stroke-dashoffset: 600;
    animation: dash 3.5s ease-out infinite;
  }}
  .chart-area {{
    animation: pulseGlow 3s ease-in-out infinite;
  }}
  .donut-ring {{
    stroke-dasharray: 300;
    animation: spinDonut 3.5s ease-in-out infinite alternate;
  }}
  .b1 {{ animation: barGrow1 1.8s cubic-bezier(0.25, 1, 0.5, 1) forwards; }}
  .b2 {{ animation: barGrow2 2.0s cubic-bezier(0.25, 1, 0.5, 1) forwards; }}
  .b3 {{ animation: barGrow3 2.2s cubic-bezier(0.25, 1, 0.5, 1) forwards; }}
  .b4 {{ animation: barGrow4 2.4s cubic-bezier(0.25, 1, 0.5, 1) forwards; }}
</style>

<linearGradient id="dbBg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0d1117"/>
  <stop offset="100%" stop-color="#161b22"/>
</linearGradient>

<linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#00D9FF"/>
  <stop offset="50%" stop-color="#7928CA"/>
  <stop offset="100%" stop-color="#FF0080"/>
</linearGradient>

<linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#00D9FF" stop-opacity="0.3"/>
  <stop offset="100%" stop-color="#00D9FF" stop-opacity="0.0"/>
</linearGradient>

<linearGradient id="donutGrad" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#00D9FF"/>
  <stop offset="100%" stop-color="#A78BFA"/>
</linearGradient>
</defs>

<!-- Outer Container -->
<rect width="{W}" height="{H}" rx="16" fill="url(#dbBg)" stroke="#30363d" stroke-width="1.5"/>

<!-- Top Header -->
<text x="20" y="32" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="14" font-weight="bold" fill="#00D9FF">📈 AI/ML &amp; Code Velocity Analytics</text>
<text x="{W-20}" y="32" font-family="monospace" font-size="11" fill="#7ee787" text-anchor="end">● LIVE REPO TELEMETRY</text>

<!-- ================= LEFT PANEL: COMMIT ACTIVITY & VELOCITY (Width: 360) ================= -->
<g transform="translate(20, 48)">
  <rect width="360" height="172" rx="12" fill="#161b26" stroke="#21262d" stroke-width="1.5"/>
  <text x="16" y="24" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="12" font-weight="bold" fill="#c9d1d9">📊 Commit Activity &amp; Velocity</text>
  <text x="344" y="24" font-family="monospace" font-size="11" font-weight="bold" fill="#00D9FF" text-anchor="end">Peak Activity 🚀</text>
  
  <!-- Subtle Grid Lines -->
  <line x1="16" y1="52" x2="344" y2="52" stroke="#21262d" stroke-dasharray="3,3"/>
  <line x1="16" y1="88" x2="344" y2="88" stroke="#21262d" stroke-dasharray="3,3"/>
  <line x1="16" y1="124" x2="344" y2="124" stroke="#21262d" stroke-dasharray="3,3"/>
  <line x1="16" y1="150" x2="344" y2="150" stroke="#30363d"/>
  
  <!-- Filled Area Under Curve -->
  <path d="M 16 150 L 16 125 Q 60 105, 100 78 T 180 98 T 260 42 T 344 32 L 344 150 Z" fill="url(#areaGrad)" class="chart-area"/>
  
  <!-- Animated Bezier Wave Line -->
  <path d="M 16 125 Q 60 105, 100 78 T 180 98 T 260 42 T 344 32" fill="none" stroke="url(#lineGrad)" stroke-width="3.5" class="chart-line"/>
  
  <!-- Glowing Data Point Nodes -->
  <circle cx="100" cy="78" r="4" fill="#00D9FF" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="180" cy="98" r="4" fill="#A78BFA" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="260" cy="42" r="4" fill="#FF0080" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="344" cy="32" r="5" fill="#00D9FF" stroke="#ffffff" stroke-width="2"/>
</g>

<!-- ================= MIDDLE PANEL: CODE QUALITY DONUT (Width: 190) ================= -->
<g transform="translate(395, 48)">
  <rect width="190" height="172" rx="12" fill="#161b26" stroke="#21262d" stroke-width="1.5"/>
  <text x="95" y="24" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="12" font-weight="bold" fill="#c9d1d9" text-anchor="middle">🎯 Code Quality</text>
  
  <!-- Background Donut Ring -->
  <circle cx="95" cy="92" r="44" fill="none" stroke="#21262d" stroke-width="9"/>
  <!-- Animated Gradient Donut Ring -->
  <circle cx="95" cy="92" r="44" fill="none" stroke="url(#donutGrad)" stroke-width="9" stroke-linecap="round" class="donut-ring" transform="rotate(-90 95 92)"/>
  
  <!-- Rating Text -->
  <text x="95" y="87" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="22" font-weight="900" fill="#ffffff" text-anchor="middle">A+</text>
  <text x="95" y="106" font-family="monospace" font-size="11" font-weight="bold" fill="#7ee787" text-anchor="middle">98.4%</text>
  
  <text x="95" y="152" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="11" fill="#8b949e" text-anchor="middle">Production-Grade</text>
</g>

<!-- ================= RIGHT PANEL: ENGINEERING FOCUS BARS (Width: 205) ================= -->
<g transform="translate(600, 48)">
  <rect width="200" height="172" rx="12" fill="#161b26" stroke="#21262d" stroke-width="1.5"/>
  <text x="14" y="24" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="12" font-weight="bold" fill="#c9d1d9">⚡ Engineering Focus</text>
  
  <!-- Bar 1: LLMs & RAG (Max track width: 172) -->
  <text x="14" y="44" font-family="sans-serif" font-size="10" fill="#a5d6ff">LLMs &amp; RAG (45%)</text>
  <rect x="14" y="49" width="172" height="7" rx="3.5" fill="#21262d"/>
  <rect x="14" y="49" height="7" rx="3.5" fill="#00D9FF" class="b1"/>
  
  <!-- Bar 2: Predictive ML -->
  <text x="14" y="73" font-family="sans-serif" font-size="10" fill="#a5d6ff">Predictive ML (30%)</text>
  <rect x="14" y="78" width="172" height="7" rx="3.5" fill="#21262d"/>
  <rect x="14" y="78" height="7" rx="3.5" fill="#A78BFA" class="b2"/>
  
  <!-- Bar 3: FastAPI & React -->
  <text x="14" y="102" font-family="sans-serif" font-size="10" fill="#a5d6ff">FastAPI &amp; React (15%)</text>
  <rect x="14" y="107" width="172" height="7" rx="3.5" fill="#34D399" class="b3"/>
  <rect x="14" y="107" width="172" height="7" rx="3.5" fill="#21262d" opacity="0.0"/>
  
  <!-- Bar 4: MLOps & Cloud -->
  <text x="14" y="131" font-family="sans-serif" font-size="10" fill="#a5d6ff">MLOps &amp; Cloud (10%)</text>
  <rect x="14" y="136" width="172" height="7" rx="3.5" fill="#21262d"/>
  <rect x="14" y="136" height="7" rx="3.5" fill="#FBBF24" class="b4"/>
  
  <text x="100" y="158" font-family="sans-serif" font-size="10" font-weight="bold" fill="#7ee787" text-anchor="middle">500+ Concurrent Users</text>
</g>

</svg>
'''

with open("github_analytics_animated.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Saved aligned github_analytics_animated.svg successfully!")
