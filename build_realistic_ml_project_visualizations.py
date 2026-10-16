import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")

W, H = 580, 260
N_FRAMES = 18

# Load clean Windows system fonts
try:
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 15)
    font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 11)
    font_bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 11)
    font_small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 9)
    font_code = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 11)
    font_code_sm = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 10)
    font_val = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 18)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_bold = font_title
    font_small = font_title
    font_code = font_title
    font_code_sm = font_title
    font_val = font_title

def create_card_base(category, title_text, subtitle_text, status_pill, status_color, header_tag_color):
    """Draws a professional, dark-mode dashboard card frame."""
    img = Image.new("RGBA", (W, H), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer container with rounded corners and subtle border
    draw.rounded_rectangle([(0, 0), (W - 1, H - 1)], radius=12, fill=(16, 21, 28, 255), outline=(48, 54, 61, 255), width=2)
    
    # Top header bar
    draw.rounded_rectangle([(0, 0), (W - 1, 30)], radius=12, fill=(22, 27, 34, 255))
    draw.rectangle([(0, 16), (W - 1, 30)], fill=(22, 27, 34, 255))
    draw.line([(0, 30), (W, 30)], fill=(48, 54, 61, 255), width=1)
    
    # Category tag
    draw.text((14, 8), category, font=font_code, fill=header_tag_color)
    
    # Status pill
    pw = 110
    draw.rounded_rectangle([(W - pw - 12, 6), (W - 12, 24)], radius=9, fill=(13, 17, 23, 255), outline=status_color, width=1)
    draw.ellipse([(W - pw - 4, 12), (W - pw + 2, 18)], fill=status_color)
    draw.text((W - pw + 8, 8), status_pill, font=font_code_sm, fill=status_color)
    
    # Title & Subtitle block
    draw.text((16, 36), title_text, font=font_title, fill=(255, 255, 255, 255))
    draw.text((16, 54), subtitle_text, font=font_sub, fill=(139, 148, 158, 255))
    
    return img, draw

def draw_pill(draw, x, y, text, bg, border, fg):
    tw = len(text) * 6.5 + 16
    draw.rounded_rectangle([(x, y), (x + tw, y + 20)], radius=4, fill=bg, outline=border, width=1)
    draw.text((x + 8, y + 3), text, font=font_bold, fill=fg)
    return x + tw + 8


# ==============================================================================
# 1. AIVOA-CRM-HCP: Live Interaction Velocity & Latency Waveform
# ==============================================================================
print("Generating 1/6: project_aivoa_crm.gif...")
frames_1 = []
gx, gy, gw, gh = 40, 75, 490, 130

for f in range(N_FRAMES):
    img, draw = create_card_base(
        "AIVOA-CRM-HCP // PRODUCTION TELEMETRY",
        "🏥 Healthcare Professional (HCP) Interaction Stream",
        "Real-time CRM logging velocity, NLP entity extraction & API latency",
        "LIVE STREAM", (52, 211, 153, 255), (52, 211, 153, 255)
    )
    
    # Graph Box
    draw.rectangle([(gx, gy), (gx + gw, gy + gh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    
    # Grid lines & Y-axis labels
    y_labels = ["600", "400", "200", "0"]
    for i, yl in enumerate(y_labels):
        yy = gy + int(i * (gh / 3))
        draw.line([(gx, yy), (gx + gw, yy)], fill=(22, 27, 34, 255), width=1)
        draw.text((gx - 28, yy - 5), yl, font=font_small, fill=(110, 118, 129, 255))
    
    # X-axis time labels
    times = ["09:00", "11:00", "13:00", "15:00", "17:00", "NOW"]
    for i, tm in enumerate(times):
        xx = gx + int(i * (gw / 5))
        draw.line([(xx, gy), (xx, gy + gh)], fill=(22, 27, 34, 255), width=1)
        draw.text((xx - 12, gy + gh + 4), tm, font=font_small, fill=(110, 118, 129, 255))
        
    # Generate smooth data curve using sine harmonics
    xs = np.linspace(0, 4 * np.pi, gw)
    shift = (f / N_FRAMES) * 2 * np.pi
    # Interaction stream waveform
    ys = (
        np.sin(xs + shift) * 22 + 
        np.sin(2 * xs - shift * 0.5) * 14 + 
        np.cos(0.5 * xs + shift) * 18 + 
        65
    )
    
    # Fill area under curve with semi-transparent emerald gradient
    curve_pts = [(gx, gy + gh)]
    for i in range(gw):
        curve_pts.append((gx + i, gy + gh - int(ys[i])))
    curve_pts.append((gx + gw, gy + gh))
    
    # Area polygon
    draw.polygon(curve_pts, fill=(6, 78, 59, 120))
    
    # Clean top curve line
    line_pts = [(gx + i, gy + gh - int(ys[i])) for i in range(gw)]
    draw.line(line_pts, fill=(52, 211, 153, 255), width=2)
    
    # Animated vertical scanning crosshair
    scan_idx = int((f / N_FRAMES) * (gw - 40)) + 20
    scan_x = gx + scan_idx
    scan_y = gy + gh - int(ys[scan_idx])
    
    draw.line([(scan_x, gy), (scan_x, gy + gh)], fill=(0, 217, 255, 180), width=1)
    draw.ellipse([(scan_x - 5, scan_y - 5), (scan_x + 5, scan_y + 5)], fill=(0, 217, 255, 255), outline=(255, 255, 255, 255), width=2)
    
    # Tooltip callout above crosshair
    tip_w, tip_h = 135, 28
    tip_x = min(scan_x - tip_w // 2, gx + gw - tip_w - 5)
    tip_x = max(tip_x, gx + 5)
    tip_y = max(gy + 6, scan_y - tip_h - 10)
    
    draw.rounded_rectangle([(tip_x, tip_y), (tip_x + tip_w, tip_y + tip_h)], radius=4, fill=(22, 27, 34, 240), outline=(0, 217, 255, 255), width=1)
    val_engagements = int(ys[scan_idx] * 6.5)
    draw.text((tip_x + 8, tip_y + 4), f"HCP Stream: {val_engagements} logs", font=font_code_sm, fill=(255, 255, 255, 255))
    draw.text((tip_x + 8, tip_y + 15), "Latency: 14ms | NLP: 98%", font=font_small, fill=(52, 211, 153, 255))
    
    # Bottom Telemetry Badges
    px = 40
    px = draw_pill(draw, px, 226, "⚡ 40-70% Manual Cut", (6, 78, 59, 180), (16, 185, 129, 255), (167, 243, 208, 255))
    px = draw_pill(draw, px, 226, "🏥 500+ Active HCPs", (8, 51, 68, 180), (8, 145, 178, 255), (103, 232, 249, 255))
    px = draw_pill(draw, px, 226, "FastAPI Async Core", (30, 27, 75, 180), (79, 70, 229, 255), (199, 210, 254, 255))
    draw_pill(draw, px, 226, "React Dashboard", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_1.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_1[0].save("project_aivoa_crm.gif", save_all=True, append_images=frames_1[1:], duration=100, loop=0)


# ==============================================================================
# 2. Customer Health Care CRM: Realistic ROC-AUC Curve & Classification Density
# ==============================================================================
print("Generating 2/6: project_customer_healthcare.gif...")
frames_2 = []

for f in range(N_FRAMES):
    img, draw = create_card_base(
        "HEALTHCARE ANALYTICS // CLASSIFICATION ENGINE",
        "🧠 Patient Risk Prediction & ROC-AUC Validation",
        "Discriminative threshold analysis & cohort risk probability distributions",
        "AUC: 0.942", (244, 114, 182, 255), (216, 180, 254, 255)
    )
    
    # Left: ROC Curve box (width 260)
    rx, ry, rw, rh = 40, 75, 230, 130
    draw.rectangle([(rx, ry), (rx + rw, ry + rh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((rx + 8, ry + 6), "ROC-AUC Curve (TPR vs FPR)", font=font_code_sm, fill=(216, 180, 254, 255))
    
    # Diagonal baseline reference line (random guess)
    draw.line([(rx, ry + rh), (rx + rw, ry)], fill=(48, 54, 61, 255), width=1)
    
    # True ROC Curve equation: y = 1 - (1 - x)^4
    pts_roc = [(rx, ry + rh)]
    curve_pts = []
    for step in range(rw):
        fpr = step / rw
        tpr = 1.0 - math.pow(1.0 - fpr, 3.8)
        px = rx + step
        py = ry + rh - int(tpr * rh)
        pts_roc.append((px, py))
        curve_pts.append((px, py))
    pts_roc.append((rx + rw, ry + rh))
    
    # Shaded AUC
    draw.polygon(pts_roc, fill=(88, 28, 135, 90))
    draw.line(curve_pts, fill=(244, 114, 182, 255), width=3)
    
    # Animated Operating Point (moving threshold)
    t_val = (f / N_FRAMES)
    opt_fpr = t_val * 0.7 + 0.05
    opt_tpr = 1.0 - math.pow(1.0 - opt_fpr, 3.8)
    ox = rx + int(opt_fpr * rw)
    oy = ry + rh - int(opt_tpr * rh)
    
    draw.line([(ox, ry), (ox, ry + rh)], fill=(244, 114, 182, 100), width=1)
    draw.line([(rx, oy), (rx + rw, oy)], fill=(244, 114, 182, 100), width=1)
    draw.ellipse([(ox - 5, oy - 5), (ox + 5, oy + 5)], fill=(255, 255, 255, 255), outline=(244, 114, 182, 255), width=2)
    
    draw.text((rx + 10, ry + rh - 22), f"Threshold: {1 - t_val:.2f}", font=font_code_sm, fill=(244, 114, 182, 255))
    draw.text((rx + 10, ry + rh - 12), f"TPR: {opt_tpr*100:.1f}% | FPR: {opt_fpr*100:.1f}%", font=font_small, fill=(216, 180, 254, 255))
    
    # Right: Patient Risk Probability Distribution (Density curve)
    dx, dy, dw, dh = 290, 75, 240, 130
    draw.rectangle([(dx, dy), (dx + dw, dy + dh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((dx + 8, dy + 6), "Patient Risk Cohort Probability Density", font=font_code_sm, fill=(103, 232, 249, 255))
    
    # Two Gaussian distributions (Low risk vs High risk)
    x_axis = np.linspace(-3, 3, dw)
    g_low = np.exp(-0.5 * ((x_axis + 1.2) / 0.8) ** 2) * 55
    g_high = np.exp(-0.5 * ((x_axis - 1.1) / 0.9) ** 2) * 52
    
    # Draw Low Risk area (Cyan)
    pts_low = [(dx, dy + dh)]
    for i in range(dw):
        pts_low.append((dx + i, dy + dh - int(g_low[i])))
    pts_low.append((dx + dw, dy + dh))
    draw.polygon(pts_low, fill=(6, 78, 59, 100))
    draw.line([(dx + i, dy + dh - int(g_low[i])) for i in range(dw)], fill=(52, 211, 153, 255), width=2)
    
    # Draw High Risk area (Pink)
    pts_high = [(dx, dy + dh)]
    for i in range(dw):
        pts_high.append((dx + i, dy + dh - int(g_high[i])))
    pts_high.append((dx + dw, dy + dh))
    draw.polygon(pts_high, fill=(136, 19, 55, 100))
    draw.line([(dx + i, dy + dh - int(g_high[i])) for i in range(dw)], fill=(244, 114, 182, 255), width=2)
    
    # Animated decision boundary divider line
    db_x = dx + int(dw * 0.52 + math.sin(f / N_FRAMES * 2 * math.pi) * 8)
    draw.line([(db_x, dy + 22), (db_x, dy + dh)], fill=(255, 255, 255, 220), width=2)
    draw.text((db_x - 30, dy + 26), "Boundary", font=font_small, fill=(255, 255, 255, 255))
    
    draw.text((dx + 16, dy + dh - 16), "Low Risk (Healthy)", font=font_small, fill=(52, 211, 153, 255))
    draw.text((dx + dw - 95, dy + dh - 16), "High Risk (Care+)", font=font_small, fill=(244, 114, 182, 255))
    
    # Badges
    px = 40
    px = draw_pill(draw, px, 226, "🎯 AUC-ROC 0.942", (74, 4, 78, 180), (192, 38, 211, 255), (245, 208, 254, 255))
    px = draw_pill(draw, px, 226, "+30% Prediction Accuracy", (46, 16, 101, 180), (124, 58, 237, 255), (221, 214, 254, 255))
    px = draw_pill(draw, px, 226, "Scikit-Learn Ensemble", (30, 41, 59, 180), (100, 116, 139, 255), (226, 232, 240, 255))
    draw_pill(draw, px, 226, "Pandas Pipeline", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_2.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_2[0].save("project_customer_healthcare.gif", save_all=True, append_images=frames_2[1:], duration=100, loop=0)


# ==============================================================================
# 3. SkC Jeevan Tutor: Algorithmic Complexity Benchmark & Compiler Monitor
# ==============================================================================
print("Generating 3/6: project_skc_tutor.gif...")
frames_3 = []

for f in range(N_FRAMES):
    img, draw = create_card_base(
        "SKC JEEVAN TUTOR // BENCHMARKING ENGINE",
        "📚 Algorithmic Complexity & Live Execution Profiler",
        "Big-O runtime analysis, AST parsing telemetry & real-time test verification",
        "10/10 PASSED", (56, 189, 248, 255), (56, 189, 248, 255)
    )
    
    # Left: Big-O Curves Benchmark Graph (width 270)
    bx, by, bw, bh = 40, 75, 250, 130
    draw.rectangle([(bx, by), (bx + bw, by + bh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((bx + 8, by + 6), "Time Complexity: O(N log N) vs O(N²)", font=font_code_sm, fill=(56, 189, 248, 255))
    
    # Grid lines
    draw.line([(bx, by + bh - 1), (bx + bw, by + bh - 1)], fill=(48, 54, 61, 255), width=1)
    draw.line([(bx + 1, by), (bx + 1, by + bh)], fill=(48, 54, 61, 255), width=1)
    
    # Animated draw of N^2 curve (Red) vs N log N (Green)
    anim_progress = (f + 1) / N_FRAMES
    max_pts = int(bw * anim_progress)
    
    pts_n2 = []
    pts_nlogn = []
    pts_linear = []
    for i in range(max_pts):
        n = i / bw
        # N^2 curve
        y_n2 = by + bh - int((n ** 2) * (bh - 25))
        pts_n2.append((bx + i, y_n2))
        # N log N curve
        y_nlogn = by + bh - int((n * math.log(n * 9 + 1)) * (bh - 40))
        pts_nlogn.append((bx + i, y_nlogn))
        # O(1) baseline
        y_lin = by + bh - int(n * 25)
        pts_linear.append((bx + i, y_lin))
    
    if len(pts_n2) > 1:
        draw.line(pts_n2, fill=(239, 68, 68, 220), width=2)
        draw.text((pts_n2[-1][0] - 25, pts_n2[-1][1] - 12), "O(N²)", font=font_small, fill=(239, 68, 68, 255))
    if len(pts_nlogn) > 1:
        draw.line(pts_nlogn, fill=(52, 211, 153, 255), width=2)
        draw.text((pts_nlogn[-1][0] - 38, pts_nlogn[-1][1] - 12), "O(N log N)", font=font_small, fill=(52, 211, 153, 255))
    if len(pts_linear) > 1:
        draw.line(pts_linear, fill=(56, 189, 248, 180), width=2)
        draw.text((pts_linear[-1][0] - 22, pts_linear[-1][1] - 10), "O(N)", font=font_small, fill=(56, 189, 248, 255))
        
    # Right: Live Code Execution & Profiler Terminal
    tx, ty, tw, th = 310, 75, 220, 130
    draw.rectangle([(tx, ty), (tx + tw, ty + th)], fill=(6, 10, 18, 255), outline=(30, 41, 59, 255), width=1)
    draw.text((tx + 8, ty + 6), "Compiler Runtime Telemetry", font=font_code_sm, fill=(148, 163, 184, 255))
    draw.line([(tx, ty + 20), (tx + tw, ty + 20)], fill=(30, 41, 59, 255), width=1)
    
    draw.text((tx + 10, ty + 28), "STATUS: EXECUTION PASS", font=font_code_sm, fill=(52, 211, 153, 255))
    draw.text((tx + 10, ty + 42), f"Exec Time: {0.012 + (f%4)*0.002:.4f}s", font=font_code_sm, fill=(255, 255, 255, 255))
    draw.text((tx + 10, ty + 56), "Memory Peak: 14.2 MB", font=font_code_sm, fill=(56, 189, 248, 255))
    draw.text((tx + 10, ty + 70), "GC Cycle: 0 paused", font=font_code_sm, fill=(148, 163, 184, 255))
    
    # Animated test bar
    draw.text((tx + 10, ty + 90), f"Test Suite: 10/10 Passed", font=font_code_sm, fill=(52, 211, 153, 255))
    bar_w = int((f / N_FRAMES) * (tw - 24))
    draw.rounded_rectangle([(tx + 10, ty + 106), (tx + tw - 14, ty + 114)], radius=4, fill=(15, 23, 42, 255))
    draw.rounded_rectangle([(tx + 10, ty + 106), (tx + 10 + bar_w, ty + 114)], radius=4, fill=(52, 211, 153, 255))
    
    # Badges
    px = 40
    px = draw_pill(draw, px, 226, "Python 3.12 Engine", (30, 58, 138, 180), (37, 99, 235, 255), (147, 197, 253, 255))
    px = draw_pill(draw, px, 226, "Live Sandbox Compiler", (6, 78, 59, 180), (5, 150, 105, 255), (110, 231, 183, 255))
    px = draw_pill(draw, px, 226, "Vanilla JS + HTML5", (67, 20, 7, 180), (234, 88, 12, 255), (253, 186, 116, 255))
    draw_pill(draw, px, 226, "100% Client-Side", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_3.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_3[0].save("project_skc_tutor.gif", save_all=True, append_images=frames_3[1:], duration=100, loop=0)


# ==============================================================================
# 4. California Housing: Geospatial Regression Fit & Feature Importance
# ==============================================================================
print("Generating 4/6: project_california_housing.gif...")
frames_4 = []

for f in range(N_FRAMES):
    img, draw = create_card_base(
        "CALIFORNIA HOUSING // REGRESSION TELEMETRY",
        "🏠 Geospatial Property Valuation & Feature Impact",
        "Gradient Boosting regression fit with confidence intervals & feature importances",
        "R² = 0.864", (251, 191, 36, 255), (251, 191, 36, 255)
    )
    
    # Left: Regression Scatter & Confidence Interval (width 270)
    sx, sy, sw, sh = 40, 75, 260, 130
    draw.rectangle([(sx, sy), (sx + sw, sy + sh)], fill=(12, 10, 8, 255), outline=(68, 40, 19, 255), width=1)
    draw.text((sx + 8, sy + 6), "Median Income vs House Price ($100k)", font=font_code_sm, fill=(253, 230, 138, 255))
    
    # Axes
    draw.line([(sx + 30, sy + sh - 20), (sx + sw - 10, sy + sh - 20)], fill=(78, 48, 22, 255), width=1)
    draw.line([(sx + 30, sy + 20), (sx + 30, sy + sh - 20)], fill=(78, 48, 22, 255), width=1)
    
    # Scatter points (California census block groups)
    np.random.seed(42)
    sample_x = np.linspace(sx + 35, sx + sw - 20, 36)
    noise = np.sin(sample_x * 0.1) * 8 + np.random.normal(0, 4.5, 36)
    sample_y = (sy + sh - 25) - ((sample_x - sx - 35) / (sw - 55)) * 80 + noise
    
    for px, py in zip(sample_x, sample_y):
        draw.ellipse([(px - 2.5, py - 2.5), (px + 2.5, py + 2.5)], fill=(253, 230, 138, 180))
        
    # Animated Regression Trend Line + Shaded Confidence Band (± 1.96 sigma)
    anim_x_len = int((sw - 55) * ((f + 1) / N_FRAMES))
    x0, y0 = sx + 35, sy + sh - 25
    x1 = x0 + anim_x_len
    y1 = y0 - int((anim_x_len / (sw - 55)) * 80)
    
    # Confidence band polygon
    band_pts = [
        (x0, y0 - 10), (x1, y1 - 10),
        (x1, y1 + 10), (x0, y0 + 10)
    ]
    draw.polygon(band_pts, fill=(245, 158, 11, 40))
    draw.line([(x0, y0), (x1, y1)], fill=(239, 68, 68, 255), width=3)
    
    draw.text((sx + 35, sy + 25), "R²: 0.864", font=font_bold, fill=(251, 191, 36, 255))
    draw.text((sx + 35, sy + 38), "RMSE: $48,210", font=font_small, fill=(253, 230, 138, 255))
    
    # Right: Feature Importance Bar Chart
    fx, fy, fw, fh = 320, 75, 210, 130
    draw.rectangle([(fx, fy), (fx + fw, fy + fh)], fill=(12, 10, 8, 255), outline=(68, 40, 19, 255), width=1)
    draw.text((fx + 8, fy + 6), "Feature Importance (Tree-Based)", font=font_code_sm, fill=(253, 230, 138, 255))
    
    features = [
        ("MedInc", 0.52),
        ("HouseAge", 0.18),
        ("AveRooms", 0.14),
        ("Latitude", 0.10),
        ("Longitude", 0.06),
    ]
    
    for i, (feat, imp) in enumerate(features):
        by = fy + 26 + i * 19
        draw.text((fx + 8, by), feat, font=font_code_sm, fill=(200, 190, 180, 255))
        # Animated filling bar
        bar_len = int((imp / 0.55) * 110 * ((f + 3) / (N_FRAMES + 2)))
        draw.rounded_rectangle([(fx + 75, by + 2), (fx + 75 + bar_len, by + 12)], radius=3, fill=(245, 158, 11, 220))
        draw.text((fx + 78 + bar_len + 4, by), f"{imp*100:.0f}%", font=font_small, fill=(253, 230, 138, 255))
        
    # Badges
    px = 40
    px = draw_pill(draw, px, 226, "Gradient Boosting Regressor", (69, 26, 3, 180), (217, 119, 6, 255), (253, 230, 138, 255))
    px = draw_pill(draw, px, 226, "🗺️ Geospatial Valuation", (59, 7, 100, 180), (126, 34, 206, 255), (233, 213, 255, 255))
    px = draw_pill(draw, px, 226, "Cross-Validated 5-Fold", (28, 25, 23, 180), (120, 113, 108, 255), (245, 245, 244, 255))
    draw_pill(draw, px, 226, "Scikit-Learn", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_4.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_4[0].save("project_california_housing.gif", save_all=True, append_images=frames_4[1:], duration=100, loop=0)


# ==============================================================================
# 5. Deep Learning Projects: TensorBoard Training Loss & Validation Accuracy
# ==============================================================================
print("Generating 5/6: project_deep_learning.gif...")
frames_5 = []

for f in range(N_FRAMES):
    img, draw = create_card_base(
        "DEEP LEARNING // TENSORBOARD DYNAMICS",
        "🤖 Neural Network Training & Convergence Dynamics",
        "Dual-axis tracking: Cross-Entropy loss decay vs Validation Accuracy climb",
        "VAL ACC: 99.2%", (244, 114, 182, 255), (244, 114, 182, 255)
    )
    
    # TensorBoard Canvas
    gx, gy, gw, gh = 40, 75, 490, 130
    draw.rectangle([(gx, gy), (gx + gw, gy + gh)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    
    # Grid lines
    for i in range(5):
        yy = gy + int(i * (gh / 4))
        draw.line([(gx, yy), (gx + gw, yy)], fill=(22, 27, 34, 255), width=1)
    for i in range(6):
        xx = gx + int(i * (gw / 5))
        draw.line([(xx, gy), (xx, gy + gh)], fill=(22, 27, 34, 255), width=1)
        draw.text((xx - 10, gy + gh + 4), f"Ep {i*20}", font=font_small, fill=(110, 118, 129, 255))
        
    # Y axis labels
    draw.text((gx - 30, gy - 2), "Loss", font=font_small, fill=(244, 114, 182, 255))
    draw.text((gx + gw + 4, gy - 2), "Acc %", font=font_small, fill=(52, 211, 153, 255))
    
    # Animated epoch progress
    curr_epoch_len = int(gw * ((f + 1) / N_FRAMES))
    epochs = np.linspace(0, 1, curr_epoch_len)
    
    # 1. Training Loss curve (Exponential decay + realistic noise)
    np.random.seed(101)
    loss_vals = 2.3 * np.exp(-epochs * 4.2) + 0.04 + np.random.normal(0, 0.025, curr_epoch_len) * (1 - epochs * 0.7)
    loss_pts = [(gx + i, gy + int((loss_vals[i] / 2.5) * (gh - 20))) for i in range(curr_epoch_len)]
    
    # 2. Validation Accuracy curve (Sigmoidal climb)
    acc_vals = 0.45 + 0.54 / (1.0 + np.exp(-epochs * 6.5 + 1.8))
    acc_pts = [(gx + i, gy + gh - int((acc_vals[i]) * (gh - 20))) for i in range(curr_epoch_len)]
    
    # Draw curves
    if len(loss_pts) > 1:
        draw.line(loss_pts, fill=(244, 114, 182, 255), width=3)
    if len(acc_pts) > 1:
        draw.line(acc_pts, fill=(52, 211, 153, 255), width=3)
        
    # Current value callout pill on right side of curve
    if curr_epoch_len > 10:
        cur_x = gx + curr_epoch_len - 1
        cur_loss_y = loss_pts[-1][1]
        cur_acc_y = acc_pts[-1][1]
        
        draw.ellipse([(cur_x - 4, cur_loss_y - 4), (cur_x + 4, cur_loss_y + 4)], fill=(244, 114, 182, 255))
        draw.ellipse([(cur_x - 4, cur_acc_y - 4), (cur_x + 4, cur_acc_y + 4)], fill=(52, 211, 153, 255))
        
        # Legend
        draw.rectangle([(gx + 12, gy + 8), (gx + 180, gy + 32)], fill=(13, 17, 23, 220), outline=(48, 54, 61, 255))
        draw.line([(gx + 18, gy + 16), (gx + 32, gy + 16)], fill=(244, 114, 182, 255), width=2)
        draw.text((gx + 36, gy + 11), f"Train Loss: {loss_vals[-1]:.3f}", font=font_code_sm, fill=(244, 114, 182, 255))
        
        draw.line([(gx + 18, gy + 26), (gx + 32, gy + 26)], fill=(52, 211, 153, 255), width=2)
        draw.text((gx + 36, gy + 21), f"Val Acc: {acc_vals[-1]*100:.1f}%", font=font_code_sm, fill=(52, 211, 153, 255))
        
    # Badges
    px = 40
    px = draw_pill(draw, px, 226, "🔥 PyTorch Models", (67, 20, 7, 180), (234, 88, 12, 255), (253, 186, 116, 255))
    px = draw_pill(draw, px, 226, "ResNet + Conv2D", (69, 26, 3, 180), (217, 119, 6, 255), (253, 230, 138, 255))
    px = draw_pill(draw, px, 226, "AdamW + Cosine Decay", (59, 7, 100, 180), (126, 34, 206, 255), (233, 213, 255, 255))
    draw_pill(draw, px, 226, "GPU Accelerated", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_5.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_5[0].save("project_deep_learning.gif", save_all=True, append_images=frames_5[1:], duration=100, loop=0)


# ==============================================================================
# 6. Deep-ML Practice: 2D Loss Surface Contour Map & Gradient Descent Path
# ==============================================================================
print("Generating 6/6: project_deep_ml.gif...")
frames_6 = []

for f in range(N_FRAMES):
    img, draw = create_card_base(
        "ALGORITHMIC FOUNDATIONS // PURE NUMPY",
        "📐 Gradient Descent Trajectory on Loss Surface",
        "Analytical loss surface contours & vectorized optimization trajectory",
        "LOSS -> 0.001", (56, 189, 248, 255), (56, 189, 248, 255)
    )
    
    # Left: 2D Contour Map (width 260)
    cx_box, cy_box, cw_box, ch_box = 40, 75, 260, 130
    draw.rectangle([(cx_box, cy_box), (cx_box + cw_box, cy_box + ch_box)], fill=(6, 18, 30, 255), outline=(7, 89, 133, 255), width=1)
    draw.text((cx_box + 8, cy_box + 6), "Loss Contours J(w₁, w₂) & Descent Path", font=font_code_sm, fill=(56, 189, 248, 255))
    
    # Draw concentric contour ellipses of quadratic bowl: J = (w1 - 1)^2 + 2*(w2 - 1)^2
    center_x, center_y = cx_box + 180, cy_box + 70
    radii = [90, 68, 48, 32, 18, 8]
    colors_contour = [(7, 89, 133), (12, 74, 110), (14, 116, 144), (6, 148, 162), (13, 148, 136), (16, 185, 129)]
    
    for r, col in zip(radii, colors_contour):
        draw.ellipse([(center_x - r * 1.5, center_y - r), (center_x + r * 1.5, center_y + r)], outline=col + (200,), width=1)
        
    # Animated descent trajectory (stepping from top-left into center minimum)
    t_steps = 14
    curr_step = int((f / N_FRAMES) * t_steps)
    traj_pts = []
    
    start_x, start_y = cx_box + 25, cy_box + 20
    for s in range(t_steps):
        alpha = s / t_steps
        # Spiral decay towards minimum with momentum oscillations
        px = start_x + (center_x - start_x) * (1.0 - math.exp(-s * 0.35)) + math.sin(s * 1.8) * 8 * (1.0 - alpha)
        py = start_y + (center_y - start_y) * (1.0 - math.exp(-s * 0.35)) + math.cos(s * 1.8) * 6 * (1.0 - alpha)
        traj_pts.append((px, py))
        
    # Draw path up to current step
    active_pts = traj_pts[:curr_step + 1]
    if len(active_pts) > 1:
        draw.line(active_pts, fill=(239, 68, 68, 255), width=2)
        for pt in active_pts[:-1]:
            draw.ellipse([(pt[0] - 2, pt[1] - 2), (pt[0] + 2, pt[1] + 2)], fill=(253, 230, 138, 255))
        # Head point
        hx, hy = active_pts[-1]
        draw.ellipse([(hx - 5, hy - 5), (hx + 5, hy + 5)], fill=(255, 255, 255, 255), outline=(239, 68, 68, 255), width=2)
        
    draw.text((center_x - 14, center_y - 6), "Min", font=font_small, fill=(52, 211, 153, 255))
    
    # Right: Formula & Vectorized Proof Board
    tx, ty, tw, th = 320, 75, 210, 130
    draw.rectangle([(tx, ty), (tx + tw, ty + th)], fill=(4, 14, 24, 255), outline=(7, 89, 133, 255), width=1)
    draw.text((tx + 8, ty + 6), "Vectorized NumPy Derivations", font=font_code_sm, fill=(56, 189, 248, 255))
    draw.line([(tx, ty + 20), (tx + tw, ty + 20)], fill=(7, 89, 133, 255), width=1)
    
    # Math formulas
    draw.text((tx + 10, ty + 28), "θ_next := θ - α · ∇J(θ)", font=font_code, fill=(74, 222, 128, 255))
    draw.text((tx + 10, ty + 46), "dW = (1/m) · X.T @ (A - Y)", font=font_code_sm, fill=(244, 114, 182, 255))
    draw.text((tx + 10, ty + 62), "db = (1/m) · sum(dZ, axis=1)", font=font_code_sm, fill=(253, 224, 71, 255))
    draw.text((tx + 10, ty + 78), "V_dW = β·V_dW + (1-β)·dW", font=font_code_sm, fill=(125, 211, 252, 255))
    
    # Live iteration indicator
    cur_loss = 1.45 * math.exp(-curr_step * 0.3) + 0.001
    draw.text((tx + 10, ty + 100), f"Step {curr_step*10:03d} | Loss: {cur_loss:.4f}", font=font_code_sm, fill=(52, 211, 153, 255))
    
    # Badges
    px = 40
    px = draw_pill(draw, px, 226, "Vectorized Matrix Math", (12, 74, 110, 180), (2, 132, 199, 255), (186, 230, 253, 255))
    px = draw_pill(draw, px, 226, "Zero Frameworks (NumPy)", (20, 83, 45, 180), (22, 163, 74, 255), (187, 247, 208, 255))
    px = draw_pill(draw, px, 226, "Theoretical Proofs", (30, 27, 75, 180), (67, 56, 202, 255), (199, 210, 254, 255))
    draw_pill(draw, px, 226, "Backpropagation", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_6.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_6[0].save("project_deep_ml.gif", save_all=True, append_images=frames_6[1:], duration=100, loop=0)

print("SUCCESS: All 6 realistic ML visualizations generated and saved!")
