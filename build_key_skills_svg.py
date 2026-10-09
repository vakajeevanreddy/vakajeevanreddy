import base64
import os

print("Generating Key Skills Circular & 4-Quadrant Animated SVG...")

def get_b64_svg(icon_name):
    path = f"skill_icons_dir/{icon_name}.svg"
    with open(path, "rb") as f:
        data = f.read()
    return "data:image/svg+xml;base64," + base64.b64encode(data).decode("utf-8")

icons = {
    # (0,0) Data Science & AI/ML
    "ds": ["python", "pytorch", "tensorflow", "sklearn", "pandas", "numpy"],
    # (0,1) Databases & Vector Storage
    "db": ["postgres", "mongodb", "sqlite", "redis", "mysql"],
    # (1,0) Backend & Web APIs
    "api": ["fastapi", "flask", "react", "js", "html"],
    # (1,1) DevOps & Tools
    "dev": ["docker", "git", "githubactions", "aws", "linux", "vscode"]
}

# Pre-encode all icons
icon_b64 = {}
for group, list_names in icons.items():
    for name in list_names:
        icon_b64[name] = get_b64_svg(name)

# SVG Dimensions
W, H = 840, 560
CX, CY = W // 2, H // 2

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<style>
  /* --- KEYFRAME ANIMATIONS --- */
  @keyframes assembleTL {{
    0% {{ transform: translate(-100px, -80px) scale(0.7); opacity: 0; }}
    60% {{ transform: translate(10px, 8px) scale(1.03); opacity: 1; }}
    100% {{ transform: translate(0, 0) scale(1); opacity: 1; }}
  }}
  @keyframes assembleTR {{
    0% {{ transform: translate(100px, -80px) scale(0.7); opacity: 0; }}
    60% {{ transform: translate(-10px, 8px) scale(1.03); opacity: 1; }}
    100% {{ transform: translate(0, 0) scale(1); opacity: 1; }}
  }}
  @keyframes assembleBL {{
    0% {{ transform: translate(-100px, 80px) scale(0.7); opacity: 0; }}
    60% {{ transform: translate(10px, -8px) scale(1.03); opacity: 1; }}
    100% {{ transform: translate(0, 0) scale(1); opacity: 1; }}
  }}
  @keyframes assembleBR {{
    0% {{ transform: translate(100px, 80px) scale(0.7); opacity: 0; }}
    60% {{ transform: translate(-10px, -8px) scale(1.03); opacity: 1; }}
    100% {{ transform: translate(0, 0) scale(1); opacity: 1; }}
  }}
  
  @keyframes spinWheel {{
    0% {{ transform: rotate(0deg); }}
    100% {{ transform: rotate(360deg); }}
  }}
  
  @keyframes pulseCenter {{
    0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 6px rgba(0, 217, 255, 0.4)); }}
    50% {{ transform: scale(1.04); filter: drop-shadow(0 0 16px rgba(0, 217, 255, 0.8)); }}
  }}
  
  @keyframes iconFloat {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-3px); }}
  }}
  
  .card-tl {{ animation: assembleTL 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }}
  .card-tr {{ animation: assembleTR 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }}
  .card-bl {{ animation: assembleBL 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }}
  .card-br {{ animation: assembleBR 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; }}
  
  .wheel-spin {{
    transform-origin: {CX}px {CY}px;
    animation: spinWheel 20s linear infinite;
  }}
  
  .center-hub {{
    transform-origin: {CX}px {CY}px;
    animation: pulseCenter 3s ease-in-out infinite;
  }}
  
  .icon-hover {{
    transition: transform 0.2s ease;
  }}
  .icon-hover:hover {{
    transform: scale(1.15);
  }}
</style>

<linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0d1117"/>
  <stop offset="100%" stop-color="#161b22"/>
</linearGradient>

<linearGradient id="cardGradTL" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#1e2230"/>
  <stop offset="100%" stop-color="#141824"/>
</linearGradient>

<linearGradient id="hubGrad" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#21283b"/>
  <stop offset="100%" stop-color="#131722"/>
</linearGradient>

<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="4" result="blur"/>
  <feComposite in="SourceGraphic" in2="blur" operator="over"/>
</filter>
</defs>

<!-- Main Container Card -->
<rect width="{W}" height="{H}" rx="20" fill="url(#bgGrad)" stroke="#30363d" stroke-width="2"/>

<!-- Decorative Connecting Circuit Lines -->
<path d="M {CX-160} {CY-100} L {CX} {CY} L {CX+160} {CY-100}" stroke="#FF9800" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.3"/>
<path d="M {CX-160} {CY+100} L {CX} {CY} L {CX+160} {CY+100}" stroke="#00BCD4" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.3"/>

<!-- ========================================== -->
<!-- 4 QUADRANT SQUARES (0,0), (0,1), (1,0), (1,1) -->
<!-- ========================================== -->

