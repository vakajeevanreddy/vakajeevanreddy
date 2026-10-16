import os
import xml.etree.ElementTree as ET

os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")
os.makedirs("assets/projects", exist_ok=True)

def verify_and_save(filename, svg_code):
    path = os.path.join("assets/projects", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_code)
    try:
        ET.parse(path)
        print(f"VERIFIED VALID XML: {filename} ({len(svg_code)} bytes)")
    except Exception as e:
        print(f"FAILED XML in {filename}: {e}")
        raise

# ==============================================================================
# 1. AIVOA-CRM-HCP (Animated ECG Pulse + Radar Beacon + Shimmer Border)
# ==============================================================================
svg_1 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="160" viewBox="0 0 480 160">
  <defs>
    <style>
      @keyframes pulseGlow {
        0%, 100% { opacity: 0.6; filter: drop-shadow(0 0 2px #10B981); }
        50% { opacity: 1; filter: drop-shadow(0 0 8px #34D399); }
      }
      @keyframes ecgMove {
        0% { stroke-dashoffset: 600; }
        100% { stroke-dashoffset: 0; }
      }
      @keyframes radarPing {
        0% { r: 3px; opacity: 1; }
        100% { r: 10px; opacity: 0; }
      }
      .ecg-anim {
        stroke-dasharray: 200, 400;
        animation: ecgMove 3s linear infinite;
      }
      .badge-glow { animation: pulseGlow 2.5s ease-in-out infinite; }
    </style>
    <linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#06121E"/>
      <stop offset="50%" stop-color="#06251F"/>
      <stop offset="100%" stop-color="#021414"/>
    </linearGradient>
    <linearGradient id="ecgGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#34D399"/>
      <stop offset="100%" stop-color="#00D9FF"/>
    </linearGradient>
    <filter id="glowGreen" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Container Box -->
  <rect width="480" height="160" rx="14" fill="url(#bg1)" stroke="#059669" stroke-width="1.5"/>

  <!-- Top System Bar -->
  <rect x="0" y="0" width="480" height="28" rx="14" fill="#041E1A"/>
  <rect x="0" y="14" width="480" height="14" fill="#041E1A"/>
  <line x1="0" y1="28" x2="480" y2="28" stroke="#065F46" stroke-width="1"/>

  <text x="18" y="18" font-family="monospace" font-size="10" font-weight="700" fill="#34D399" letter-spacing="1.5">HEALTHCARE AI // ENTERPRISE CRM</text>
  
  <!-- Live Radar Indicator -->
  <g transform="translate(415, 14)">
    <circle cx="0" cy="0" r="3" fill="#10B981"/>
    <circle cx="0" cy="0" r="3" fill="none" stroke="#34D399" stroke-width="1.5">
      <animate attributeName="r" values="3;10" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0" dur="1.8s" repeatCount="indefinite"/>
    </circle>
    <text x="12" y="3.5" font-family="monospace" font-size="9" font-weight="700" fill="#34D399">ONLINE</text>
  </g>

  <!-- Grid Guide Lines -->
  <line x1="20" y1="65" x2="460" y2="65" stroke="#064E3B" stroke-width="0.7" stroke-dasharray="3,3"/>
  <line x1="20" y1="95" x2="460" y2="95" stroke="#064E3B" stroke-width="0.7" stroke-dasharray="3,3"/>

  <!-- Animated ECG Line -->
  <path d="M 20 80 L 120 80 L 135 55 L 145 105 L 155 40 L 168 115 L 178 70 L 188 88 L 198 80 L 320 80 L 330 60 L 340 100 L 350 80 L 460 80" 
        fill="none" stroke="url(#ecgGrad)" stroke-width="2.5" class="ecg-anim" filter="url(#glowGreen)"/>

  <!-- Icon + Main Title Block -->
  <g transform="translate(20, 38)">
    <circle cx="18" cy="18" r="16" fill="#064E3B" stroke="#10B981" stroke-width="1.5"/>
    <rect x="15" y="8" width="6" height="20" rx="1.5" fill="#34D399"/>
    <rect x="8" y="15" width="20" height="6" rx="1.5" fill="#34D399"/>

    <text x="44" y="15" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="900" fill="#FFFFFF" letter-spacing="0.3">AIVOA-CRM-HCP</text>
    <text x="44" y="30" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#6EE7B7">AI Documentation &amp; HCP Interaction Platform</text>
  </g>

  <!-- Animated Interactive Metric Badges -->
  <g transform="translate(20, 122)">
    <!-- Badge 1 -->
    <rect x="0" y="0" width="135" height="24" rx="6" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <circle cx="12" cy="12" r="3.5" fill="#34D399">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="22" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#A7F3D0">40-70% Automation</text>

    <!-- Badge 2 -->
    <rect x="145" y="0" width="130" height="24" rx="6" fill="#083344" stroke="#0891B2" stroke-width="1"/>
    <text x="155" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#67E8F9">🏥 500+ Active Users</text>

    <!-- Badge 3 -->
    <rect x="285" y="0" width="105" height="24" rx="6" fill="#1E1B4B" stroke="#4F46E5" stroke-width="1"/>
    <text x="295" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#C7D2FE">⚡ FastAPI Backend</text>

    <!-- Badge 4 -->
    <rect x="400" y="0" width="60" height="24" rx="6" fill="#1E293B" stroke="#475569" stroke-width="1"/>
    <text x="410" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#93C5FD">React</text>
  </g>
</svg>'''

# ==============================================================================
# 2. Customer Health Care CRM App (Animated Equalizer Bars + Glowing Clusters)
# ==============================================================================
svg_2 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="160" viewBox="0 0 480 160">
  <defs>
    <style>
      @keyframes eq1 { 0%, 100% { height: 18px; y: 72px; } 50% { height: 42px; y: 48px; } }
      @keyframes eq2 { 0%, 100% { height: 38px; y: 52px; } 50% { height: 20px; y: 70px; } }
      @keyframes eq3 { 0%, 100% { height: 28px; y: 62px; } 50% { height: 48px; y: 42px; } }
      @keyframes eq4 { 0%, 100% { height: 44px; y: 46px; } 50% { height: 22px; y: 68px; } }
      @keyframes clusterPulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.15); opacity: 1; }
      }
      .b-anim1 { animation: eq1 1.6s ease-in-out infinite; }
      .b-anim2 { animation: eq2 2.1s ease-in-out infinite; }
      .b-anim3 { animation: eq3 1.8s ease-in-out infinite; }
      .b-anim4 { animation: eq4 2.4s ease-in-out infinite; }
    </style>
    <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1E0E2B"/>
      <stop offset="50%" stop-color="#2D0B38"/>
      <stop offset="100%" stop-color="#0E071A"/>
    </linearGradient>
    <linearGradient id="purpleBar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F472B6"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <filter id="glowPurple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="160" rx="14" fill="url(#bg2)" stroke="#A855F7" stroke-width="1.5"/>

  <!-- Top System Bar -->
  <rect x="0" y="0" width="480" height="28" rx="14" fill="#1C052A"/>
  <rect x="0" y="14" width="480" height="14" fill="#1C052A"/>
  <line x1="0" y1="28" x2="480" y2="28" stroke="#581C87" stroke-width="1"/>

  <text x="18" y="18" font-family="monospace" font-size="10" font-weight="700" fill="#D8B4FE" letter-spacing="1.5">PREDICTIVE ANALYTICS // DECISION SUPPORT</text>

  <rect x="375" y="6" width="90" height="16" rx="8" fill="#3B0764" stroke="#7C3AED" stroke-width="1"/>
  <text x="420" y="17.5" font-family="monospace" font-size="8.5" font-weight="bold" fill="#F0ABFC" text-anchor="middle">ML PIPELINE</text>

  <!-- Title & Icon Block -->
  <g transform="translate(20, 38)">
    <circle cx="18" cy="18" r="16" fill="#3B0764" stroke="#C084FC" stroke-width="1.5"/>
    <text x="18" y="24" font-size="16" text-anchor="middle">🧠</text>

    <text x="44" y="15" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">Customer Health Care CRM</text>
    <text x="44" y="30" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#F472B6">End-to-End Patient Analytics &amp; Risk Scoring</text>
  </g>

  <!-- Animated Live Bar Visualizer (Right) -->
  <g transform="translate(350, 0)">
    <rect x="0" y="48" width="10" height="42" rx="3" fill="url(#purpleBar)" class="b-anim1"/>
    <rect x="16" y="52" width="10" height="38" rx="3" fill="url(#purpleBar)" class="b-anim2"/>
    <rect x="32" y="62" width="10" height="28" rx="3" fill="url(#purpleBar)" class="b-anim3"/>
    <rect x="48" y="46" width="10" height="44" rx="3" fill="url(#purpleBar)" class="b-anim4"/>
    <rect x="64" y="56" width="10" height="34" rx="3" fill="url(#purpleBar)" class="b-anim2"/>
    <rect x="80" y="44" width="10" height="46" rx="3" fill="url(#purpleBar)" class="b-anim1"/>
    <line x1="-5" y1="94" x2="98" y2="94" stroke="#581C87" stroke-width="1"/>
  </g>

  <!-- Pulsing Cluster Dots (Center) -->
  <g transform="translate(190, 72)">
    <circle cx="15" cy="5" r="4.5" fill="#38BDF8">
      <animate attributeName="r" values="3.5;5.5;3.5" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="35" cy="18" r="4" fill="#38BDF8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="1.7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="55" cy="8" r="5" fill="#F472B6">
      <animate attributeName="r" values="4;6;4" dur="2.3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="75" cy="22" r="4" fill="#F472B6"/>
    <circle cx="95" cy="12" r="5" fill="#A855F7">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
    </circle>
    <!-- Decision boundary wave -->
    <path d="M 0 25 Q 40 5 80 20 T 140 10" fill="none" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.7"/>
  </g>

  <!-- Metric Badges -->
  <g transform="translate(20, 122)">
    <rect x="0" y="0" width="130" height="24" rx="6" fill="#4A044E" stroke="#C026D3" stroke-width="1"/>
    <text x="65" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#F5D0FE" text-anchor="middle">🎯 +30% Accuracy</text>

    <rect x="140" y="0" width="120" height="24" rx="6" fill="#2E1065" stroke="#7C3AED" stroke-width="1"/>
    <text x="200" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#DDD6FE" text-anchor="middle">🤖 Scikit-Learn</text>

    <rect x="270" y="0" width="95" height="24" rx="6" fill="#1E293B" stroke="#64748B" stroke-width="1"/>
    <text x="317" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#E2E8F0" text-anchor="middle">📊 Pandas</text>

    <rect x="375" y="0" width="85" height="24" rx="6" fill="#1E1B4B" stroke="#4F46E5" stroke-width="1"/>
    <text x="417" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#C7D2FE" text-anchor="middle">Jupyter</text>
  </g>
</svg>'''

# ==============================================================================
# 3. SkC Jeevan Tutor (Animated Code Editor + Blinking Terminal Cursor)
# ==============================================================================
svg_3 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="160" viewBox="0 0 480 160">
  <defs>
    <style>
      @keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
      @keyframes progFill { 0% { width: 0; } 100% { width: 140px; } }
      .cursor-blink { animation: blink 0.9s infinite; }
      .progress-bar-anim { animation: progFill 2.2s cubic-bezier(0.25, 1, 0.5, 1) forwards; }
    </style>
    <linearGradient id="bg3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0B132B"/>
      <stop offset="50%" stop-color="#1C2541"/>
      <stop offset="100%" stop-color="#0B132B"/>
    </linearGradient>
    <linearGradient id="progGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>

  <rect width="480" height="160" rx="14" fill="url(#bg3)" stroke="#38BDF8" stroke-width="1.5"/>

  <!-- Top System Bar -->
  <rect x="0" y="0" width="480" height="28" rx="14" fill="#0A1128"/>
  <rect x="0" y="14" width="480" height="14" fill="#0A1128"/>
  <line x1="0" y1="28" x2="480" y2="28" stroke="#1E3A8A" stroke-width="1"/>

  <text x="18" y="18" font-family="monospace" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.5">INTERACTIVE EDTECH // CODING ENVIRONMENT</text>

  <rect x="365" y="6" width="100" height="16" rx="8" fill="#082F49" stroke="#0284C7" stroke-width="1"/>
  <text x="415" y="17.5" font-family="monospace" font-size="8.5" font-weight="bold" fill="#7DD3FC" text-anchor="middle">LIVE PLATFORM</text>

  <!-- Title & Icon Block -->
  <g transform="translate(20, 38)">
    <circle cx="18" cy="18" r="16" fill="#0C4A6E" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="18" y="24" font-size="16" text-anchor="middle">📚</text>

    <text x="44" y="15" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">SkC Jeevan Tutor</text>
    <text x="44" y="30" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#38BDF8">Interactive Web-Based Python Learning Engine</text>
  </g>

  <!-- Animated Interactive Mini IDE Window (Right) -->
  <g transform="translate(230, 40)">
    <rect width="230" height="70" rx="6" fill="#060913" stroke="#1E293B" stroke-width="1"/>
    <!-- Window buttons -->
    <circle cx="10" cy="10" r="3" fill="#EF4444"/>
    <circle cx="18" cy="10" r="3" fill="#F59E0B"/>
    <circle cx="26" cy="10" r="3" fill="#10B981"/>
    <text x="40" y="13" font-family="monospace" font-size="7.5" fill="#64748B">tutorial_lab.py</text>
    <line x1="0" y1="18" x2="230" y2="18" stroke="#1E293B" stroke-width="0.8"/>
    <!-- Code line with syntax coloring -->
    <text x="10" y="33" font-family="monospace" font-size="8.5" fill="#F472B6">def <tspan fill="#38BDF8">start_coding</tspan>():</text>
    <text x="20" y="47" font-family="monospace" font-size="8.5" fill="#94A3B8">track = <tspan fill="#FDE047">"Python 3"</tspan></text>
    <text x="20" y="60" font-family="monospace" font-size="8.5" fill="#F472B6">return <tspan fill="#34D399">"Success!"</tspan></text>
    <!-- Blinking cursor -->
    <rect x="126" y="52" width="5" height="10" fill="#38BDF8" class="cursor-blink"/>
  </g>

  <!-- Progress bar tracker (Left side) -->
  <g transform="translate(20, 92)">
    <text x="0" y="0" font-family="monospace" font-size="8.5" font-weight="bold" fill="#94A3B8">Curriculum Progress: 85%</text>
    <rect x="0" y="6" width="180" height="7" rx="3.5" fill="#1E293B"/>
    <rect x="0" y="6" width="153" height="7" rx="3.5" fill="url(#progGrad)" class="progress-bar-anim"/>
  </g>

  <!-- Tech Badges -->
  <g transform="translate(20, 122)">
    <rect x="0" y="0" width="120" height="24" rx="6" fill="#1E3A8A" stroke="#2563EB" stroke-width="1"/>
    <text x="60" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#93C5FD" text-anchor="middle">🐍 Python 3.x</text>

    <rect x="130" y="0" width="105" height="24" rx="6" fill="#431407" stroke="#EA580C" stroke-width="1"/>
    <text x="182" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#FDBA74" text-anchor="middle">HTML5 / CSS3</text>

    <rect x="245" y="0" width="110" height="24" rx="6" fill="#422006" stroke="#CA8A04" stroke-width="1"/>
    <text x="300" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#FDE047" text-anchor="middle">⚡ JavaScript</text>

    <rect x="365" y="0" width="95" height="24" rx="6" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <text x="412" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#6EE7B7" text-anchor="middle">Live REPL</text>
  </g>
</svg>'''

# ==============================================================================
# 4. California House Price Prediction (Animated Regression Fit Curve)
# ==============================================================================
svg_4 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="160" viewBox="0 0 480 160">
  <defs>
    <style>
      @keyframes lineDraw {
        0% { stroke-dashoffset: 300; }
        100% { stroke-dashoffset: 0; }
      }
      @keyframes dotPop {
        0%, 100% { transform: scale(1); opacity: 0.7; }
        50% { transform: scale(1.3); opacity: 1; }
      }
      .reg-line-anim {
        stroke-dasharray: 300;
        animation: lineDraw 3s ease-out infinite;
      }
    </style>
    <linearGradient id="bg4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1C140E"/>
      <stop offset="50%" stop-color="#26170D"/>
      <stop offset="100%" stop-color="#0E0A07"/>
    </linearGradient>
    <linearGradient id="regGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#EF4444"/>
    </linearGradient>
    <filter id="glowOrange" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="160" rx="14" fill="url(#bg4)" stroke="#F59E0B" stroke-width="1.5"/>

  <!-- Top System Bar -->
  <rect x="0" y="0" width="480" height="28" rx="14" fill="#1C0E06"/>
  <rect x="0" y="14" width="480" height="14" fill="#1C0E06"/>
  <line x1="0" y1="28" x2="480" y2="28" stroke="#78350F" stroke-width="1"/>

  <text x="18" y="18" font-family="monospace" font-size="10" font-weight="700" fill="#FBBF24" letter-spacing="1.5">SUPERVISED LEARNING // REGRESSION MODEL</text>

  <rect x="365" y="6" width="100" height="16" rx="8" fill="#451A03" stroke="#D97706" stroke-width="1"/>
  <text x="415" y="17.5" font-family="monospace" font-size="8.5" font-weight="bold" fill="#FDE68A" text-anchor="middle">R² SCORE: 0.86</text>

  <!-- Title & Icon Block -->
  <g transform="translate(20, 38)">
    <circle cx="18" cy="18" r="16" fill="#451A03" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="18" y="24" font-size="16" text-anchor="middle">🏠</text>

    <text x="44" y="15" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">California House Price Pred</text>
    <text x="44" y="30" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#FBBF24">Advanced Regression &amp; Geospatial Feature Engineering</text>
  </g>

  <!-- Animated Interactive Regression Coordinate Chart (Right) -->
  <g transform="translate(270, 38)">
    <rect width="190" height="74" rx="6" fill="#120B06" stroke="#442813" stroke-width="1"/>
    <!-- Axes -->
    <line x1="20" y1="60" x2="180" y2="60" stroke="#78350F" stroke-width="1"/>
    <line x1="20" y1="12" x2="20" y2="60" stroke="#78350F" stroke-width="1"/>
    
    <!-- Data points with animation -->
    <circle cx="35" cy="52" r="3" fill="#FDE68A" opacity="0.6"/>
    <circle cx="55" cy="46" r="3" fill="#FDE68A" opacity="0.8"/>
    <circle cx="75" cy="42" r="3.5" fill="#FDE68A"/>
    <circle cx="95" cy="35" r="3" fill="#FDE68A" opacity="0.7"/>
    <circle cx="115" cy="30" r="3.5" fill="#FDE68A"/>
    <circle cx="135" cy="22" r="3" fill="#FDE68A" opacity="0.8"/>
    <circle cx="155" cy="18" r="4" fill="#FDE68A">
      <animate attributeName="r" values="3;5;3" dur="1.5s" repeatCount="indefinite"/>
    </circle>

    <!-- Animated Regression Best Fit Line -->
    <line x1="22" y1="58" x2="175" y2="15" stroke="url(#regGrad)" stroke-width="2.5" class="reg-line-anim" filter="url(#glowOrange)"/>
  </g>

  <!-- Tags -->
  <g transform="translate(20, 122)">
    <rect x="0" y="0" width="125" height="24" rx="6" fill="#451A03" stroke="#D97706" stroke-width="1"/>
    <text x="62" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#FDE68A" text-anchor="middle">📈 Random Forest</text>

    <rect x="135" y="0" width="125" height="24" rx="6" fill="#3B0764" stroke="#7E22CE" stroke-width="1"/>
    <text x="197" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#E9D5FF" text-anchor="middle">🗺️ Geo Valuation</text>

    <rect x="270" y="0" width="105" height="24" rx="6" fill="#1C1917" stroke="#78716C" stroke-width="1"/>
    <text x="322" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#F5F5F4" text-anchor="middle">Scikit-Learn</text>

    <rect x="385" y="0" width="75" height="24" rx="6" fill="#0C4A6E" stroke="#0284C7" stroke-width="1"/>
    <text x="422" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#BAE6FD" text-anchor="middle">Matplotlib</text>
  </g>
</svg>'''

# ==============================================================================
# 5. Deep Learning Projects (Animated Synapse Neural Transmission)
# ==============================================================================
svg_5 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="160" viewBox="0 0 480 160">
  <defs>
    <style>
      @keyframes synPulse1 { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
      @keyframes nodeFwd {
        0% { fill: #38BDF8; }
        33% { fill: #F472B6; }
        66% { fill: #A855F7; }
        100% { fill: #38BDF8; }
      }
      .syn-anim { animation: synPulse1 2s ease-in-out infinite; }
      .node-anim { animation: nodeFwd 3s ease-in-out infinite; }
    </style>
    <linearGradient id="bg5" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#160826"/>
      <stop offset="50%" stop-color="#1B0A2E"/>
      <stop offset="100%" stop-color="#0A0413"/>
    </linearGradient>
    <filter id="glowPink" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="160" rx="14" fill="url(#bg5)" stroke="#EC4899" stroke-width="1.5"/>

  <!-- Top System Bar -->
  <rect x="0" y="0" width="480" height="28" rx="14" fill="#150624"/>
  <rect x="0" y="14" width="480" height="14" fill="#150624"/>
  <line x1="0" y1="28" x2="480" y2="28" stroke="#701A75" stroke-width="1"/>

  <text x="18" y="18" font-family="monospace" font-size="10" font-weight="700" fill="#F472B6" letter-spacing="1.5">DEEP LEARNING // NEURAL NETWORKS &amp; VISION</text>

  <rect x="365" y="6" width="100" height="16" rx="8" fill="#500724" stroke="#DB2777" stroke-width="1"/>
  <text x="415" y="17.5" font-family="monospace" font-size="8.5" font-weight="bold" fill="#FBCFE8" text-anchor="middle">PYTORCH / TF</text>

  <!-- Title & Icon Block -->
  <g transform="translate(20, 38)">
    <circle cx="18" cy="18" r="16" fill="#500724" stroke="#F472B6" stroke-width="1.5"/>
    <text x="18" y="24" font-size="16" text-anchor="middle">🤖</text>

    <text x="44" y="15" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">Deep Learning Projects</text>
    <text x="44" y="30" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#F472B6">CNNs, RNNs, Vision Models &amp; Attention Blocks</text>
  </g>

  <!-- Animated Neural Network Architecture Diagram (Right) -->
  <g transform="translate(260, 38)">
    <!-- Layer 1 -> Layer 2 Synapses -->
    <line x1="20" y1="18" x2="70" y2="12" stroke="#831843" stroke-width="1.2"/>
    <line x1="20" y1="18" x2="70" y2="36" stroke="#EC4899" stroke-width="1.5" class="syn-anim"/>
    <line x1="20" y1="18" x2="70" y2="60" stroke="#831843" stroke-width="1.2"/>
    <line x1="20" y1="52" x2="70" y2="12" stroke="#831843" stroke-width="1.2"/>
    <line x1="20" y1="52" x2="70" y2="36" stroke="#EC4899" stroke-width="1.5" class="syn-anim"/>
    <line x1="20" y1="52" x2="70" y2="60" stroke="#831843" stroke-width="1.2"/>
    
    <!-- Layer 2 -> Layer 3 Synapses -->
    <line x1="70" y1="12" x2="120" y2="22" stroke="#A855F7" stroke-width="1.5" class="syn-anim"/>
    <line x1="70" y1="36" x2="120" y2="22" stroke="#F472B6" stroke-width="1.8" class="syn-anim"/>
    <line x1="70" y1="60" x2="120" y2="48" stroke="#A855F7" stroke-width="1.5" class="syn-anim"/>
    
    <!-- Layer 3 -> Output Synapses -->
    <line x1="120" y1="22" x2="170" y2="36" stroke="#34D399" stroke-width="2" class="syn-anim"/>
    <line x1="120" y1="48" x2="170" y2="36" stroke="#34D399" stroke-width="1.5" class="syn-anim"/>

    <!-- Layer 1 Nodes (Input) -->
    <circle cx="20" cy="18" r="5" fill="#38BDF8"/>
    <circle cx="20" cy="52" r="5" fill="#38BDF8"/>

    <!-- Layer 2 Nodes (Hidden 1) with pulse -->
    <circle cx="70" cy="12" r="5" fill="#A855F7"/>
    <circle cx="70" cy="36" r="6" fill="#F472B6" filter="url(#glowPink)">
      <animate attributeName="r" values="5;7;5" dur="1.4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="70" cy="60" r="5" fill="#A855F7"/>

    <!-- Layer 3 Nodes (Hidden 2) -->
    <circle cx="120" cy="22" r="6" fill="#F472B6" filter="url(#glowPink)">
      <animate attributeName="r" values="5;7;5" dur="1.7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="120" cy="48" r="5" fill="#EC4899"/>

    <!-- Output Layer Node -->
    <circle cx="170" cy="36" r="7.5" fill="#10B981" filter="url(#glowPink)">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="1.2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Tags -->
  <g transform="translate(20, 122)">
    <rect x="0" y="0" width="115" height="24" rx="6" fill="#431407" stroke="#EA580C" stroke-width="1"/>
    <text x="57" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#FDBA74" text-anchor="middle">🔥 PyTorch</text>

    <rect x="123" y="0" width="125" height="24" rx="6" fill="#451A03" stroke="#D97706" stroke-width="1"/>
    <text x="185" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#FDE68A" text-anchor="middle">⚡ TensorFlow</text>

    <rect x="256" y="0" width="115" height="24" rx="6" fill="#3B0764" stroke="#7E22CE" stroke-width="1"/>
    <text x="313" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#E9D5FF" text-anchor="middle">🧠 CNN &amp; NLP</text>

    <rect x="380" y="0" width="80" height="24" rx="6" fill="#1E293B" stroke="#475569" stroke-width="1"/>
    <text x="420" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#94A3B8" text-anchor="middle">Jupyter</text>
  </g>
</svg>'''

# ==============================================================================
# 6. Deep-ML Practice (Animated Gradient Descent Scan Line + Math Matrix)
# ==============================================================================
svg_6 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="160" viewBox="0 0 480 160">
  <defs>
    <style>
      @keyframes scanSweep {
        0% { transform: translateY(0); opacity: 0.2; }
        50% { opacity: 0.8; }
        100% { transform: translateY(58px); opacity: 0.2; }
      }
      @keyframes formulaGlow {
        0%, 100% { fill: #38BDF8; }
        50% { fill: #4ADE80; }
      }
      .scanner-line { animation: scanSweep 2.5s ease-in-out infinite; }
      .formula-text { animation: formulaGlow 3s ease-in-out infinite; }
    </style>
    <linearGradient id="bg6" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#021E36"/>
      <stop offset="50%" stop-color="#082F49"/>
      <stop offset="100%" stop-color="#051527"/>
    </linearGradient>
    <filter id="glowBlue" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="160" rx="14" fill="url(#bg6)" stroke="#0284C7" stroke-width="1.5"/>

  <!-- Top System Bar -->
  <rect x="0" y="0" width="480" height="28" rx="14" fill="#031A2F"/>
  <rect x="0" y="14" width="480" height="14" fill="#031A2F"/>
  <line x1="0" y1="28" x2="480" y2="28" stroke="#075985" stroke-width="1"/>

  <text x="18" y="18" font-family="monospace" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.5">ALGORITHMIC FOUNDATIONS // PURE NUMPY</text>

  <rect x="365" y="6" width="100" height="16" rx="8" fill="#082F49" stroke="#0284C7" stroke-width="1"/>
  <text x="415" y="17.5" font-family="monospace" font-size="8.5" font-weight="bold" fill="#BAE6FD" text-anchor="middle">FROM SCRATCH</text>

  <!-- Title & Icon Block -->
  <g transform="translate(20, 38)">
    <circle cx="18" cy="18" r="16" fill="#0C4A6E" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="18" y="23" font-size="16" text-anchor="middle" fill="#BAE6FD" font-weight="bold">∑</text>

    <text x="44" y="15" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="900" fill="#FFFFFF">Deep-ML Practice</text>
    <text x="44" y="30" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#38BDF8">Mathematical Derivations &amp; Vectorized ML Algorithms</text>
  </g>

  <!-- Interactive Terminal Matrix Board (Right) -->
  <g transform="translate(270, 38)">
    <rect width="190" height="74" rx="6" fill="#031422" stroke="#0369A1" stroke-width="1"/>
    
    <!-- Gradient Descent formula -->
    <text x="14" y="24" font-family="Georgia,serif" font-size="12" font-style="italic" class="formula-text">W := W - α · ∇L(W)</text>
    <line x1="14" y1="32" x2="175" y2="32" stroke="#075985" stroke-width="0.8"/>
    
    <!-- Matrix Ops -->
    <text x="14" y="47" font-family="monospace" font-size="9" fill="#7DD3FC">Z = np.dot(X, W) + b</text>
    <text x="14" y="62" font-family="monospace" font-size="8.5" fill="#4ADE80">Backprop: dW = (1/m)(Xᵀ·dZ)</text>

    <!-- Scanning beam line -->
    <line x1="8" y1="10" x2="182" y2="10" stroke="#38BDF8" stroke-width="1.5" class="scanner-line"/>
  </g>

  <!-- Tags -->
  <g transform="translate(20, 122)">
    <rect x="0" y="0" width="125" height="24" rx="6" fill="#0C4A6E" stroke="#0284C7" stroke-width="1"/>
    <text x="62" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#BAE6FD" text-anchor="middle">📐 Vectorized NumPy</text>

    <rect x="135" y="0" width="135" height="24" rx="6" fill="#14532D" stroke="#16A34A" stroke-width="1"/>
    <text x="202" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#BBF7D0" text-anchor="middle">⚡ Zero Frameworks</text>

    <rect x="280" y="0" width="105" height="24" rx="6" fill="#1E1B4B" stroke="#4338CA" stroke-width="1"/>
    <text x="332" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#C7D2FE" text-anchor="middle">🎓 Math Proofs</text>

    <rect x="395" y="0" width="65" height="24" rx="6" fill="#1E293B" stroke="#475569" stroke-width="1"/>
    <text x="427" y="16" font-family="monospace" font-size="9.5" font-weight="700" fill="#94A3B8" text-anchor="middle">Python</text>
  </g>
</svg>'''

verify_and_save("aivoa_crm.svg", svg_1)
verify_and_save("customer_healthcare.svg", svg_2)
verify_and_save("skc_tutor.svg", svg_3)
verify_and_save("california_housing.svg", svg_4)
verify_and_save("deep_learning.svg", svg_5)
verify_and_save("deep_ml.svg", svg_6)

print("SUCCESS: All 6 animated and structured project SVGs built and verified!")
