"""
Build perfectly aligned, high-resolution, silky-smooth animated ML project visualizations.
Canvas: W = 600, H = 270 (Aspect Ratio: 2.22 : 1)
Symmetric Grid:
- Card width: 600, Left Margin = 24, Right Margin = 24 -> Inner Width = 552
- Single Panel: x = 24, w = 552
- Dual Panel: Panel 1: x = 24, w = 268; Gap = 16; Panel 2: x = 308, w = 268 (24 + 268 + 16 + 268 = 576, Right margin = 24)
- Exact Vertical Grid:
  y = 0..30 : Top Header Bar
  y = 36..52 : Title Text (16px bold)
  y = 54..68 : Subtitle Text (11px regular)
  y = 74..218: Visualization Canvas (Height = 144)
  y = 226..252: Metric Badge Row (Height = 26)
  y = 252..270: Bottom Margin (18px)
"""
import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")

W, H = 600, 270
N_FRAMES = 24  # 24 frames for ultra-smooth 15 fps animation

# Load fonts
try:
    font_cat = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 11)
    font_stat = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 10)
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 15)
    font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 11)
    font_bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 11)
    font_small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 9)
    font_code = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 10)
    font_code_b = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 10)
except Exception:
    font_cat = ImageFont.load_default()
    font_stat = font_cat
    font_title = font_cat
    font_sub = font_cat
    font_bold = font_cat
    font_small = font_cat
    font_code = font_cat
    font_code_b = font_cat