<!-- (0,0) TOP-LEFT: Data Science & AI/ML -->
<g class="card-tl">
  <rect x="25" y="25" width="260" height="235" rx="16" fill="url(#cardGradTL)" stroke="#FF5722" stroke-width="1.5"/>
  <rect x="25" y="25" width="260" height="34" rx="16" fill="#FF5722" opacity="0.15"/>
  <text x="40" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="13" font-weight="bold" fill="#FF7043">🤖 Data Science &amp; AI/ML</text>
  <text x="260" y="48" font-family="monospace" font-size="11" font-weight="bold" fill="#FFAB91" text-anchor="end">(0,0)</text>
  
  <!-- Icons Grid 3x2 -->
  <g transform="translate(42, 75)">
    <g class="icon-hover"><image href="{icon_b64['python']}" x="0" y="0" width="46" height="46"/><text x="23" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Python</text></g>
    <g class="icon-hover"><image href="{icon_b64['pytorch']}" x="80" y="0" width="46" height="46"/><text x="103" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">PyTorch</text></g>
    <g class="icon-hover"><image href="{icon_b64['tensorflow']}" x="160" y="0" width="46" height="46"/><text x="183" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">TensorFlow</text></g>
    
    <g class="icon-hover"><image href="{icon_b64['sklearn']}" x="0" y="80" width="46" height="46"/><text x="23" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Scikit-Learn</text></g>
    <g class="icon-hover"><image href="{icon_b64['pandas']}" x="80" y="80" width="46" height="46"/><text x="103" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Pandas</text></g>
    <g class="icon-hover"><image href="{icon_b64['numpy']}" x="160" y="80" width="46" height="46"/><text x="183" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">NumPy</text></g>
  </g>
</g>

<!-- (0,1) TOP-RIGHT: Databases & Storage -->
<g class="card-tr">
  <rect x="555" y="25" width="260" height="235" rx="16" fill="url(#cardGradTL)" stroke="#AB47BC" stroke-width="1.5"/>
  <rect x="555" y="25" width="260" height="34" rx="16" fill="#AB47BC" opacity="0.15"/>
  <text x="570" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="13" font-weight="bold" fill="#BA68C8">🗄️ Databases &amp; Storage</text>
  <text x="790" y="48" font-family="monospace" font-size="11" font-weight="bold" fill="#CE93D8" text-anchor="end">(0,1)</text>
  
  <!-- Icons Grid 3x2 -->
  <g transform="translate(572, 75)">
    <g class="icon-hover"><image href="{icon_b64['postgres']}" x="0" y="0" width="46" height="46"/><text x="23" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Postgres</text></g>
    <g class="icon-hover"><image href="{icon_b64['mongodb']}" x="80" y="0" width="46" height="46"/><text x="103" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">MongoDB</text></g>
    <g class="icon-hover"><image href="{icon_b64['sqlite']}" x="160" y="0" width="46" height="46"/><text x="183" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">SQLite</text></g>
    
    <g class="icon-hover"><image href="{icon_b64['redis']}" x="40" y="80" width="46" height="46"/><text x="63" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Redis</text></g>
    <g class="icon-hover"><image href="{icon_b64['mysql']}" x="120" y="80" width="46" height="46"/><text x="143" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">MySQL</text></g>
  </g>
</g>

<!-- (1,0) BOTTOM-LEFT: Backend, Web & APIs -->
<g class="card-bl">
  <rect x="25" y="300" width="260" height="235" rx="16" fill="url(#cardGradTL)" stroke="#00BCD4" stroke-width="1.5"/>
  <rect x="25" y="300" width="260" height="34" rx="16" fill="#00BCD4" opacity="0.15"/>
  <text x="40" y="323" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="13" font-weight="bold" fill="#4DD0E1">🌐 Backend, Web &amp; APIs</text>
  <text x="260" y="323" font-family="monospace" font-size="11" font-weight="bold" fill="#80DEEA" text-anchor="end">(1,0)</text>
  
  <!-- Icons Grid 3x2 -->
  <g transform="translate(42, 350)">
    <g class="icon-hover"><image href="{icon_b64['fastapi']}" x="0" y="0" width="46" height="46"/><text x="23" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">FastAPI</text></g>
    <g class="icon-hover"><image href="{icon_b64['flask']}" x="80" y="0" width="46" height="46"/><text x="103" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Flask</text></g>
    <g class="icon-hover"><image href="{icon_b64['react']}" x="160" y="0" width="46" height="46"/><text x="183" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">React</text></g>
    
    <g class="icon-hover"><image href="{icon_b64['js']}" x="40" y="80" width="46" height="46"/><text x="63" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">JavaScript</text></g>
    <g class="icon-hover"><image href="{icon_b64['html']}" x="120" y="80" width="46" height="46"/><text x="143" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">HTML5</text></g>
  </g>
