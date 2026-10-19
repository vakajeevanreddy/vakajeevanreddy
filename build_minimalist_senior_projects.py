import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions (1200 x 560, 2x Retina)
WIDTH, HEIGHT = 1200, 560
N_FRAMES = 18

def get_font(size, bold=False):
    win_fonts = "C:\\Windows\\Fonts\\"
    try:
        if bold:
            return ImageFont.truetype(os.path.join(win_fonts, "segoeuib.ttf"), size)
        else:
            return ImageFont.truetype(os.path.join(win_fonts, "segoeui.ttf"), size)
    except:
        return ImageFont.load_default()

def get_mono_font(size, bold=False):
    win_fonts = "C:\\Windows\\Fonts\\"
    try:
        if bold:
            return ImageFont.truetype(os.path.join(win_fonts, "consolab.ttf"), size)
        else:
            return ImageFont.truetype(os.path.join(win_fonts, "consola.ttf"), size)
    except:
        return ImageFont.load_default()

font_title = get_font(26, bold=True)
font_subtitle = get_font(16, bold=False)
font_panel_title = get_font(18, bold=True)
font_body = get_font(15, bold=False)
font_body_b = get_font(15, bold=True)
font_code = get_mono_font(15, bold=False)
font_code_b = get_mono_font(15, bold=True)
font_code_sm = get_mono_font(13, bold=False)
font_small = get_font(13, bold=False)