def create_base_canvas(category, title, subtitle, status_txt, status_col, cat_col):
    img = Image.new("RGBA", (W, H), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer card border
    draw.rounded_rectangle([(0, 0), (W - 1, H - 1)], radius=12, fill=(16, 21, 28, 255), outline=(48, 54, 61, 255), width=2)
    
    # Top header bar
    draw.rounded_rectangle([(0, 0), (W - 1, 30)], radius=12, fill=(22, 27, 34, 255))
    draw.rectangle([(0, 16), (W - 1, 30)], fill=(22, 27, 34, 255))
    draw.line([(0, 30), (W, 30)], fill=(48, 54, 61, 255), width=1)
    
    # Category tag (left aligned at 24)
    draw.text((24, 8), category, font=font_cat, fill=cat_col)
    
    # Status pill (right aligned at W - 24)
    pill_w = len(status_txt) * 6.5 + 26
    pill_x = W - 24 - pill_w
    draw.rounded_rectangle([(pill_x, 6), (W - 24, 24)], radius=9, fill=(13, 17, 23, 255), outline=status_col, width=1)
    draw.ellipse([(pill_x + 8, 12), (pill_x + 14, 18)], fill=status_col)
    draw.text((pill_x + 19, 8), status_txt, font=font_stat, fill=status_col)
    
    # Title & Subtitle
    draw.text((24, 38), title, font=font_title, fill=(255, 255, 255, 255))
    draw.text((24, 56), subtitle, font=font_sub, fill=(139, 148, 158, 255))
    
    return img, draw

def draw_pill(draw, x, y, text, bg, border, fg):
    tw = len(text) * 6.2 + 18
    draw.rounded_rectangle([(x, y), (x + tw, y + 24)], radius=5, fill=bg, outline=border, width=1)
    draw.text((x + 9, y + 5), text, font=font_bold, fill=fg)
    return x + tw + 10


# ==============================================================================
# 1. AIVOA-CRM-HCP (Full width perfectly centered waveform + scanning tooltip)
# ==============================================================================
print("Rendering 1/6: AIVOA-CRM-HCP...")
frames_1 = []
gx, gy, gw, gh = 24, 76, 552, 140

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "AIVOA-CRM-HCP // PRODUCTION TELEMETRY",
        "🏥 Healthcare Professional (HCP) Interaction Stream",
        "Live engagement velocity, automated transcription & latency telemetry",
        "ONLINE 99.8%", (52, 211, 153, 255), (52, 211, 153, 255)
    )
    
    # Visual Box
    draw.rectangle([(gx, gy), (gx + gw, gy + gh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    
    # Grid lines & Y axis
    for i, yl in enumerate(["600", "400", "200", "0"]):
        yy = gy + int(i * (gh / 3))
        draw.line([(gx, yy), (gx + gw, yy)], fill=(22, 27, 34, 255), width=1)
        draw.text((gx + 6, yy - 12), yl, font=font_small, fill=(110, 118, 129, 255))
        
    for i, tm in enumerate(["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "NOW"]):
        xx = gx + int(i * (gw / 6))
        draw.line([(xx, gy), (xx, gy + gh)], fill=(22, 27, 34, 255), width=1)
        draw.text((xx - 12, gy + gh - 14), tm, font=font_small, fill=(110, 118, 129, 255))
        
    # Smooth harmonic curve
    xs = np.linspace(0, 4 * np.pi, gw)
    shift = (f / N_FRAMES) * 2 * np.pi
    ys = (
        np.sin(xs + shift) * 26 + 
        np.sin(2.2 * xs - shift * 0.7) * 16 + 
        np.cos(0.5 * xs + shift) * 20 + 
        75
    )
    
    # Area fill
    pts_area = [(gx, gy + gh)]
    for i in range(gw):
        pts_area.append((gx + i, gy + gh - int(ys[i])))
    pts_area.append((gx + gw, gy + gh))
    draw.polygon(pts_area, fill=(6, 78, 59, 130))
    
    # Wave line
    draw.line([(gx + i, gy + gh - int(ys[i])) for i in range(gw)], fill=(52, 211, 153, 255), width=2)
    
    # Scanning crosshair (sweeps left to right)
    scan_idx = int((f / N_FRAMES) * (gw - 60)) + 30
    scan_x = gx + scan_idx
    scan_y = gy + gh - int(ys[scan_idx])
    
    draw.line([(scan_x, gy), (scan_x, gy + gh)], fill=(0, 217, 255, 160), width=1)
    draw.ellipse([(scan_x - 5, scan_y - 5), (scan_x + 5, scan_y + 5)], fill=(0, 217, 255, 255), outline=(255, 255, 255, 255), width=2)
    
    # Floating Tooltip
    tip_w, tip_h = 160, 32
    tip_x = min(scan_x - tip_w // 2, gx + gw - tip_w - 8)
    tip_x = max(tip_x, gx + 8)
    tip_y = max(gy + 8, scan_y - tip_h - 12)
    
    draw.rounded_rectangle([(tip_x, tip_y), (tip_x + tip_w, tip_y + tip_h)], radius=4, fill=(16, 21, 28, 245), outline=(0, 217, 255, 255), width=1)
    hcp_val = int(ys[scan_idx] * 6.2)
    draw.text((tip_x + 8, tip_y + 5), f"HCP Engagement: {hcp_val} events", font=font_code_b, fill=(255, 255, 255, 255))
    draw.text((tip_x + 8, tip_y + 18), "Latency: 12ms | NLP Sync: 99%", font=font_small, fill=(52, 211, 153, 255))
    
    # Badges (symmetrically starting at 24)
    bx = 24
    bx = draw_pill(draw, bx, 230, "⚡ 40-70% Manual Effort Cut", (6, 78, 59, 180), (16, 185, 129, 255), (167, 243, 208, 255))
    bx = draw_pill(draw, bx, 230, "🏥 500+ Active HCPs", (8, 51, 68, 180), (8, 145, 178, 255), (103, 232, 249, 255))
    bx = draw_pill(draw, bx, 230, "FastAPI Async Core", (30, 27, 75, 180), (79, 70, 229, 255), (199, 210, 254, 255))
    draw_pill(draw, bx, 230, "React Frontend", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_1.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_1[0].save("project_aivoa_crm.gif", save_all=True, append_images=frames_1[1:], duration=70, loop=0)


# ==============================================================================
# 2. Customer Health Care CRM (Symmetric 268px + 268px dual panel)
# ==============================================================================
print("Rendering 2/6: Customer Health Care CRM...")
frames_2 = []
p1_x, p1_w = 24, 268
p2_x, p2_w = 308, 268
py, ph = 76, 140

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "HEALTHCARE ANALYTICS // CLASSIFICATION ENGINE",
        "🧠 Patient Risk Prediction & ROC-AUC Validation",
        "Discriminative threshold analysis & cohort risk probability distributions",
        "AUC: 0.942", (244, 114, 182, 255), (216, 180, 254, 255)
    )
    
    # Left Panel: ROC Curve (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p1_x + 8, py + 8), "ROC-AUC Curve (TPR vs FPR)", font=font_code_b, fill=(216, 180, 254, 255))
    
    # Baseline diagonal
    draw.line([(p1_x, py + ph), (p1_x + p1_w, py + 24)], fill=(48, 54, 61, 255), width=1)
    
    # Smooth ROC Curve
    curve_pts = []
    pts_auc = [(p1_x, py + ph)]
    for step in range(p1_w):
        fpr = step / p1_w
        tpr = 1.0 - math.pow(1.0 - fpr, 3.8)
        cx = p1_x + step
        cy = py + ph - int(tpr * (ph - 24))
        curve_pts.append((cx, cy))
        pts_auc.append((cx, cy))
    pts_auc.append((p1_x + p1_w, py + ph))
    
    draw.polygon(pts_auc, fill=(88, 28, 135, 95))
    draw.line(curve_pts, fill=(244, 114, 182, 255), width=2)
    
    # Dynamic operating point
    t_val = f / N_FRAMES
    opt_fpr = t_val * 0.72 + 0.04
    opt_tpr = 1.0 - math.pow(1.0 - opt_fpr, 3.8)
    ox = p1_x + int(opt_fpr * p1_w)
    oy = py + ph - int(opt_tpr * (ph - 24))
    
    draw.line([(ox, py + 24), (ox, py + ph)], fill=(244, 114, 182, 120), width=1)
    draw.line([(p1_x, oy), (p1_x + p1_w, oy)], fill=(244, 114, 182, 120), width=1)
    draw.ellipse([(ox - 4, oy - 4), (ox + 4, oy + 4)], fill=(255, 255, 255, 255), outline=(244, 114, 182, 255), width=2)
    
    draw.text((p1_x + 12, py + ph - 26), f"Threshold: {1 - t_val:.2f}", font=font_code_b, fill=(244, 114, 182, 255))
    draw.text((p1_x + 12, py + ph - 14), f"TPR: {opt_tpr*100:.1f}% | FPR: {opt_fpr*100:.1f}%", font=font_small, fill=(216, 180, 254, 255))
    
    # Right Panel: Risk Probability Distribution (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Patient Risk Cohort Distribution", font=font_code_b, fill=(103, 232, 249, 255))
    
    x_axis = np.linspace(-3, 3, p2_w)
    g_low = np.exp(-0.5 * ((x_axis + 1.2) / 0.8) ** 2) * 65
    g_high = np.exp(-0.5 * ((x_axis - 1.1) / 0.9) ** 2) * 60
    
    # Low Risk fill
    pts_l = [(p2_x, py + ph)]
    for i in range(p2_w):
        pts_l.append((p2_x + i, py + ph - int(g_low[i])))
    pts_l.append((p2_x + p2_w, py + ph))
    draw.polygon(pts_l, fill=(6, 78, 59, 110))
    draw.line([(p2_x + i, py + ph - int(g_low[i])) for i in range(p2_w)], fill=(52, 211, 153, 255), width=2)
    
    # High Risk fill
    pts_h = [(p2_x, py + ph)]
    for i in range(p2_w):
        pts_h.append((p2_x + i, py + ph - int(g_high[i])))
    pts_h.append((p2_x + p2_w, py + ph))
    draw.polygon(pts_h, fill=(136, 19, 55, 110))
    draw.line([(p2_x + i, py + ph - int(g_high[i])) for i in range(p2_w)], fill=(244, 114, 182, 255), width=2)
    
    # Decision boundary line
    db_x = p2_x + int(p2_w * 0.52 + math.sin(f / N_FRAMES * 2 * math.pi) * 8)
    draw.line([(db_x, py + 26), (db_x, py + ph)], fill=(255, 255, 255, 220), width=1)
    draw.text((db_x - 24, py + 28), "Boundary", font=font_small, fill=(255, 255, 255, 255))
    
    draw.text((p2_x + 10, py + ph - 14), "Low Risk (Healthy)", font=font_small, fill=(52, 211, 153, 255))
    draw.text((p2_x + p2_w - 95, py + ph - 14), "High Risk (Care+)", font=font_small, fill=(244, 114, 182, 255))
    
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "🎯 AUC-ROC 0.942", (74, 4, 78, 180), (192, 38, 211, 255), (245, 208, 254, 255))
    bx = draw_pill(draw, bx, 230, "+30% Prediction Accuracy", (46, 16, 101, 180), (124, 58, 237, 255), (221, 214, 254, 255))
    bx = draw_pill(draw, bx, 230, "Scikit-Learn Ensemble", (30, 41, 59, 180), (100, 116, 139, 255), (226, 232, 240, 255))
    draw_pill(draw, bx, 230, "Pandas Pipeline", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_2.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_2[0].save("project_customer_healthcare.gif", save_all=True, append_images=frames_2[1:], duration=70, loop=0)


# ==============================================================================
# 3. SkC Jeevan Tutor (Symmetric 268px + 268px dual panel)
# ==============================================================================
print("Rendering 3/6: SkC Jeevan Tutor...")
frames_3 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "SKC JEEVAN TUTOR // BENCHMARKING ENGINE",
        "📚 Algorithmic Complexity & Live Execution Profiler",
        "Big-O runtime analysis, AST parsing telemetry & real-time test verification",
        "10/10 PASSED", (56, 189, 248, 255), (56, 189, 248, 255)
    )
    
    # Left: Big-O Curves (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p1_x + 8, py + 8), "Time Complexity: O(N log N) vs O(N²)", font=font_code_b, fill=(56, 189, 248, 255))
    
    draw.line([(p1_x + 8, py + ph - 16), (p1_x + p1_w - 8, py + ph - 16)], fill=(48, 54, 61, 255), width=1)
    draw.line([(p1_x + 24, py + 24), (p1_x + 24, py + ph - 16)], fill=(48, 54, 61, 255), width=1)
    
    anim_prog = (f + 1) / N_FRAMES
    avail_w = p1_w - 40
    curr_pts_len = int(avail_w * anim_prog)
    
    pts_n2 = []
    pts_nlogn = []
    pts_lin = []
    for i in range(curr_pts_len):
        n = i / avail_w
        px = p1_x + 24 + i
        y_n2 = (py + ph - 16) - int((n ** 2) * (ph - 45))
        y_nlog = (py + ph - 16) - int((n * math.log(n * 9 + 1)) * (ph - 55))
        y_l = (py + ph - 16) - int(n * 30)
        pts_n2.append((px, y_n2))
        pts_nlogn.append((px, y_nlog))
        pts_lin.append((px, y_l))
        
    if len(pts_n2) > 1:
        draw.line(pts_n2, fill=(239, 68, 68, 240), width=2)
        draw.text((pts_n2[-1][0] - 26, pts_n2[-1][1] - 12), "O(N²)", font=font_small, fill=(239, 68, 68, 255))
    if len(pts_nlogn) > 1:
        draw.line(pts_nlogn, fill=(52, 211, 153, 255), width=2)
        draw.text((pts_nlogn[-1][0] - 44, pts_nlogn[-1][1] - 12), "O(N log N)", font=font_small, fill=(52, 211, 153, 255))
    if len(pts_lin) > 1:
        draw.line(pts_lin, fill=(56, 189, 248, 180), width=1)
        draw.text((pts_lin[-1][0] - 22, pts_lin[-1][1] - 10), "O(N)", font=font_small, fill=(56, 189, 248, 255))
        
    # Right: Compiler Runtime Telemetry (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(6, 10, 18, 255), outline=(30, 41, 59, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Compiler Runtime Telemetry", font=font_code_b, fill=(148, 163, 184, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(30, 41, 59, 255), width=1)
    
    draw.text((p2_x + 12, py + 34), "STATUS: EXECUTION PASS", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 12, py + 50), f"Exec Time: {0.012 + (f%4)*0.002:.4f}s", font=font_code, fill=(255, 255, 255, 255))
    draw.text((p2_x + 12, py + 66), "Memory Peak: 14.2 MB", font=font_code, fill=(56, 189, 248, 255))
    draw.text((p2_x + 12, py + 82), "GC Cycle: 0 paused (Optimal)", font=font_code, fill=(148, 163, 184, 255))
    
    # Progress Bar
    draw.text((p2_x + 12, py + 102), "Test Suite: 10/10 Passed 🚀", font=font_code_b, fill=(52, 211, 153, 255))
    bar_prog = int((f / N_FRAMES) * (p2_w - 24))
    draw.rounded_rectangle([(p2_x + 12, py + 118), (p2_x + p2_w - 12, py + 126)], radius=4, fill=(15, 23, 42, 255))
    draw.rounded_rectangle([(p2_x + 12, py + 118), (p2_x + 12 + bar_prog, py + 126)], radius=4, fill=(52, 211, 153, 255))
    
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "Python 3.12 Engine", (30, 58, 138, 180), (37, 99, 235, 255), (147, 197, 253, 255))
    bx = draw_pill(draw, bx, 230, "Live Sandbox Compiler", (6, 78, 59, 180), (5, 150, 105, 255), (110, 231, 183, 255))
    bx = draw_pill(draw, bx, 230, "Vanilla JS + HTML5", (67, 20, 7, 180), (234, 88, 12, 255), (253, 186, 116, 255))
    draw_pill(draw, bx, 230, "100% Client-Side", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_3.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_3[0].save("project_skc_tutor.gif", save_all=True, append_images=frames_3[1:], duration=70, loop=0)


# ==============================================================================
# 4. California Housing (Symmetric 268px + 268px dual panel)
# ==============================================================================
print("Rendering 4/6: California House Price Prediction...")
frames_4 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "CALIFORNIA HOUSING // REGRESSION TELEMETRY",
        "🏠 Geospatial Property Valuation & Feature Impact",
        "Gradient Boosting regression fit with confidence intervals & feature importances",
        "R² = 0.864", (251, 191, 36, 255), (251, 191, 36, 255)
    )
    
    # Left: Regression Scatter (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(12, 10, 8, 255), outline=(68, 40, 19, 255), width=1)
    draw.text((p1_x + 8, py + 8), "Income vs Price ($100k)", font=font_code_b, fill=(253, 230, 138, 255))
    
    # Axes
    draw.line([(p1_x + 28, py + ph - 20), (p1_x + p1_w - 12, py + ph - 20)], fill=(78, 48, 22, 255), width=1)
    draw.line([(p1_x + 28, py + 26), (p1_x + 28, py + ph - 20)], fill=(78, 48, 22, 255), width=1)
    
    np.random.seed(42)
    sample_x = np.linspace(p1_x + 34, p1_x + p1_w - 18, 38)
    noise = np.sin(sample_x * 0.12) * 8 + np.random.normal(0, 4.5, 38)
    sample_y = (py + ph - 25) - ((sample_x - p1_x - 34) / (p1_w - 52)) * 88 + noise
    
    for px, py_val in zip(sample_x, sample_y):
        draw.ellipse([(px - 2.5, py_val - 2.5), (px + 2.5, py_val + 2.5)], fill=(253, 230, 138, 180))
        
    anim_x_len = int((p1_w - 52) * ((f + 1) / N_FRAMES))
    x0, y0 = p1_x + 34, py + ph - 25
    x1 = x0 + anim_x_len
    y1 = y0 - int((anim_x_len / (p1_w - 52)) * 88)
    
    # Confidence band
    draw.polygon([(x0, y0 - 10), (x1, y1 - 10), (x1, y1 + 10), (x0, y0 + 10)], fill=(245, 158, 11, 45))
    draw.line([(x0, y0), (x1, y1)], fill=(239, 68, 68, 255), width=2)
    
    draw.text((p1_x + 34, py + 28), "R²: 0.864", font=font_bold, fill=(251, 191, 36, 255))
    draw.text((p1_x + 34, py + 42), "RMSE: $48,210", font=font_small, fill=(253, 230, 138, 255))
    
    # Right: Feature Importance Bar Chart (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(12, 10, 8, 255), outline=(68, 40, 19, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Feature Importance (Tree-Based)", font=font_code_b, fill=(253, 230, 138, 255))
    
    features = [
        ("MedInc", 0.52),
        ("HouseAge", 0.18),
        ("AveRooms", 0.14),
        ("Latitude", 0.10),
        ("Longitude", 0.06),
    ]
    
    for i, (feat, imp) in enumerate(features):
        by = py + 28 + i * 21
        draw.text((p2_x + 10, by), feat, font=font_code, fill=(200, 190, 180, 255))
        bar_len = int((imp / 0.55) * 140 * ((f + 3) / (N_FRAMES + 2)))
        draw.rounded_rectangle([(p2_x + 80, by + 2), (p2_x + 80 + bar_len, by + 14)], radius=3, fill=(245, 158, 11, 230))
        draw.text((p2_x + 84 + bar_len + 4, by), f"{imp*100:.0f}%", font=font_small, fill=(253, 230, 138, 255))
        
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "Gradient Boosting Regressor", (69, 26, 3, 180), (217, 119, 6, 255), (253, 230, 138, 255))
    bx = draw_pill(draw, bx, 230, "🗺️ Geospatial Valuation", (59, 7, 100, 180), (126, 34, 206, 255), (233, 213, 255, 255))
    bx = draw_pill(draw, bx, 230, "5-Fold Cross-Validated", (28, 25, 23, 180), (120, 113, 108, 255), (245, 245, 244, 255))
    draw_pill(draw, bx, 230, "Scikit-Learn", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_4.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_4[0].save("project_california_housing.gif", save_all=True, append_images=frames_4[1:], duration=70, loop=0)


# ==============================================================================
# 5. Deep Learning Projects (Full width perfectly centered TensorBoard dual curves)
# ==============================================================================
print("Rendering 5/6: Deep Learning Projects...")
frames_5 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "DEEP LEARNING // TENSORBOARD DYNAMICS",
        "🤖 Neural Network Training & Convergence Dynamics",
        "Dual-axis tracking: Cross-Entropy loss decay vs Validation Accuracy climb",
        "VAL ACC: 99.2%", (244, 114, 182, 255), (244, 114, 182, 255)
    )
    
    draw.rectangle([(gx, gy), (gx + gw, gy + gh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    
    # Grid lines
    for i in range(5):
        yy = gy + int(i * (gh / 4))
        draw.line([(gx, yy), (gx + gw, yy)], fill=(22, 27, 34, 255), width=1)
    for i in range(7):
        xx = gx + int(i * (gw / 6))
        draw.line([(xx, gy), (xx, gy + gh)], fill=(22, 27, 34, 255), width=1)
        draw.text((xx - 14, gy + gh - 14), f"Ep {i*20}", font=font_small, fill=(110, 118, 129, 255))
        
    draw.text((gx + 8, gy + 6), "Loss (Train)", font=font_small, fill=(244, 114, 182, 255))
    draw.text((gx + gw - 65, gy + 6), "Accuracy %", font=font_small, fill=(52, 211, 153, 255))
    
    curr_epoch_len = int(gw * ((f + 1) / N_FRAMES))
    epochs = np.linspace(0, 1, curr_epoch_len)
    
    np.random.seed(101)
    loss_vals = 2.3 * np.exp(-epochs * 4.2) + 0.04 + np.random.normal(0, 0.025, curr_epoch_len) * (1 - epochs * 0.7)
    loss_pts = [(gx + i, gy + int((loss_vals[i] / 2.5) * (gh - 24))) for i in range(curr_epoch_len)]
    
    acc_vals = 0.45 + 0.54 / (1.0 + np.exp(-epochs * 6.5 + 1.8))
    acc_pts = [(gx + i, gy + gh - int((acc_vals[i]) * (gh - 24))) for i in range(curr_epoch_len)]
    
    if len(loss_pts) > 1:
        draw.line(loss_pts, fill=(244, 114, 182, 255), width=2)
    if len(acc_pts) > 1:
        draw.line(acc_pts, fill=(52, 211, 153, 255), width=2)
        
    if curr_epoch_len > 10:
        cur_x = gx + curr_epoch_len - 1
        cur_loss_y = loss_pts[-1][1]
        cur_acc_y = acc_pts[-1][1]
        
        draw.ellipse([(cur_x - 4, cur_loss_y - 4), (cur_x + 4, cur_loss_y + 4)], fill=(244, 114, 182, 255))
        draw.ellipse([(cur_x - 4, cur_acc_y - 4), (cur_x + 4, cur_acc_y + 4)], fill=(52, 211, 153, 255))
        
        # Legend
        draw.rectangle([(gx + 12, gy + 22), (gx + 195, gy + 52)], fill=(13, 17, 23, 230), outline=(48, 54, 61, 255))
        draw.line([(gx + 18, gy + 32), (gx + 32, gy + 32)], fill=(244, 114, 182, 255), width=2)
        draw.text((gx + 38, gy + 27), f"Train Loss: {loss_vals[-1]:.3f}", font=font_code_b, fill=(244, 114, 182, 255))
        
        draw.line([(gx + 18, gy + 44), (gx + 32, gy + 44)], fill=(52, 211, 153, 255), width=2)
        draw.text((gx + 38, gy + 39), f"Val Acc: {acc_vals[-1]*100:.1f}%", font=font_code_b, fill=(52, 211, 153, 255))
        
    bx = 24
    bx = draw_pill(draw, bx, 230, "🔥 PyTorch Models", (67, 20, 7, 180), (234, 88, 12, 255), (253, 186, 116, 255))
    bx = draw_pill(draw, bx, 230, "ResNet + Conv2D", (69, 26, 3, 180), (217, 119, 6, 255), (253, 230, 138, 255))
    bx = draw_pill(draw, bx, 230, "AdamW + Cosine Decay", (59, 7, 100, 180), (126, 34, 206, 255), (233, 213, 255, 255))
    draw_pill(draw, bx, 230, "GPU Accelerated", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_5.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_5[0].save("project_deep_learning.gif", save_all=True, append_images=frames_5[1:], duration=70, loop=0)


# ==============================================================================
# 6. Deep-ML Practice (Symmetric 268px + 268px dual panel)
# ==============================================================================
print("Rendering 6/6: Deep-ML Practice...")
frames_6 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "ALGORITHMIC FOUNDATIONS // PURE NUMPY",
        "📐 Gradient Descent Trajectory on Loss Surface",
        "Analytical loss surface contours & vectorized optimization trajectory",
        "LOSS -> 0.001", (56, 189, 248, 255), (56, 189, 248, 255)
    )
    
    # Left: 2D Contour Map (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(6, 18, 30, 255), outline=(7, 89, 133, 255), width=1)
    draw.text((p1_x + 8, py + 8), "Loss Contours J(w₁, w₂) & Descent", font=font_code_b, fill=(56, 189, 248, 255))
    
    center_x, center_y = p1_x + 175, py + 75
    radii = [90, 68, 48, 32, 18, 8]
    colors_contour = [(7, 89, 133), (12, 74, 110), (14, 116, 144), (6, 148, 162), (13, 148, 136), (16, 185, 129)]
    
    for r, col in zip(radii, colors_contour):
        draw.ellipse([(center_x - r * 1.5, center_y - r), (center_x + r * 1.5, center_y + r)], outline=col + (200,), width=1)
        
    t_steps = 18
    curr_step = int((f / N_FRAMES) * t_steps)
    traj_pts = []
    
    start_x, start_y = p1_x + 25, py + 22
    for s in range(t_steps):
        alpha = s / t_steps
        px = start_x + (center_x - start_x) * (1.0 - math.exp(-s * 0.35)) + math.sin(s * 1.8) * 8 * (1.0 - alpha)
        py_pt = start_y + (center_y - start_y) * (1.0 - math.exp(-s * 0.35)) + math.cos(s * 1.8) * 6 * (1.0 - alpha)
        traj_pts.append((px, py_pt))
        
    active_pts = traj_pts[:curr_step + 1]
    if len(active_pts) > 1:
        draw.line(active_pts, fill=(239, 68, 68, 255), width=2)
        for pt in active_pts[:-1]:
            draw.ellipse([(pt[0] - 2, pt[1] - 2), (pt[0] + 2, pt[1] + 2)], fill=(253, 230, 138, 255))
        hx, hy = active_pts[-1]
        draw.ellipse([(hx - 4, hy - 4), (hx + 4, hy + 4)], fill=(255, 255, 255, 255), outline=(239, 68, 68, 255), width=2)
        
    draw.text((center_x - 12, center_y - 6), "Min", font=font_small, fill=(52, 211, 153, 255))
    
    # Right: Formula & Vectorized Proof Board (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(4, 14, 24, 255), outline=(7, 89, 133, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Vectorized NumPy Derivations", font=font_code_b, fill=(56, 189, 248, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(7, 89, 133, 255), width=1)
    
    draw.text((p2_x + 12, py + 34), "θ_next := θ - α · ∇J(θ)", font=font_code_b, fill=(74, 222, 128, 255))
    draw.text((p2_x + 12, py + 52), "dW = (1/m) · X.T @ (A - Y)", font=font_code, fill=(244, 114, 182, 255))
    draw.text((p2_x + 12, py + 68), "db = (1/m) · sum(dZ, axis=1)", font=font_code, fill=(253, 224, 71, 255))
    draw.text((p2_x + 12, py + 84), "V_dW = β·V_dW + (1-β)·dW", font=font_code, fill=(125, 211, 252, 255))
    
    cur_loss = 1.45 * math.exp(-curr_step * 0.28) + 0.001
    draw.text((p2_x + 12, py + 110), f"Step {curr_step*10:03d} | Loss: {cur_loss:.4f}", font=font_code_b, fill=(52, 211, 153, 255))
    
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "Vectorized Matrix Math", (12, 74, 110, 180), (2, 132, 199, 255), (186, 230, 253, 255))
    bx = draw_pill(draw, bx, 230, "Zero Frameworks (NumPy)", (20, 83, 45, 180), (22, 163, 74, 255), (187, 247, 208, 255))
    bx = draw_pill(draw, bx, 230, "Theoretical Proofs", (30, 27, 75, 180), (67, 56, 202, 255), (199, 210, 254, 255))
    draw_pill(draw, bx, 230, "Backpropagation", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_6.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_6[0].save("project_deep_ml.gif", save_all=True, append_images=frames_6[1:], duration=70, loop=0)

print("SUCCESS: All 6 perfectly aligned project visualizations generated!")