</g>

<!-- (1,1) BOTTOM-RIGHT: DevOps, Cloud & Tools -->
<g class="card-br">
  <rect x="555" y="300" width="260" height="235" rx="16" fill="url(#cardGradTL)" stroke="#29B6F6" stroke-width="1.5"/>
  <rect x="555" y="300" width="260" height="34" rx="16" fill="#29B6F6" opacity="0.15"/>
  <text x="570" y="323" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="13" font-weight="bold" fill="#81D4FA">☁️ DevOps, Cloud &amp; Tools</text>
  <text x="790" y="323" font-family="monospace" font-size="11" font-weight="bold" fill="#B3E5FC" text-anchor="end">(1,1)</text>
  
  <!-- Icons Grid 3x2 -->
  <g transform="translate(572, 350)">
    <g class="icon-hover"><image href="{icon_b64['docker']}" x="0" y="0" width="46" height="46"/><text x="23" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Docker</text></g>
    <g class="icon-hover"><image href="{icon_b64['git']}" x="80" y="0" width="46" height="46"/><text x="103" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Git</text></g>
    <g class="icon-hover"><image href="{icon_b64['githubactions']}" x="160" y="0" width="46" height="46"/><text x="183" y="60" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Actions</text></g>
    
    <g class="icon-hover"><image href="{icon_b64['aws']}" x="0" y="80" width="46" height="46"/><text x="23" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">AWS</text></g>
    <g class="icon-hover"><image href="{icon_b64['linux']}" x="80" y="80" width="46" height="46"/><text x="103" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">Linux</text></g>
    <g class="icon-hover"><image href="{icon_b64['vscode']}" x="160" y="80" width="46" height="46"/><text x="183" y="140" font-family="sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">VS Code</text></g>
  </g>
</g>

<!-- ========================================== -->
<!-- CENTER CIRCULAR PINWHEEL APERTURE (KEY SKILLS) -->
<!-- ========================================== -->

<!-- Rotating Pinwheel Spiral Blades -->
<g class="wheel-spin">
  <!-- 8 Overlapping Colorful Spiral Petals/Blades -->
  <!-- Blade 1: Orange -->
  <path d="M {CX} {CY} C {CX+45} {CY-85} {CX+95} {CY-45} {CX+85} {CY} Z" fill="#FF5722" opacity="0.9"/>
  <!-- Blade 2: Amber -->
  <path d="M {CX} {CY} C {CX+85} {CY-45} {CX+95} {CY+45} {CX+60} {CY+65} Z" fill="#FF9800" opacity="0.9"/>
  <!-- Blade 3: Yellow -->
  <path d="M {CX} {CY} C {CX+95} {CY+45} {CX+45} {CY+95} {CX} {CY+85} Z" fill="#FFC107" opacity="0.9"/>
  <!-- Blade 4: Lime/Green -->
  <path d="M {CX} {CY} C {CX+45} {CY+95} {CX-45} {CY+95} {CX-65} {CY+60} Z" fill="#8BC34A" opacity="0.9"/>
  <!-- Blade 5: Emerald/Cyan -->
  <path d="M {CX} {CY} C {CX-45} {CY+95} {CX-95} {CY+45} {CX-85} {CY} Z" fill="#00BCD4" opacity="0.9"/>
  <!-- Blade 6: Blue -->
  <path d="M {CX} {CY} C {CX-95} {CY+45} {CX-95} {CY-45} {CX-60} {CY-65} Z" fill="#2196F3" opacity="0.9"/>
  <!-- Blade 7: Purple -->
  <path d="M {CX} {CY} C {CX-95} {CY-45} {CX-45} {CY-95} {CX} {CY-85} Z" fill="#9C27B0" opacity="0.9"/>
  <!-- Blade 8: Pink -->
  <path d="M {CX} {CY} C {CX-45} {CY-95} {CX+45} {CY-95} {CX+65} {CY-60} Z" fill="#E91E63" opacity="0.9"/>
</g>

<!-- Central Circular Hub -->
<g class="center-hub">
  <circle cx="{CX}" cy="{CY}" r="64" fill="url(#hubGrad)" stroke="#00D9FF" stroke-width="3" filter="url(#glow)"/>
  <circle cx="{CX}" cy="{CY}" r="56" fill="#161b26" stroke="#30363d" stroke-width="1.5"/>
  
  <!-- Central Text -->
  <text x="{CX}" y="{CY-8}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="14" font-weight="900" fill="#00D9FF" text-anchor="middle" letter-spacing="2">KEY</text>
  <text x="{CX}" y="{CY+14}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="2">SKILLS</text>
  <circle cx="{CX}" cy="{CY+26}" r="3" fill="#00D9FF"/>
</g>

</svg>
'''

with open("key_skills_wheel.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Saved key_skills_wheel.svg successfully!")