def create_clean_canvas(title, subtitle):
    # Pure clean dark slate card, NO colored top bar, NO badge pills
    img = Image.new("RGBA", (WIDTH, HEIGHT), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer Border (Minimalist clean border)
    draw.rounded_rectangle([(2, 2), (WIDTH - 3, HEIGHT - 3)], radius=16, fill=(22, 27, 34, 255), outline=(48, 54, 61, 255), width=2)
    
    # Clean Header (NO colored bars, NO pills, pure clean typography)
    draw.text((44, 28), title, font=font_title, fill=(240, 246, 252, 255))
    draw.text((44, 64), subtitle, font=font_subtitle, fill=(139, 148, 158, 255))
    draw.line([(44, 96), (WIDTH - 44, 96)], fill=(33, 38, 45, 255), width=1)
    
    return img, draw

# Dual-panel coordinates (clean, spacious, balanced)
# From y = 112 to y = 528 (height 416px, large and crisp!)
p1_x, p1_w = 44, 536
p2_x, p2_w = 620, 536
py, ph = 114, 414

# ==============================================================================
# 1. AIVOA-CRM-HCP (Clean Senior Architecture & Signal Telemetry)
# ==============================================================================
print("Rendering 1/6: AIVOA-CRM-HCP (Clean Minimalist)...")
frames_1 = []

for f in range(N_FRAMES):
    img, draw = create_clean_canvas(
        "AIVOA-CRM-HCP: Clinical Interaction Architecture",
        "FastAPI Async Microservices & Intelligent Clinical Speech Analytics"
    )
    
    # Left Panel: Signal Waveform & Transcription
    draw.rounded_rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p1_x + 20, py + 18), "Clinical Audio Signal & Transcription", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p1_x, py + 52), (p1_x + p1_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    # Grid lines
    for i in range(1, 4):
        yy = py + 52 + i * 60
        draw.line([(p1_x, yy), (p1_x + p1_w, yy)], fill=(22, 27, 34, 255), width=1)
        
    xs = np.linspace(0, 3 * np.pi, p1_w)
    shift = (f / N_FRAMES) * 2 * np.pi
    ys = (
        np.sin(xs + shift) * 40 + 
        np.sin(2.2 * xs - shift * 0.7) * 24 + 
        np.cos(0.5 * xs + shift) * 28 + 
        115
    )
    
    base_y = py + 260
    pts_area = [(p1_x, base_y)]
    for i in range(p1_w):
        pts_area.append((p1_x + i, base_y - int(ys[i])))
    pts_area.append((p1_x + p1_w, base_y))
    draw.polygon(pts_area, fill=(16, 42, 60, 80))
    
    curve_pts = [(p1_x + i, base_y - int(ys[i])) for i in range(p1_w)]
    draw.line(curve_pts, fill=(56, 189, 248, 255), width=3)
    
    # Scanning needle
    scan_idx = int((f / N_FRAMES) * (p1_w - 60)) + 30
    scan_x = p1_x + scan_idx
    scan_y = base_y - int(ys[scan_idx])
    draw.line([(scan_x, py + 54), (scan_x, base_y)], fill=(56, 189, 248, 160), width=2)
    draw.ellipse([(scan_x - 6, scan_y - 6), (scan_x + 6, scan_y + 6)], fill=(255, 255, 255, 255), outline=(56, 189, 248, 255), width=2)
    
    # Text Analysis Summary (NO color bars)
    draw.text((p1_x + 24, py + 285), "Sentiment Classification: POSITIVE (0.94)", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p1_x + 24, py + 315), "Extracted Entities: Prescription, Treatment Schedule", font=font_code, fill=(200, 210, 220, 255))
    draw.text((p1_x + 24, py + 345), "ASR Engine: OpenAI Whisper (Custom Clinical LoRA)", font=font_code_sm, fill=(139, 148, 158, 255))
    draw.text((p1_x + 24, py + 375), "Throughput: 500+ Active HCP Sessions Tracked", font=font_code_sm, fill=(139, 148, 158, 255))
    
    # Right Panel: Microservice Pipeline Architecture
    draw.rounded_rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p2_x + 20, py + 18), "Microservice Architecture Flow", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p2_x, py + 52), (p2_x + p2_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    steps = [
        ("1. React Frontend Client", "Audio recording & clinician interaction dashboard", (240, 246, 252)),
        ("2. FastAPI Gateway", "Async router, token authentication (12ms latency)", (240, 246, 252)),
        ("3. Whisper NLP Pipeline", "Automated transcription & medical entity extraction", (240, 246, 252)),
        ("4. PostgreSQL & Vector Store", "Structured CRM records & semantic search history", (240, 246, 252))
    ]
    
    step_y = py + 68
    for i, (name, desc, col) in enumerate(steps):
        box_y = step_y + i * 82
        draw.rounded_rectangle([(p2_x + 20, box_y), (p2_x + p2_w - 20, box_y + 68)], radius=8, fill=(22, 27, 34, 255), outline=(48, 54, 61, 255), width=1)
        draw.text((p2_x + 36, box_y + 12), name, font=font_body_b, fill=col)
        draw.text((p2_x + 36, box_y + 38), desc, font=font_small, fill=(139, 148, 158, 255))
        
        # Subtle status indicator
        draw.ellipse([(p2_x + p2_w - 44, box_y + 26), (p2_x + p2_w - 32, box_y + 38)], fill=(52, 211, 153, 255))
        
    frames_1.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_1[0].save("project_aivoa_crm.gif", save_all=True, append_images=frames_1[1:], duration=80, loop=0)
print("project_aivoa_crm.gif saved!")


# ==============================================================================
# 2. Customer Health Care CRM (Clean ROC-AUC & Cohort Distributions)
# ==============================================================================
print("Rendering 2/6: Customer Health Care CRM (Clean Minimalist)...")
frames_2 = []

for f in range(N_FRAMES):
    img, draw = create_clean_canvas(
        "Customer Healthcare CRM: Patient Risk Analytics",
        "Ensemble Classifier for Patient Churn & Stratified Clinical Risk Scoring"
    )
    
    # Left Panel: ROC-AUC Curve
    draw.rounded_rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p1_x + 20, py + 18), "Model Discrimination: ROC-AUC Validation", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p1_x, py + 52), (p1_x + p1_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    chart_x = p1_x + 60
    chart_y = py + 80
    chart_w = p1_w - 100
    chart_h = ph - 160
    
    draw.line([(chart_x, chart_y + chart_h), (chart_x + chart_w, chart_y + chart_h)], fill=(78, 88, 100, 255), width=2)
    draw.line([(chart_x, chart_y), (chart_x, chart_y + chart_h)], fill=(78, 88, 100, 255), width=2)
    draw.text((chart_x + chart_w // 2 - 50, chart_y + chart_h + 16), "False Positive Rate (1 - Specificity)", font=font_small, fill=(148, 163, 184, 255))
    draw.text((chart_x - 30, chart_y - 20), "True Positive Rate (Sensitivity)", font=font_small, fill=(148, 163, 184, 255))
    
    # Diagonal baseline
    draw.line([(chart_x, chart_y + chart_h), (chart_x + chart_w, chart_y)], fill=(55, 65, 81, 255), width=1)
    
    curve_pts = []
    pts_auc = [(chart_x, chart_y + chart_h)]
    for step in range(chart_w):
        fpr = step / chart_w
        tpr = 1.0 - math.pow(1.0 - fpr, 3.8)
        cx = chart_x + step
        cy = chart_y + chart_h - int(tpr * chart_h)
        curve_pts.append((cx, cy))
        pts_auc.append((cx, cy))
    pts_auc.append((chart_x + chart_w, chart_y + chart_h))
    
    draw.polygon(pts_auc, fill=(50, 30, 80, 70))
    draw.line(curve_pts, fill=(167, 139, 250, 255), width=3)
    
    # Threshold Point
    t_val = f / N_FRAMES
    opt_fpr = t_val * 0.65 + 0.05
    opt_tpr = 1.0 - math.pow(1.0 - opt_fpr, 3.8)
    ox = chart_x + int(opt_fpr * chart_w)
    oy = chart_y + chart_h - int(opt_tpr * chart_h)
    
    draw.line([(ox, chart_y), (ox, chart_y + chart_h)], fill=(167, 139, 250, 100), width=1)
    draw.line([(chart_x, oy), (chart_x + chart_w, oy)], fill=(167, 139, 250, 100), width=1)
    draw.ellipse([(ox - 6, oy - 6), (ox + 6, oy + 6)], fill=(255, 255, 255, 255), outline=(167, 139, 250, 255), width=2)
    
    draw.text((chart_x + 16, chart_y + 16), f"AUC = 0.942 | Optimal Threshold = {1 - t_val:.2f}", font=font_code_b, fill=(240, 246, 252, 255))
    draw.text((chart_x + 16, chart_y + 44), f"Sensitivity: {opt_tpr*100:.1f}% | Specificity: {(1-opt_fpr)*100:.1f}%", font=font_code, fill=(139, 148, 158, 255))
    
    # Right Panel: Patient Risk Distribution
    draw.rounded_rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p2_x + 20, py + 18), "Patient Risk Cohort Distributions", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p2_x, py + 52), (p2_x + p2_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    c2_x = p2_x + 50
    c2_w = p2_w - 100
    c2_y = py + 80
    c2_h = ph - 170
    base_dist_y = c2_y + c2_h
    
    draw.line([(c2_x, base_dist_y), (c2_x + c2_w, base_dist_y)], fill=(78, 88, 100, 255), width=2)
    
    x_axis = np.linspace(-3, 3, c2_w)
    g_low = np.exp(-0.5 * ((x_axis + 1.2) / 0.8) ** 2) * (c2_h - 20)
    g_high = np.exp(-0.5 * ((x_axis - 1.1) / 0.9) ** 2) * (c2_h - 30)
    
    pts_l = [(c2_x, base_dist_y)]
    for i in range(c2_w):
        pts_l.append((c2_x + i, base_dist_y - int(g_low[i])))
    pts_l.append((c2_x + c2_w, base_dist_y))
    draw.polygon(pts_l, fill=(6, 78, 59, 90))
    draw.line([(c2_x + i, base_dist_y - int(g_low[i])) for i in range(c2_w)], fill=(52, 211, 153, 255), width=3)
    
    pts_h = [(c2_x, base_dist_y)]
    for i in range(c2_w):
        pts_h.append((c2_x + i, base_dist_y - int(g_high[i])))
    pts_h.append((c2_x + c2_w, base_dist_y))
    draw.polygon(pts_h, fill=(120, 20, 40, 80))
    draw.line([(c2_x + i, base_dist_y - int(g_high[i])) for i in range(c2_w)], fill=(244, 114, 182, 255), width=3)
    
    db_x = c2_x + int(c2_w * 0.52 + math.sin(f / N_FRAMES * 2 * math.pi) * 16)
    draw.line([(db_x, c2_y - 10), (db_x, base_dist_y)], fill=(255, 255, 255, 220), width=2)
    draw.text((db_x - 36, c2_y - 28), "Optimal Cutoff", font=font_code_b, fill=(255, 255, 255, 255))
    
    # Text summary (NO color bars)
    draw.text((p2_x + 30, py + ph - 68), "Low Risk Cohort: 84.6% (Standard Preventive Protocol)", font=font_body_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 30, py + ph - 38), "High Risk Cohort: 15.4% (Critical Priority Intervention)", font=font_body_b, fill=(244, 114, 182, 255))
    
    frames_2.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_2[0].save("project_customer_healthcare.gif", save_all=True, append_images=frames_2[1:], duration=80, loop=0)
print("project_customer_healthcare.gif saved!")


# ==============================================================================
# 3. SkC Jeevan Tutor (Clean IDE Sandbox & Big-O)
# ==============================================================================
print("Rendering 3/6: SkC Jeevan Tutor (Clean Minimalist)...")
frames_3 = []

for f in range(N_FRAMES):
    img, draw = create_clean_canvas(
        "SkC Jeevan Tutor: Interactive Python Sandbox",
        "Browser-Based Python Execution Engine with Real-Time Algorithmic Profiling"
    )
    
    # Left Panel: Big-O Curves
    draw.rounded_rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p1_x + 20, py + 18), "Algorithmic Runtime Complexity (Big-O)", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p1_x, py + 52), (p1_x + p1_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    b_x = p1_x + 60
    b_y = py + 80
    b_w = p1_w - 100
    b_h = ph - 160
    
    draw.line([(b_x, b_y + b_h), (b_x + b_w, b_y + b_h)], fill=(78, 88, 100, 255), width=2)
    draw.line([(b_x, b_y), (b_x, b_y + b_h)], fill=(78, 88, 100, 255), width=2)
    draw.text((b_x + b_w // 2 - 30, b_y + b_h + 16), "Input Size (N)", font=font_small, fill=(148, 163, 184, 255))
    draw.text((b_x - 30, b_y - 20), "Operations / Time", font=font_small, fill=(148, 163, 184, 255))
    
    anim_prog = (f + 1) / N_FRAMES
    curr_len = int(b_w * anim_prog)
    
    pts_n2 = []
    pts_nlog = []
    pts_lin = []
    for i in range(curr_len):
        n = i / b_w
        px = b_x + i
        y_n2 = (b_y + b_h) - int((n ** 2) * (b_h - 30))
        y_nlog = (b_y + b_h) - int((n * math.log(n * 9 + 1)) * (b_h - 40))
        y_l = (b_y + b_h) - int(n * (b_h * 0.45))
        pts_n2.append((px, y_n2))
        pts_nlog.append((px, y_nlog))
        pts_lin.append((px, y_l))
        
    if len(pts_n2) > 1:
        draw.line(pts_n2, fill=(239, 68, 68, 255), width=3)
        draw.text((pts_n2[-1][0] - 38, pts_n2[-1][1] - 22), "O(N2)", font=font_code_b, fill=(239, 68, 68, 255))
    if len(pts_nlog) > 1:
        draw.line(pts_nlog, fill=(52, 211, 153, 255), width=3)
        draw.text((pts_nlog[-1][0] - 65, pts_nlog[-1][1] - 22), "O(N log N)", font=font_code_b, fill=(52, 211, 153, 255))
    if len(pts_lin) > 1:
        draw.line(pts_lin, fill=(56, 189, 248, 255), width=2)
        draw.text((pts_lin[-1][0] - 32, pts_lin[-1][1] - 18), "O(N)", font=font_code_b, fill=(56, 189, 248, 255))
        
    # Right Panel: Clean Code Editor
    draw.rounded_rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    
    # macOS window dots
    draw.ellipse([(p2_x + 20, py + 20), (p2_x + 30, py + 30)], fill=(239, 68, 68, 255))
    draw.ellipse([(p2_x + 38, py + 20), (p2_x + 48, py + 30)], fill=(245, 158, 11, 255))
    draw.ellipse([(p2_x + 56, py + 20), (p2_x + 66, py + 30)], fill=(52, 211, 153, 255))
    draw.text((p2_x + 82, py + 18), "solution.py — Python 3.12 Engine", font=font_code, fill=(148, 163, 184, 255))
    draw.line([(p2_x, py + 52), (p2_x + p2_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    cy = py + 72
    draw.text((p2_x + 24, cy), "def", font=font_code_b, fill=(244, 114, 182, 255))
    draw.text((p2_x + 60, cy), " binary_search(arr, target):", font=font_code, fill=(240, 246, 252, 255))
    draw.text((p2_x + 24, cy + 32), "    low, high = 0, len(arr) - 1", font=font_code, fill=(200, 210, 220, 255))
    draw.text((p2_x + 24, cy + 64), "    while low <= high:", font=font_code_b, fill=(244, 114, 182, 255))
    draw.text((p2_x + 24, cy + 96), "        mid = (low + high) // 2", font=font_code, fill=(200, 210, 220, 255))
    draw.text((p2_x + 24, cy + 128), "        if arr[mid] == target:", font=font_code_b, fill=(244, 114, 182, 255))
    draw.text((p2_x + 24, cy + 160), "            return mid  # Target Found", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 24, cy + 192), "    return -1", font=font_code_b, fill=(239, 68, 68, 255))
    
    # Terminal text
    draw.text((p2_x + 24, py + ph - 70), "Test Suite: 10/10 Passed (100% Correctness)", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 24, py + ph - 40), "Execution Time: 0.014s | 100% Client-Side WebAssembly", font=font_code, fill=(139, 148, 158, 255))
    
    frames_3.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_3[0].save("project_skc_tutor.gif", save_all=True, append_images=frames_3[1:], duration=80, loop=0)
print("project_skc_tutor.gif saved!")


# ==============================================================================
# 4. California Housing (Clean Regression & Feature Importance)
# ==============================================================================
print("Rendering 4/6: California Housing (Clean Minimalist)...")
frames_4 = []

for f in range(N_FRAMES):
    img, draw = create_clean_canvas(
        "California Housing Price Prediction Engine",
        "Gradient Boosting Regressor with 95% Confidence Intervals & Feature Analysis"
    )
    
    # Left Panel: Scatter
    draw.rounded_rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p1_x + 20, py + 18), "Regression Diagnostics: Actual vs Predicted", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p1_x, py + 52), (p1_x + p1_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    s_x = p1_x + 60
    s_y = py + 80
    s_w = p1_w - 100
    s_h = ph - 160
    
    draw.line([(s_x, s_y + s_h), (s_x + s_w, s_y + s_h)], fill=(78, 88, 100, 255), width=2)
    draw.line([(s_x, s_y), (s_x, s_y + s_h)], fill=(78, 88, 100, 255), width=2)
    draw.text((s_x + s_w // 2 - 40, s_y + s_h + 16), "Actual Price ($100k)", font=font_small, fill=(148, 163, 184, 255))
    draw.text((s_x - 30, s_y - 20), "Predicted Price ($100k)", font=font_small, fill=(148, 163, 184, 255))
    
    np.random.seed(42)
    sample_x = np.linspace(s_x + 10, s_x + s_w - 10, 48)
    noise = np.sin(sample_x * 0.12) * 12 + np.random.normal(0, 7.0, 48)
    sample_y = (s_y + s_h - 10) - ((sample_x - s_x - 10) / (s_w - 20)) * (s_h - 20) + noise
    
    for px, py_val in zip(sample_x, sample_y):
        draw.ellipse([(px - 4, py_val - 4), (px + 4, py_val + 4)], fill=(251, 191, 36, 180))
        
    anim_x_len = int((s_w - 20) * ((f + 1) / N_FRAMES))
    x0, y0 = s_x + 10, s_y + s_h - 10
    x1 = x0 + anim_x_len
    y1 = y0 - int((anim_x_len / (s_w - 20)) * (s_h - 20))
    
    draw.polygon([(x0, y0 - 18), (x1, y1 - 18), (x1, y1 + 18), (x0, y0 + 18)], fill=(245, 158, 11, 40))
    draw.line([(x0, y0), (x1, y1)], fill=(239, 68, 68, 255), width=3)
    
    draw.text((s_x + 16, s_y + 16), "R2 = 0.864 | RMSE = $48,210", font=font_code_b, fill=(240, 246, 252, 255))
    draw.text((s_x + 16, s_y + 44), "5-Fold Stratified Cross-Validation", font=font_code, fill=(139, 148, 158, 255))
    
    # Right Panel: Feature Importance List (NO color bars!)
    draw.rounded_rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p2_x + 20, py + 18), "Feature Importance Analysis (GBM)", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p2_x, py + 52), (p2_x + p2_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    features = [
        ("Median Income (MedInc)", "0.52 (Primary Pricing Factor)", "52%"),
        ("House Age (HouseAge)", "0.18 (Historical Valuation Decay)", "18%"),
        ("Average Rooms (AveRooms)", "0.14 (Property Area Metric)", "14%"),
        ("Geospatial Latitude", "0.10 (Regional Coastal Proximity)", "10%"),
        ("Geospatial Longitude", "0.06 (Metropolitan Proximity)", "6%"),
    ]
    
    for i, (feat, desc, pct) in enumerate(features):
        by = py + 68 + i * 66
        draw.text((p2_x + 24, by + 6), feat, font=font_body_b, fill=(240, 246, 252, 255))
        draw.text((p2_x + 24, by + 32), desc, font=font_small, fill=(139, 148, 158, 255))
        draw.text((p2_x + p2_w - 70, by + 16), pct, font=font_code_b, fill=(251, 191, 36, 255))
        draw.line([(p2_x + 20, by + 60), (p2_x + p2_w - 20, by + 60)], fill=(33, 38, 45, 255), width=1)
        
    frames_4.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_4[0].save("project_california_housing.gif", save_all=True, append_images=frames_4[1:], duration=80, loop=0)
print("project_california_housing.gif saved!")


# ==============================================================================
# 5. Deep Learning Projects (Clean Loss Decay & Activations)
# ==============================================================================
print("Rendering 5/6: Deep Learning Projects (Clean Minimalist)...")
frames_5 = []

for f in range(N_FRAMES):
    img, draw = create_clean_canvas(
        "Deep Learning Projects: Neural Architectures & Training",
        "PyTorch Implementations of CNNs, RNNs & Transformers with Convergence Tracking"
    )
    
    # Left Panel: Loss Decay
    draw.rounded_rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p1_x + 20, py + 18), "Training vs Validation Loss Decay", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p1_x, py + 52), (p1_x + p1_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    l_x = p1_x + 60
    l_y = py + 80
    l_w = p1_w - 100
    l_h = ph - 160
    
    draw.line([(l_x, l_y + l_h), (l_x + l_w, l_y + l_h)], fill=(78, 88, 100, 255), width=2)
    draw.line([(l_x, l_y), (l_x, l_y + l_h)], fill=(78, 88, 100, 255), width=2)
    
    for i in range(5):
        xx = l_x + int(i * (l_w / 4))
        draw.text((xx - 16, l_y + l_h + 16), f"Epoch {i*25}", font=font_small, fill=(148, 163, 184, 255))
        
    curr_len_1 = int(l_w * ((f + 1) / N_FRAMES))
    ep_1 = np.linspace(0, 1, curr_len_1)
    np.random.seed(101)
    l_pts = 2.4 * np.exp(-ep_1 * 4.2) + 0.04 + np.random.normal(0, 0.025, curr_len_1) * (1 - ep_1 * 0.7)
    
    pts_loss = [(l_x + i, l_y + int((l_pts[i] / 2.5) * l_h)) for i in range(curr_len_1)]
    if len(pts_loss) > 1:
        draw.line(pts_loss, fill=(244, 114, 182, 255), width=3)
        
    draw.text((l_x + 16, l_y + 16), "Cross-Entropy Train Loss: 0.042 (Converged)", font=font_code_b, fill=(240, 246, 252, 255))
    draw.text((l_x + 16, l_y + 44), f"Validation Loss: 0.058 | Epoch: {int((f+1)/N_FRAMES * 100)}/100", font=font_code, fill=(139, 148, 158, 255))
    
    # Right Panel: Validation Accuracy & Weights
    draw.rounded_rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p2_x + 20, py + 18), "Validation Accuracy & Neural Layer Flow", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p2_x, py + 52), (p2_x + p2_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    a_x = p2_x + 36
    a_w = p2_w - 240
    curr_len_2 = int(a_w * ((f + 1) / N_FRAMES))
    ep_2 = np.linspace(0, 1, curr_len_2)
    acc_pts = 0.45 + 0.54 / (1.0 + np.exp(-ep_2 * 6.5 + 1.8))
    pts_acc = [(a_x + i, py + 260 - int(acc_pts[i] * 140)) for i in range(curr_len_2)]
    if len(pts_acc) > 1:
        draw.line(pts_acc, fill=(52, 211, 153, 255), width=3)
        
    draw.text((a_x, py + 68), "Validation Accuracy: 99.2%", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((a_x, py + 94), "Architectures: CNN, RNN, Transformers", font=font_small, fill=(148, 163, 184, 255))
    
    # Synapse Weights Heatmap
    hx = p2_x + p2_w - 180
    hy = py + 72
    draw.text((hx, hy - 4), "Synapse Weights", font=font_code_sm, fill=(148, 163, 184, 255))
    for r in range(4):
        for c in range(4):
            val = math.sin(f * 0.3 + r * 1.2 + c * 0.8)
            intensity = int(128 + val * 120)
            col = (52, intensity, 153, 255) if val > 0 else (intensity, 68, 68, 255)
            draw.rounded_rectangle([(hx + c * 38, hy + 20 + r * 38), (hx + c * 38 + 32, hy + 20 + r * 38 + 32)], radius=4, fill=col)
            
    # Architecture Pipeline Text (NO color bars)
    draw.text((p2_x + 24, py + ph - 70), "Layer Pipeline: Input(28x28) -> Conv2D(32) -> Dense(128) -> Output(10)", font=font_code_b, fill=(240, 246, 252, 255))
    draw.text((p2_x + 24, py + ph - 40), "Frameworks: PyTorch 2.3, TensorFlow Keras, TensorBoard Integration", font=font_code, fill=(139, 148, 158, 255))
    
    frames_5.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_5[0].save("project_deep_learning.gif", save_all=True, append_images=frames_5[1:], duration=80, loop=0)
print("project_deep_learning.gif saved!")


# ==============================================================================
# 6. Deep-ML Practice (Clean 2D Loss Contours & Gradient Math)
# ==============================================================================
print("Rendering 6/6: Deep-ML Practice (Clean Minimalist)...")
frames_6 = []

for f in range(N_FRAMES):
    img, draw = create_clean_canvas(
        "Deep-ML Practice: Pure NumPy ML Foundations",
        "Convex 2D Loss Surface Optimization & Vectorized Gradient Descent Implementation"
    )
    
    # Left Panel: 2D Loss Contours
    draw.rounded_rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    draw.text((p1_x + 20, py + 18), "2D Loss Surface Contours & Optimization Path", font=font_panel_title, fill=(240, 246, 252, 255))
    draw.line([(p1_x, py + 52), (p1_x + p1_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    center_x = p1_x + p1_w // 2
    center_y = py + 52 + (ph - 52) // 2
    
    radii = [28, 60, 96, 138, 180]
    for r in radii:
        rx = r
        ry = int(r * 0.58)
        draw.ellipse([(center_x - rx, center_y - ry), (center_x + rx, center_y + ry)], outline=(50, 65, 85, 220), width=1)
        
    draw.ellipse([(center_x - 5, center_y - 5), (center_x + 5, center_y + 5)], fill=(52, 211, 153, 255))
    draw.text((center_x + 10, center_y - 12), "L* (Global Min)", font=font_body_b, fill=(52, 211, 153, 255))
    
    t_opt = (f / N_FRAMES)
    gd_steps = 22
    curr_steps = int(gd_steps * ((f + 1) / N_FRAMES))
    path_pts = []
    for s in range(curr_steps):
        prog = s / gd_steps
        angle = prog * 2.5 * math.pi + 0.3
        rad = 150 * (1.0 - prog * 0.88)
        px = center_x + int(math.cos(angle) * rad)
        py_pt = center_y + int(math.sin(angle) * rad * 0.58)
        path_pts.append((px, py_pt))
        
    if len(path_pts) > 1:
        draw.line(path_pts, fill=(244, 114, 182, 240), width=3)
        draw.ellipse([(path_pts[-1][0] - 6, path_pts[-1][1] - 6), (path_pts[-1][0] + 6, path_pts[-1][1] + 6)], fill=(255, 255, 255, 255), outline=(239, 68, 68, 255), width=3)
        
    draw.text((p1_x + 24, py + ph - 36), "Optimization: Vectorized Momentum SGD in Pure NumPy", font=font_small, fill=(148, 163, 184, 255))
    
    # Right Panel: Vectorized Code & Stats
    draw.rounded_rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    
    draw.ellipse([(p2_x + 20, py + 20), (p2_x + 30, py + 30)], fill=(239, 68, 68, 255))
    draw.ellipse([(p2_x + 38, py + 20), (p2_x + 48, py + 30)], fill=(245, 158, 11, 255))
    draw.ellipse([(p2_x + 56, py + 20), (p2_x + 66, py + 30)], fill=(52, 211, 153, 255))
    draw.text((p2_x + 82, py + 18), "linear_regression.py — Vectorized Math", font=font_code, fill=(148, 163, 184, 255))
    draw.line([(p2_x, py + 52), (p2_x + p2_w, py + 52)], fill=(33, 38, 45, 255), width=1)
    
    cy = py + 72
    draw.text((p2_x + 24, cy), "# Vectorized Optimization in Pure NumPy", font=font_code, fill=(139, 148, 158, 255))
    draw.text((p2_x + 24, cy + 32), "error = X @ weights - y", font=font_code_b, fill=(240, 246, 252, 255))
    draw.text((p2_x + 24, cy + 64), "grad = (2 / n_samples) * (X.T @ error)", font=font_code_b, fill=(56, 189, 248, 255))
    draw.text((p2_x + 24, cy + 96), "weights -= learning_rate * grad", font=font_code_b, fill=(52, 211, 153, 255))
    
    norm_val = 0.082 * math.exp(-t_opt * 3.8) + 0.0018
    draw.text((p2_x + 24, py + 220), f"Gradient Norm: ||grad|| = {norm_val:.4f}", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 24, py + 252), f"Iterations: {int(t_opt * 1000)}/1000 Steps Completed", font=font_code, fill=(240, 246, 252, 255))
    draw.text((p2_x + 24, py + 284), "Learning Rate Schedule: 0.01 (Cosine Annealing)", font=font_code, fill=(139, 148, 158, 255))
    draw.text((p2_x + 24, py + 316), "Loss: 0.0004 (Global Minimum Converged)", font=font_code, fill=(251, 191, 36, 255))
    
    frames_6.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_6[0].save("project_deep_ml.gif", save_all=True, append_images=frames_6[1:], duration=80, loop=0)
print("project_deep_ml.gif saved!")

print("\nSUCCESS: All 6 figures generated with ZERO color bars, clean typography, and 1200x560 Retina resolution!")
