import os
import xml.etree.ElementTree as ET

os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")
os.makedirs("assets/projects", exist_ok=True)

def save_and_verify(filename, svg_content):
    path = os.path.join("assets/projects", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    try:
        ET.parse(path)
        print(f"VALID XML: {filename} ({len(svg_content)} bytes)")
    except Exception as e:
        print(f"ERROR in {filename}: {e}")
        raise

# ==============================================================================
# 1. AIVOA-CRM-HCP (Healthcare CRM + AI)
# ==============================================================================
svg_1 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="150" viewBox="0 0 480 150">
  <defs>
    <linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="60%" stop-color="#022C22"/>
      <stop offset="100%" stop-color="#04151F"/>
    </linearGradient>
    <linearGradient id="lineG1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#34D399"/>
      <stop offset="100%" stop-color="#06B6D4"/>
    </linearGradient>
    <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="150" rx="12" fill="url(#bg1)" stroke="#059669" stroke-width="1.5"/>

  <!-- Background grid lines -->
  <line x1="20" y1="40" x2="460" y2="40" stroke="#064E3B" stroke-width="0.7" stroke-dasharray="4,4"/>
  <line x1="20" y1="75" x2="460" y2="75" stroke="#064E3B" stroke-width="0.7" stroke-dasharray="4,4"/>
  <line x1="20" y1="110" x2="460" y2="110" stroke="#064E3B" stroke-width="0.7" stroke-dasharray="4,4"/>

  <!-- Glowing ECG Pulse line across the card -->
  <path d="M 20 75 L 140 75 L 155 45 L 170 105 L 185 60 L 195 85 L 205 75 L 340 75 L 350 55 L 360 95 L 370 75 L 460 75" 
        fill="none" stroke="url(#lineG1)" stroke-width="2.5" filter="url(#glow1)"/>

  <!-- Medical Cross Icon with glowing pulse -->
  <g transform="translate(32, 24)" filter="url(#glow1)">
    <circle cx="16" cy="16" r="18" fill="#065F46" stroke="#34D399" stroke-width="1.5"/>
    <rect x="13" y="7" width="6" height="18" rx="2" fill="#34D399"/>
    <rect x="7" y="13" width="18" height="6" rx="2" fill="#34D399"/>
  </g>

  <!-- Title & Subtitle -->
  <text x="75" y="32" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">AIVOA-CRM-HCP</text>
  <text x="75" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10.5" font-weight="600" fill="#34D399">AI-POWERED HEALTHCARE CRM &amp; HCP ANALYTICS</text>

  <!-- Key Metrics / Feature Badges -->
  <g transform="translate(24, 118)">
    <rect x="0" y="0" width="125" height="22" rx="11" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <text x="62" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#A7F3D0" text-anchor="middle">⚡ 40-70% Less Effort</text>

    <rect x="133" y="0" width="120" height="22" rx="11" fill="#083344" stroke="#0891B2" stroke-width="1"/>
    <text x="193" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#67E8F9" text-anchor="middle">🏥 500+ HCP Users</text>

    <rect x="261" y="0" width="105" height="22" rx="11" fill="#1E1B4B" stroke="#4F46E5" stroke-width="1"/>
    <text x="313" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#C7D2FE" text-anchor="middle">🔗 FastAPI + React</text>
  </g>

  <!-- Status indicator badge -->
  <rect x="375" y="18" width="85" height="20" rx="10" fill="#042F2E" stroke="#14B8A6" stroke-width="1"/>
  <circle cx="387" cy="28" r="4" fill="#2DD4BF"/>
  <text x="397" y="32" font-family="monospace" font-size="9" font-weight="bold" fill="#2DD4BF">PRODUCTION</text>
</svg>'''

# ==============================================================================
# 2. Customer Health Care CRM App (Predictive Analytics & Clustering)
# ==============================================================================
svg_2 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="150" viewBox="0 0 480 150">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#180B26"/>
      <stop offset="50%" stop-color="#2D0B38"/>
      <stop offset="100%" stop-color="#0D1117"/>
    </linearGradient>
    <linearGradient id="barG2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#EC4899"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <filter id="glow2" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="150" rx="12" fill="url(#bg2)" stroke="#A855F7" stroke-width="1.5"/>

  <!-- Brain & Data Node Icon -->
  <g transform="translate(30, 24)" filter="url(#glow2)">
    <circle cx="16" cy="16" r="18" fill="#3B0764" stroke="#D8B4FE" stroke-width="1.5"/>
    <!-- Node network -->
    <circle cx="16" cy="10" r="3" fill="#F472B6"/>
    <circle cx="9" cy="20" r="3" fill="#A78BFA"/>
    <circle cx="23" cy="20" r="3" fill="#A78BFA"/>
    <line x1="16" y1="10" x2="9" y2="20" stroke="#E879F9" stroke-width="1.5"/>
    <line x1="16" y1="10" x2="23" y2="20" stroke="#E879F9" stroke-width="1.5"/>
    <line x1="9" y1="20" x2="23" y2="20" stroke="#E879F9" stroke-width="1.5"/>
  </g>

  <!-- Title & Subtitle -->
  <text x="75" y="32" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">Customer Health Care CRM</text>
  <text x="75" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10.5" font-weight="600" fill="#F472B6">PREDICTIVE ANALYTICS &amp; PATIENT CLUSTERING</text>

  <!-- Mini Predictive Analytics Bar/Cluster Graphic on the right -->
  <g transform="translate(350, 52)">
    <rect x="0" y="35" width="12" height="25" rx="3" fill="url(#barG2)"/>
    <rect x="18" y="20" width="12" height="40" rx="3" fill="url(#barG2)"/>
    <rect x="36" y="8" width="12" height="52" rx="3" fill="url(#barG2)"/>
    <rect x="54" y="28" width="12" height="32" rx="3" fill="url(#barG2)"/>
    <rect x="72" y="15" width="12" height="45" rx="3" fill="url(#barG2)"/>
    <line x1="-5" y1="62" x2="90" y2="62" stroke="#4C1D95" stroke-width="1"/>
  </g>

  <!-- Scatter plot dots (clusters) -->
  <circle cx="160" cy="78" r="3.5" fill="#38BDF8" opacity="0.8"/>
  <circle cx="185" cy="72" r="4.5" fill="#38BDF8" opacity="0.9"/>
  <circle cx="170" cy="92" r="3" fill="#38BDF8" opacity="0.7"/>
  <circle cx="230" cy="75" r="4" fill="#F472B6" opacity="0.9"/>
  <circle cx="250" cy="88" r="5" fill="#F472B6" opacity="0.8"/>
  <circle cx="270" cy="70" r="3.5" fill="#F472B6" opacity="0.9"/>
  <path d="M 130 98 Q 200 82 320 68" fill="none" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.8"/>

  <!-- Metric Badges -->
  <g transform="translate(24, 118)">
    <rect x="0" y="0" width="120" height="22" rx="11" fill="#4A044E" stroke="#C026D3" stroke-width="1"/>
    <text x="60" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#F5D0FE" text-anchor="middle">🎯 +30% Accuracy</text>

    <rect x="128" y="0" width="115" height="22" rx="11" fill="#2E1065" stroke="#7C3AED" stroke-width="1"/>
    <text x="185" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#DDD6FE" text-anchor="middle">🤖 Scikit-Learn</text>

    <rect x="251" y="0" width="110" height="22" rx="11" fill="#1E293B" stroke="#64748B" stroke-width="1"/>
    <text x="306" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#E2E8F0" text-anchor="middle">📊 Pandas &amp; EDA</text>
  </g>
</svg>'''

# ==============================================================================
# 3. SkC Jeevan Tutor (Interactive Python Learning Platform)
# ==============================================================================
svg_3 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="150" viewBox="0 0 480 150">
  <defs>
    <linearGradient id="bg3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="50%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <filter id="glow3" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="150" rx="12" fill="url(#bg3)" stroke="#38BDF8" stroke-width="1.5"/>

  <!-- Code Editor Frame on the right -->
  <g transform="translate(230, 20)">
    <rect width="230" height="85" rx="8" fill="#090D16" stroke="#334155" stroke-width="1"/>
    <!-- Window buttons -->
    <circle cx="12" cy="12" r="3.5" fill="#EF4444"/>
    <circle cx="22" cy="12" r="3.5" fill="#F59E0B"/>
    <circle cx="32" cy="12" r="3.5" fill="#10B981"/>
    <text x="50" y="15" font-family="monospace" font-size="8.5" fill="#64748B">main.py</text>
    <line x1="0" y1="22" x2="230" y2="22" stroke="#1E293B" stroke-width="1"/>
    <!-- Code lines -->
    <text x="12" y="38" font-family="monospace" font-size="9" fill="#F472B6">def <tspan fill="#38BDF8">learn_python</tspan>():</text>
    <text x="24" y="52" font-family="monospace" font-size="9" fill="#94A3B8">skills = [<tspan fill="#FDE047">"Data"</tspan>, <tspan fill="#FDE047">"ML"</tspan>]</text>
    <text x="24" y="66" font-family="monospace" font-size="9" fill="#F472B6">return <tspan fill="#34D399">"Mastered 🚀"</tspan></text>
    <rect x="135" y="58" width="6" height="10" fill="#38BDF8">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Book / Code Icon on Left -->
  <g transform="translate(28, 26)" filter="url(#glow3)">
    <circle cx="16" cy="16" r="18" fill="#0C4A6E" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="16" y="22" font-size="16" text-anchor="middle">💻</text>
  </g>

  <text x="75" y="34" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">SkC Jeevan Tutor</text>
  <text x="75" y="50" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10.5" font-weight="600" fill="#38BDF8">INTERACTIVE PYTHON LEARNING PLATFORM</text>

  <!-- Progress bar -->
  <g transform="translate(75, 70)">
    <text x="0" y="9" font-family="monospace" font-size="9" fill="#94A3B8">Tutorial Modules Completed</text>
    <rect x="0" y="14" width="135" height="8" rx="4" fill="#1E293B"/>
    <rect x="0" y="14" width="115" height="8" rx="4" fill="#0284C7"/>
    <text x="142" y="21" font-family="monospace" font-size="8.5" font-weight="bold" fill="#38BDF8">85%</text>
  </g>

  <!-- Tags -->
  <g transform="translate(24, 118)">
    <rect x="0" y="0" width="115" height="22" rx="11" fill="#1E3A8A" stroke="#2563EB" stroke-width="1"/>
    <text x="57" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#93C5FD" text-anchor="middle">🐍 Python 3</text>

    <rect x="123" y="0" width="115" height="22" rx="11" fill="#431407" stroke="#EA580C" stroke-width="1"/>
    <text x="180" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#FDBA74" text-anchor="middle">🌐 HTML5 / JS</text>

    <rect x="246" y="0" width="125" height="22" rx="11" fill="#064E3B" stroke="#059669" stroke-width="1"/>
    <text x="308" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#6EE7B7" text-anchor="middle">⚡ Live Code Runner</text>
  </g>
</svg>'''

# ==============================================================================
# 4. California House Price Prediction (ML Regression)
# ==============================================================================
svg_4 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="150" viewBox="0 0 480 150">
  <defs>
    <linearGradient id="bg4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1C1917"/>
      <stop offset="60%" stop-color="#292524"/>
      <stop offset="100%" stop-color="#0C0A09"/>
    </linearGradient>
    <linearGradient id="curveG4" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#EF4444"/>
    </linearGradient>
    <filter id="glow4" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="150" rx="12" fill="url(#bg4)" stroke="#F59E0B" stroke-width="1.5"/>

  <!-- Icon: House with Trend Arrow -->
  <g transform="translate(30, 24)" filter="url(#glow4)">
    <circle cx="16" cy="16" r="18" fill="#451A03" stroke="#FBBF24" stroke-width="1.5"/>
    <path d="M 8 18 L 16 10 L 24 18 L 24 24 L 8 24 Z" fill="none" stroke="#FDE68A" stroke-width="1.5"/>
    <rect x="13" y="19" width="6" height="5" fill="#FDE68A"/>
  </g>

  <!-- Title & Subtitle -->
  <text x="75" y="32" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">California House Price Pred</text>
  <text x="75" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10.5" font-weight="600" fill="#FBBF24">ML REGRESSION &amp; GEOSPATIAL VALUATION</text>

  <!-- Regression Graph on the right -->
  <g transform="translate(290, 20)">
    <rect width="170" height="85" rx="8" fill="#141211" stroke="#44403C" stroke-width="1"/>
    <line x1="20" y1="70" x2="155" y2="70" stroke="#78716C" stroke-width="1"/>
    <line x1="20" y1="15" x2="20" y2="70" stroke="#78716C" stroke-width="1"/>
    
    <!-- Data points -->
    <circle cx="35" cy="62" r="2.5" fill="#FBBF24" opacity="0.6"/>
    <circle cx="50" cy="55" r="3" fill="#FBBF24" opacity="0.8"/>
    <circle cx="68" cy="48" r="2.5" fill="#FBBF24" opacity="0.7"/>
    <circle cx="85" cy="40" r="3" fill="#FBBF24" opacity="0.9"/>
    <circle cx="105" cy="32" r="2.5" fill="#FBBF24" opacity="0.7"/>
    <circle cx="125" cy="25" r="3" fill="#FBBF24" opacity="0.8"/>
    <circle cx="145" cy="22" r="3.5" fill="#FBBF24" opacity="0.9"/>

    <!-- Best Fit Regression Line -->
    <line x1="25" y1="67" x2="150" y2="20" stroke="url(#curveG4)" stroke-width="2" filter="url(#glow4)"/>
    <text x="90" y="16" font-family="monospace" font-size="8.5" font-weight="bold" fill="#F59E0B">R² = 0.86</text>
  </g>

  <!-- Metrics / Features -->
  <g transform="translate(24, 118)">
    <rect x="0" y="0" width="115" height="22" rx="11" fill="#451A03" stroke="#D97706" stroke-width="1"/>
    <text x="57" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#FDE68A" text-anchor="middle">📈 Random Forest</text>

    <rect x="123" y="0" width="115" height="22" rx="11" fill="#3B0764" stroke="#7E22CE" stroke-width="1"/>
    <text x="180" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#E9D5FF" text-anchor="middle">🗺️ Geo Features</text>

    <rect x="246" y="0" width="115" height="22" rx="11" fill="#1C1917" stroke="#78716C" stroke-width="1"/>
    <text x="303" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#F5F5F4" text-anchor="middle">📊 Scikit-Learn</text>
  </g>
</svg>'''

# ==============================================================================
# 5. Deep Learning Projects (Neural Networks, CNNs, Transformers)
# ==============================================================================
svg_5 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="150" viewBox="0 0 480 150">
  <defs>
    <linearGradient id="bg5" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1A0B2E"/>
      <stop offset="50%" stop-color="#110B22"/>
      <stop offset="100%" stop-color="#0A0614"/>
    </linearGradient>
    <filter id="glow5" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="150" rx="12" fill="url(#bg5)" stroke="#EC4899" stroke-width="1.5"/>

  <!-- Neural Net Icon -->
  <g transform="translate(30, 24)" filter="url(#glow5)">
    <circle cx="16" cy="16" r="18" fill="#500724" stroke="#F472B6" stroke-width="1.5"/>
    <text x="16" y="22" font-size="16" text-anchor="middle">🤖</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="75" y="32" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">Deep Learning Projects</text>
  <text x="75" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10.5" font-weight="600" fill="#F472B6">CNNs, RNNs, VISION &amp; TRANSFORMER ARCHITECTURES</text>

  <!-- Multi-Layer Neural Network Architecture Diagram on Right -->
  <g transform="translate(280, 25)">
    <!-- Synapse lines -->
    <!-- Layer 1 to Layer 2 -->
    <line x1="20" y1="20" x2="70" y2="12" stroke="#831843" stroke-width="1"/>
    <line x1="20" y1="20" x2="70" y2="35" stroke="#831843" stroke-width="1"/>
    <line x1="20" y1="20" x2="70" y2="58" stroke="#831843" stroke-width="1"/>
    <line x1="20" y1="50" x2="70" y2="12" stroke="#831843" stroke-width="1"/>
    <line x1="20" y1="50" x2="70" y2="35" stroke="#F472B6" stroke-width="1.5"/>
    <line x1="20" y1="50" x2="70" y2="58" stroke="#831843" stroke-width="1"/>
    <!-- Layer 2 to Layer 3 -->
    <line x1="70" y1="12" x2="120" y2="25" stroke="#BE185D" stroke-width="1"/>
    <line x1="70" y1="35" x2="120" y2="25" stroke="#F472B6" stroke-width="1.5"/>
    <line x1="70" y1="58" x2="120" y2="45" stroke="#BE185D" stroke-width="1"/>
    <!-- Layer 3 to Output -->
    <line x1="120" y1="25" x2="165" y2="35" stroke="#F472B6" stroke-width="2"/>
    <line x1="120" y1="45" x2="165" y2="35" stroke="#BE185D" stroke-width="1"/>

    <!-- Nodes (Layer 1) -->
    <circle cx="20" cy="20" r="5" fill="#38BDF8"/>
    <circle cx="20" cy="50" r="5" fill="#38BDF8"/>

    <!-- Nodes (Layer 2 Hidden) -->
    <circle cx="70" cy="12" r="5" fill="#A855F7"/>
    <circle cx="70" cy="35" r="6" fill="#F472B6" filter="url(#glow5)"/>
    <circle cx="70" cy="58" r="5" fill="#A855F7"/>

    <!-- Nodes (Layer 3 Hidden) -->
    <circle cx="120" cy="25" r="6" fill="#F472B6" filter="url(#glow5)"/>
    <circle cx="120" cy="45" r="5" fill="#EC4899"/>

    <!-- Output Node -->
    <circle cx="165" cy="35" r="7" fill="#22C55E" filter="url(#glow5)"/>
  </g>

  <!-- Badges -->
  <g transform="translate(24, 118)">
    <rect x="0" y="0" width="115" height="22" rx="11" fill="#431407" stroke="#EA580C" stroke-width="1"/>
    <text x="57" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#FDBA74" text-anchor="middle">🔥 PyTorch</text>

    <rect x="123" y="0" width="125" height="22" rx="11" fill="#451A03" stroke="#D97706" stroke-width="1"/>
    <text x="185" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#FDE68A" text-anchor="middle">⚡ TensorFlow</text>

    <rect x="256" y="0" width="115" height="22" rx="11" fill="#3B0764" stroke="#7E22CE" stroke-width="1"/>
    <text x="313" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#E9D5FF" text-anchor="middle">🧠 CNN &amp; NLP</text>
  </g>
</svg>'''

# ==============================================================================
# 6. Deep-ML Practice (Algorithms from Scratch in NumPy)
# ==============================================================================
svg_6 = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="150" viewBox="0 0 480 150">
  <defs>
    <linearGradient id="bg6" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#021E36"/>
      <stop offset="50%" stop-color="#082F49"/>
      <stop offset="100%" stop-color="#0B132B"/>
    </linearGradient>
    <filter id="glow6" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="480" height="150" rx="12" fill="url(#bg6)" stroke="#0284C7" stroke-width="1.5"/>

  <!-- Math / Matrix Icon -->
  <g transform="translate(30, 24)" filter="url(#glow6)">
    <circle cx="16" cy="16" r="18" fill="#0C4A6E" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="16" y="22" font-size="17" text-anchor="middle" fill="#E0F2FE" font-weight="bold">∑</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="75" y="32" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="16" font-weight="800" fill="#FFFFFF">Deep-ML Practice</text>
  <text x="75" y="48" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="10.5" font-weight="600" fill="#38BDF8">ALGORITHMS BUILT FROM SCRATCH IN PURE NUMPY</text>

  <!-- Mathematical Formula & Matrix Board on the right -->
  <g transform="translate(285, 20)">
    <rect width="175" height="85" rx="8" fill="#031A2F" stroke="#0369A1" stroke-width="1"/>
    <!-- Gradient descent formula display -->
    <text x="14" y="28" font-family="Georgia,serif" font-size="13" font-style="italic" fill="#38BDF8">θ := θ - α ∇J(θ)</text>
    <line x1="14" y1="40" x2="160" y2="40" stroke="#075985" stroke-width="1"/>
    <!-- Matrix bracket visual -->
    <text x="14" y="58" font-family="monospace" font-size="10" fill="#7DD3FC">[W·X + b] → ReLU</text>
    <text x="14" y="74" font-family="monospace" font-size="9" fill="#4ADE80">Backprop: ∂L/∂W = δ·Xᵀ</text>
  </g>

  <!-- Metric Badges -->
  <g transform="translate(24, 118)">
    <rect x="0" y="0" width="115" height="22" rx="11" fill="#0C4A6E" stroke="#0284C7" stroke-width="1"/>
    <text x="57" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#BAE6FD" text-anchor="middle">📐 Pure NumPy</text>

    <rect x="123" y="0" width="125" height="22" rx="11" fill="#14532D" stroke="#16A34A" stroke-width="1"/>
    <text x="185" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#BBF7D0" text-anchor="middle">⚡ Zero Frameworks</text>

    <rect x="256" y="0" width="115" height="22" rx="11" fill="#1E1B4B" stroke="#4338CA" stroke-width="1"/>
    <text x="313" y="14" font-family="monospace" font-size="10" font-weight="bold" fill="#C7D2FE" text-anchor="middle">🎓 Math Proofs</text>
  </g>
</svg>'''

# Save and verify all 6
save_and_verify("aivoa_crm.svg", svg_1)
save_and_verify("customer_healthcare.svg", svg_2)
save_and_verify("skc_tutor.svg", svg_3)
save_and_verify("california_housing.svg", svg_4)
save_and_verify("deep_learning.svg", svg_5)
save_and_verify("deep_ml.svg", svg_6)

print("All 6 project banners successfully generated and verified!")
