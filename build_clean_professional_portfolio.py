import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions
WIDTH, HEIGHT = 600, 270
N_FRAMES = 24

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

font_title = get_font(13, bold=True)
font_subtitle = get_font(10, bold=False)
font_bold = get_font(10, bold=True)
font_small = get_font(9, bold=False)
font_code = get_mono_font(9, bold=False)
font_code_b = get_mono_font(9, bold=True)
font_code_s = get_mono_font(8, bold=False)

def draw_pill(draw, x, y, text, bg_col, border_col, txt_col):
    bbox = font_small.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad_h, pad_v = 8, 4
    w = tw + pad_h * 2
    h = th + pad_v * 2
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=4, fill=bg_col, outline=border_col, width=1)
    draw.text((x + pad_h, y + pad_v - 1), text, font=font_small, fill=txt_col)
    return x + w + 8

def create_base_canvas(tag, title, subtitle, status_txt, tag_col, status_col):
    img = Image.new("RGBA", (WIDTH, HEIGHT), (10, 14, 20, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer Border
    draw.rounded_rectangle([(1, 1), (WIDTH - 2, HEIGHT - 2)], radius=12, fill=(13, 17, 23, 255), outline=(48, 54, 61, 255), width=1)
    
    # Top Bar Header Background
    draw.rounded_rectangle([(1, 1), (WIDTH - 2, 30)], radius=12, fill=(22, 27, 34, 255))
    draw.rectangle([(1, 20), (WIDTH - 2, 30)], fill=(22, 27, 34, 255))
    draw.line([(1, 30), (WIDTH - 2, 30)], fill=(48, 54, 61, 255), width=1)
    
    # Header tag pill
    bbox_tag = font_code_b.getbbox(tag)
    tag_w = (bbox_tag[2] - bbox_tag[0]) + 16
    draw.rounded_rectangle([(24, 6), (24 + tag_w, 24)], radius=4, fill=(tag_col[0], tag_col[1], tag_col[2], 40), outline=tag_col, width=1)
    draw.text((32, 8), tag, font=font_code_b, fill=tag_col)
    
    # Status indicator dot
    draw.ellipse([(WIDTH - 110, 13), (WIDTH - 104, 19)], fill=status_col)
    draw.text((WIDTH - 98, 9), status_txt, font=font_code_b, fill=status_col)
    
    # Main Title & Subtitle (symmetrically starting at x = 24)
    draw.text((24, 38), title, font=font_title, fill=(255, 255, 255, 255))
    draw.text((24, 56), subtitle, font=font_subtitle, fill=(139, 148, 158, 255))
    
    return img, draw

# Dual-panel coordinates (identical across all 6 projects)
p1_x, p1_w = 24, 268
p2_x, p2_w = 308, 268
py, ph = 76, 140

# ==============================================================================
# 1. AIVOA-CRM-HCP (Dual Panel: Interaction Waveform + Automation Telemetry)
# ==============================================================================
print("Rendering 1/6: AIVOA-CRM-HCP...")
frames_1 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "HEALTHCARE AI // CRM",
        "AIVOA-CRM-HCP: AI Healthcare CRM System",
        "FastAPI Async Backend with React UI & Intelligent HCP Interaction Analytics",
        "SYNC: 99.4%", (0, 217, 255, 255), (52, 211, 153, 255)
    )
    
    # Left: Signal Waveform (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(6, 12, 18, 255), outline=(30, 58, 80, 255), width=1)
    draw.text((p1_x + 8, py + 8), "HCP Interaction Signal Velocity", font=font_code_b, fill=(0, 217, 255, 255))
    draw.line([(p1_x, py + 24), (p1_x + p1_w, py + 24)], fill=(30, 58, 80, 255), width=1)
    
    for i in range(1, 4):
        yy = py + 24 + i * 26
        draw.line([(p1_x, yy), (p1_x + p1_w, yy)], fill=(15, 30, 45, 255), width=1)
        
    xs = np.linspace(0, 3 * np.pi, p1_w)
    shift = (f / N_FRAMES) * 2 * np.pi
    ys = (
        np.sin(xs + shift) * 22 + 
        np.sin(2.2 * xs - shift * 0.7) * 14 + 
        np.cos(0.5 * xs + shift) * 15 + 
        68
    )
    
    pts_area = [(p1_x, py + ph)]
    for i in range(p1_w):
        pts_area.append((p1_x + i, py + ph - int(ys[i])))
    pts_area.append((p1_x + p1_w, py + ph))
    draw.polygon(pts_area, fill=(6, 78, 59, 110))
    
    curve_pts = [(p1_x + i, py + ph - int(ys[i])) for i in range(p1_w)]
    draw.line(curve_pts, fill=(52, 211, 153, 255), width=2)
    
    scan_idx = int((f / N_FRAMES) * (p1_w - 40)) + 20
    scan_x = p1_x + scan_idx
    scan_y = py + ph - int(ys[scan_idx])
    draw.line([(scan_x, py + 25), (scan_x, py + ph)], fill=(0, 217, 255, 160), width=1)
    draw.ellipse([(scan_x - 4, scan_y - 4), (scan_x + 4, scan_y + 4)], fill=(0, 217, 255, 255), outline=(255, 255, 255, 255), width=1)
    
    draw.text((p1_x + 10, py + ph - 16), f"Stream: {int(ys[scan_idx] * 4.2)} events/min", font=font_code, fill=(52, 211, 153, 255))
    
    # Right: Workflow Automation Telemetry (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(6, 12, 18, 255), outline=(30, 58, 80, 255), width=1)
    draw.text((p2_x + 8, py + 8), "CRM Workflow Automation", font=font_code_b, fill=(0, 217, 255, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(30, 58, 80, 255), width=1)
    
    draw.text((p2_x + 12, py + 34), "STATUS: ACTIVE AGENT RUNNING", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 12, py + 50), "Effort Cut: 40-70% Automated", font=font_code, fill=(255, 255, 255, 255))
    draw.text((p2_x + 12, py + 66), "FastAPI Latency: 12ms (Async)", font=font_code, fill=(56, 189, 248, 255))
    draw.text((p2_x + 12, py + 82), "Active HCP Network: 500+ Users", font=font_code, fill=(148, 163, 184, 255))
    
    draw.text((p2_x + 12, py + 102), "NLP Sync & Transcription: 99.4%", font=font_code_b, fill=(52, 211, 153, 255))
    bar_prog = int((0.75 + 0.24 * math.sin(f / N_FRAMES * 2 * math.pi)) * (p2_w - 24))
    draw.rounded_rectangle([(p2_x + 12, py + 118), (p2_x + p2_w - 12, py + 126)], radius=4, fill=(15, 23, 42, 255))
    draw.rounded_rectangle([(p2_x + 12, py + 118), (p2_x + 12 + bar_prog, py + 126)], radius=4, fill=(0, 217, 255, 255))
    
    # Bottom Badges (x = 24)
    bx = 24
    bx = draw_pill(draw, bx, 230, "40-70% Effort Cut", (6, 78, 59, 180), (16, 185, 129, 255), (167, 243, 208, 255))
    bx = draw_pill(draw, bx, 230, "500+ Active HCPs", (8, 51, 68, 180), (8, 145, 178, 255), (103, 232, 249, 255))
    bx = draw_pill(draw, bx, 230, "FastAPI Async Core", (30, 27, 75, 180), (79, 70, 229, 255), (199, 210, 254, 255))
    draw_pill(draw, bx, 230, "React Frontend", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_1.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_1[0].save("project_aivoa_crm.gif", save_all=True, append_images=frames_1[1:], duration=70, loop=0)
print("project_aivoa_crm.gif generated successfully!")


# ==============================================================================
# 2. Customer Health Care CRM (Dual Panel: ROC-AUC + Risk Distribution)
# ==============================================================================
print("Rendering 2/6: Customer Health Care CRM...")
frames_2 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "HEALTHCARE // ANALYTICS",
        "Customer Healthcare CRM: Patient Risk Analytics",
        "Discriminative Threshold Analysis & Cohort Risk Probability Distributions",
        "AUC: 0.942", (244, 114, 182, 255), (216, 180, 254, 255)
    )
    
    # Left: ROC Curve (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p1_x + 8, py + 8), "ROC-AUC Curve (TPR vs FPR)", font=font_code_b, fill=(216, 180, 254, 255))
    draw.line([(p1_x, py + 24), (p1_x + p1_w, py + 24)], fill=(33, 38, 45, 255), width=1)
    
    draw.line([(p1_x, py + ph), (p1_x + p1_w, py + 24)], fill=(48, 54, 61, 255), width=1)
    
    curve_pts = []
    pts_auc = [(p1_x, py + ph)]
    for step in range(p1_w):
        fpr = step / p1_w
        tpr = 1.0 - math.pow(1.0 - fpr, 3.8)
        cx = p1_x + step
        cy = py + ph - int(tpr * (ph - 28))
        curve_pts.append((cx, cy))
        pts_auc.append((cx, cy))
    pts_auc.append((p1_x + p1_w, py + ph))
    
    draw.polygon(pts_auc, fill=(88, 28, 135, 95))
    draw.line(curve_pts, fill=(244, 114, 182, 255), width=2)
    
    t_val = f / N_FRAMES
    opt_fpr = t_val * 0.72 + 0.04
    opt_tpr = 1.0 - math.pow(1.0 - opt_fpr, 3.8)
    ox = p1_x + int(opt_fpr * p1_w)
    oy = py + ph - int(opt_tpr * (ph - 28))
    
    draw.line([(ox, py + 24), (ox, py + ph)], fill=(244, 114, 182, 120), width=1)
    draw.line([(p1_x, oy), (p1_x + p1_w, oy)], fill=(244, 114, 182, 120), width=1)
    draw.ellipse([(ox - 4, oy - 4), (ox + 4, oy + 4)], fill=(255, 255, 255, 255), outline=(244, 114, 182, 255), width=2)
    
    draw.text((p1_x + 10, py + ph - 24), f"Threshold: {1 - t_val:.2f}", font=font_code_b, fill=(244, 114, 182, 255))
    draw.text((p1_x + 10, py + ph - 12), f"TPR: {opt_tpr*100:.1f}% | FPR: {opt_fpr*100:.1f}%", font=font_small, fill=(216, 180, 254, 255))
    
    # Right: Patient Risk Cohort Distribution (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Patient Risk Cohort Distribution", font=font_code_b, fill=(103, 232, 249, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(33, 38, 45, 255), width=1)
    
    x_axis = np.linspace(-3, 3, p2_w)
    g_low = np.exp(-0.5 * ((x_axis + 1.2) / 0.8) ** 2) * 65
    g_high = np.exp(-0.5 * ((x_axis - 1.1) / 0.9) ** 2) * 60
    
    pts_l = [(p2_x, py + ph)]
    for i in range(p2_w):
        pts_l.append((p2_x + i, py + ph - int(g_low[i])))
    pts_l.append((p2_x + p2_w, py + ph))
    draw.polygon(pts_l, fill=(6, 78, 59, 110))
    draw.line([(p2_x + i, py + ph - int(g_low[i])) for i in range(p2_w)], fill=(52, 211, 153, 255), width=2)
    
    pts_h = [(p2_x, py + ph)]
    for i in range(p2_w):
        pts_h.append((p2_x + i, py + ph - int(g_high[i])))
    pts_h.append((p2_x + p2_w, py + ph))
    draw.polygon(pts_h, fill=(136, 19, 55, 110))
    draw.line([(p2_x + i, py + ph - int(g_high[i])) for i in range(p2_w)], fill=(244, 114, 182, 255), width=2)
    
    db_x = p2_x + int(p2_w * 0.52 + math.sin(f / N_FRAMES * 2 * math.pi) * 8)
    draw.line([(db_x, py + 26), (db_x, py + ph)], fill=(255, 255, 255, 220), width=1)
    draw.text((db_x - 22, py + 28), "Boundary", font=font_small, fill=(255, 255, 255, 255))
    
    draw.text((p2_x + 10, py + ph - 14), "Low Risk (Normal)", font=font_small, fill=(52, 211, 153, 255))
    draw.text((p2_x + p2_w - 95, py + ph - 14), "High Risk (Care+)", font=font_small, fill=(244, 114, 182, 255))
    
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "AUC-ROC: 0.942", (74, 4, 78, 180), (192, 38, 211, 255), (245, 208, 254, 255))
    bx = draw_pill(draw, bx, 230, "+30% Accuracy Boost", (46, 16, 101, 180), (124, 58, 237, 255), (221, 214, 254, 255))
    bx = draw_pill(draw, bx, 230, "Scikit-Learn Ensemble", (30, 41, 59, 180), (100, 116, 139, 255), (226, 232, 240, 255))
    draw_pill(draw, bx, 230, "Pandas Pipeline", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_2.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_2[0].save("project_customer_healthcare.gif", save_all=True, append_images=frames_2[1:], duration=70, loop=0)
print("project_customer_healthcare.gif generated successfully!")


# ==============================================================================
# 3. SkC Jeevan Tutor (Dual Panel: Big-O Curves + Compiler Runtime)
# ==============================================================================
print("Rendering 3/6: SkC Jeevan Tutor...")
frames_3 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "PYTHON // SANDBOX",
        "SkC_Jeevan_Tutor: Interactive Python Learning Platform",
        "Algorithmic Complexity Profiling & Live Client-Side Code Execution",
        "TESTS: 10/10 PASS", (52, 211, 153, 255), (52, 211, 153, 255)
    )
    
    # Left: Big-O Curves (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(6, 10, 18, 255), outline=(30, 41, 59, 255), width=1)
    draw.text((p1_x + 8, py + 8), "Algorithmic Time Complexity", font=font_code_b, fill=(56, 189, 248, 255))
    draw.line([(p1_x, py + 24), (p1_x + p1_w, py + 24)], fill=(30, 41, 59, 255), width=1)
    
    draw.line([(p1_x + 24, py + ph - 16), (p1_x + p1_w - 12, py + ph - 16)], fill=(51, 65, 85, 255), width=1)
    draw.line([(p1_x + 24, py + 28), (p1_x + 24, py + ph - 16)], fill=(51, 65, 85, 255), width=1)
    
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
        draw.text((pts_n2[-1][0] - 26, pts_n2[-1][1] - 12), "O(N2)", font=font_small, fill=(239, 68, 68, 255))
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
    
    draw.text((p2_x + 12, py + 102), "Test Suite: 10/10 Passed", font=font_code_b, fill=(52, 211, 153, 255))
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
print("project_skc_tutor.gif generated successfully!")


# ==============================================================================
# 4. California Housing (Dual Panel: Regression Fit + Feature Importance)
# ==============================================================================
print("Rendering 4/6: California House Price Prediction...")
frames_4 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "ML // REGRESSION",
        "California Housing: Property Valuation Regression",
        "Gradient Boosting Fit with 95% Confidence Intervals & Feature Importances",
        "R2: 0.864", (251, 191, 36, 255), (251, 191, 36, 255)
    )
    
    # Left: Regression Scatter (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(12, 10, 8, 255), outline=(68, 40, 19, 255), width=1)
    draw.text((p1_x + 8, py + 8), "Income vs Price ($100k)", font=font_code_b, fill=(253, 230, 138, 255))
    draw.line([(p1_x, py + 24), (p1_x + p1_w, py + 24)], fill=(68, 40, 19, 255), width=1)
    
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
    
    draw.polygon([(x0, y0 - 10), (x1, y1 - 10), (x1, y1 + 10), (x0, y0 + 10)], fill=(245, 158, 11, 45))
    draw.line([(x0, y0), (x1, y1)], fill=(239, 68, 68, 255), width=2)
    
    draw.text((p1_x + 34, py + 28), "R2: 0.864", font=font_bold, fill=(251, 191, 36, 255))
    draw.text((p1_x + 34, py + 42), "RMSE: $48,210", font=font_small, fill=(253, 230, 138, 255))
    
    # Right: Feature Importance Bar Chart (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(12, 10, 8, 255), outline=(68, 40, 19, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Feature Importance (Tree-Based)", font=font_code_b, fill=(253, 230, 138, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(68, 40, 19, 255), width=1)
    
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
    bx = draw_pill(draw, bx, 230, "Geospatial Valuation", (59, 7, 100, 180), (126, 34, 206, 255), (233, 213, 255, 255))
    bx = draw_pill(draw, bx, 230, "5-Fold Cross-Validated", (28, 25, 23, 180), (120, 113, 108, 255), (245, 245, 244, 255))
    draw_pill(draw, bx, 230, "Scikit-Learn", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_4.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_4[0].save("project_california_housing.gif", save_all=True, append_images=frames_4[1:], duration=70, loop=0)
print("project_california_housing.gif generated successfully!")


# ==============================================================================
# 5. Deep Learning Projects (Dual Panel: Loss Convergence + Layer Activations)
# ==============================================================================
print("Rendering 5/6: Deep Learning Projects...")
frames_5 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "DEEP LEARNING // PYTORCH",
        "Deep Learning Projects: Neural Architecture & Dynamics",
        "Dual-Axis Tracking: Cross-Entropy Loss Decay vs Validation Accuracy",
        "VAL ACC: 99.2%", (244, 114, 182, 255), (244, 114, 182, 255)
    )
    
    # Left: Training Loss Convergence (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p1_x + 8, py + 8), "Cross-Entropy Loss Decay", font=font_code_b, fill=(244, 114, 182, 255))
    draw.line([(p1_x, py + 24), (p1_x + p1_w, py + 24)], fill=(33, 38, 45, 255), width=1)
    
    for i in range(1, 4):
        yy = py + 24 + i * 26
        draw.line([(p1_x, yy), (p1_x + p1_w, yy)], fill=(22, 27, 34, 255), width=1)
        
    curr_len_1 = int((p1_w - 20) * ((f + 1) / N_FRAMES))
    ep_1 = np.linspace(0, 1, curr_len_1)
    np.random.seed(101)
    l_pts = 2.4 * np.exp(-ep_1 * 4.2) + 0.04 + np.random.normal(0, 0.025, curr_len_1) * (1 - ep_1 * 0.7)
    
    pts_loss = [(p1_x + 10 + i, py + 28 + int((l_pts[i] / 2.5) * (ph - 40))) for i in range(curr_len_1)]
    if len(pts_loss) > 1:
        draw.line(pts_loss, fill=(244, 114, 182, 255), width=2)
        
    draw.text((p1_x + 10, py + ph - 24), "Train Loss: 0.042 (Converged)", font=font_code_b, fill=(244, 114, 182, 255))
    draw.text((p1_x + 10, py + ph - 12), f"Epoch: {int((f+1)/N_FRAMES * 100)}/100 | LR: 1e-4", font=font_small, fill=(148, 163, 184, 255))
    
    # Right: Validation Accuracy & Layer Weights Heatmap (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(10, 14, 20, 255), outline=(33, 38, 45, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Validation Accuracy & Weights", font=font_code_b, fill=(52, 211, 153, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(33, 38, 45, 255), width=1)
    
    curr_len_2 = int((p2_w - 110) * ((f + 1) / N_FRAMES))
    ep_2 = np.linspace(0, 1, curr_len_2)
    acc_pts = 0.45 + 0.54 / (1.0 + np.exp(-ep_2 * 6.5 + 1.8))
    pts_acc = [(p2_x + 10 + i, py + ph - 20 - int(acc_pts[i] * 70)) for i in range(curr_len_2)]
    if len(pts_acc) > 1:
        draw.line(pts_acc, fill=(52, 211, 153, 255), width=2)
        
    draw.text((p2_x + 10, py + 30), "Val Acc: 99.2%", font=font_code_b, fill=(52, 211, 153, 255))
    
    hx = p2_x + p2_w - 95
    hy = py + 32
    draw.text((hx, hy - 4), "Synapse Weights", font=font_code_s, fill=(148, 163, 184, 255))
    for r in range(4):
        for c in range(4):
            val = math.sin(f * 0.3 + r * 1.2 + c * 0.8)
            intensity = int(128 + val * 120)
            col = (52, intensity, 153, 255) if val > 0 else (intensity, 68, 68, 255)
            draw.rectangle([(hx + c * 20, hy + 12 + r * 18), (hx + c * 20 + 16, hy + 12 + r * 18 + 14)], fill=col)
            
    draw.text((p2_x + 10, py + ph - 14), "Architectures: CNN, RNN, Transformers", font=font_small, fill=(148, 163, 184, 255))
    
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "PyTorch 2.3", (69, 10, 10, 180), (220, 38, 38, 255), (254, 202, 202, 255))
    bx = draw_pill(draw, bx, 230, "TensorFlow Keras", (67, 20, 7, 180), (234, 88, 12, 255), (253, 186, 116, 255))
    bx = draw_pill(draw, bx, 230, "Computer Vision & NLP", (6, 78, 59, 180), (5, 150, 105, 255), (110, 231, 183, 255))
    draw_pill(draw, bx, 230, "Jupyter Lab", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_5.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_5[0].save("project_deep_learning.gif", save_all=True, append_images=frames_5[1:], duration=70, loop=0)
print("project_deep_learning.gif generated successfully!")


# ==============================================================================
# 6. Deep-ML Practice (Dual Panel: Loss Contours + Gradient Vector Telemetry)
# ==============================================================================
print("Rendering 6/6: Deep-ML Practice...")
frames_6 = []

for f in range(N_FRAMES):
    img, draw = create_base_canvas(
        "MACHINE LEARNING // FROM SCRATCH",
        "Deep-ML Practice: Pure NumPy ML Foundations",
        "Convex 2D Loss Surface Contours & Gradient Descent Trajectory",
        "GRAD NORM: 0.0018", (0, 217, 255, 255), (52, 211, 153, 255)
    )
    
    # Left: 2D Loss Contours (268px)
    draw.rectangle([(p1_x, py), (p1_x + p1_w, py + ph)], fill=(6, 10, 18, 255), outline=(30, 41, 59, 255), width=1)
    draw.text((p1_x + 8, py + 8), "2D Loss Contours: L(w1, w2)", font=font_code_b, fill=(0, 217, 255, 255))
    draw.line([(p1_x, py + 24), (p1_x + p1_w, py + 24)], fill=(30, 41, 59, 255), width=1)
    
    center_x = p1_x + p1_w // 2
    center_y = py + 24 + (ph - 24) // 2
    
    radii = [18, 38, 58, 80, 102]
    for r in radii:
        rx = r
        ry = int(r * 0.58)
        draw.ellipse([(center_x - rx, center_y - ry), (center_x + rx, center_y + ry)], outline=(30, 58, 80, 220), width=1)
        
    draw.ellipse([(center_x - 3, center_y - 3), (center_x + 3, center_y + 3)], fill=(52, 211, 153, 255))
    draw.text((center_x + 6, center_y - 6), "L*", font=font_small, fill=(52, 211, 153, 255))
    
    t_opt = (f / N_FRAMES)
    gd_steps = 20
    curr_steps = int(gd_steps * ((f + 1) / N_FRAMES))
    path_pts = []
    for s in range(curr_steps):
        prog = s / gd_steps
        angle = prog * 2.5 * math.pi + 0.3
        rad = 85 * (1.0 - prog * 0.88)
        px = center_x + int(math.cos(angle) * rad)
        py_pt = center_y + int(math.sin(angle) * rad * 0.58)
        path_pts.append((px, py_pt))
        
    if len(path_pts) > 1:
        draw.line(path_pts, fill=(244, 114, 182, 240), width=2)
        draw.ellipse([(path_pts[-1][0] - 4, path_pts[-1][1] - 4), (path_pts[-1][0] + 4, path_pts[-1][1] + 4)], fill=(255, 255, 255, 255), outline=(239, 68, 68, 255), width=2)
        
    draw.text((p1_x + 10, py + ph - 14), "Optimizer: Pure NumPy Momentum SGD", font=font_small, fill=(148, 163, 184, 255))
    
    # Right: Gradient Telemetry (268px)
    draw.rectangle([(p2_x, py), (p2_x + p2_w, py + ph)], fill=(6, 10, 18, 255), outline=(30, 41, 59, 255), width=1)
    draw.text((p2_x + 8, py + 8), "Gradient Vector & Convergence", font=font_code_b, fill=(52, 211, 153, 255))
    draw.line([(p2_x, py + 24), (p2_x + p2_w, py + 24)], fill=(30, 41, 59, 255), width=1)
    
    norm_val = 0.082 * math.exp(-t_opt * 3.8) + 0.0018
    draw.text((p2_x + 12, py + 34), f"Grad Norm: {norm_val:.4f}", font=font_code_b, fill=(52, 211, 153, 255))
    draw.text((p2_x + 12, py + 50), f"Step: {int(t_opt * 1000)}/1000 iters", font=font_code, fill=(255, 255, 255, 255))
    draw.text((p2_x + 12, py + 66), "Learning Rate: 0.01 (Cosine)", font=font_code, fill=(56, 189, 248, 255))
    draw.text((p2_x + 12, py + 82), "Loss: 0.0004 (Global Minimum)", font=font_code, fill=(148, 163, 184, 255))
    
    draw.text((p2_x + 12, py + 102), "Gradient Decay Telemetry:", font=font_code_s, fill=(148, 163, 184, 255))
    spark_len = int((p2_w - 24) * ((f + 1) / N_FRAMES))
    s_pts = [(p2_x + 12 + i, py + ph - 8 - int(18 * math.exp(-i / 50))) for i in range(spark_len)]
    if len(s_pts) > 1:
        draw.line(s_pts, fill=(52, 211, 153, 255), width=2)
        
    # Badges
    bx = 24
    bx = draw_pill(draw, bx, 230, "Pure NumPy Implementation", (6, 78, 59, 180), (5, 150, 105, 255), (110, 231, 183, 255))
    bx = draw_pill(draw, bx, 230, "Mathematical Foundations", (46, 16, 101, 180), (124, 58, 237, 255), (221, 214, 254, 255))
    bx = draw_pill(draw, bx, 230, "Vector Calculus", (67, 20, 7, 180), (234, 88, 12, 255), (253, 186, 116, 255))
    draw_pill(draw, bx, 230, "Deep-ML Labs", (22, 27, 34, 180), (48, 54, 61, 255), (139, 148, 158, 255))
    
    frames_6.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_6[0].save("project_deep_ml.gif", save_all=True, append_images=frames_6[1:], duration=70, loop=0)
print("project_deep_ml.gif generated successfully!")


# ==============================================================================
# 7. TWIN CARDS: CURRENT FOCUS & CORE EXPERTISE (480 x 270 Identical Dimensions)
# ==============================================================================
W_TWIN, H_TWIN = 480, 270
print("Rendering 7/8: current_focus_animated.gif...")
frames_focus = []

f_twin_head = get_font(12, bold=True)
f_item_title = get_font(11, bold=True)
f_item_desc = get_font(9, bold=False)
f_item_badge = get_mono_font(8, bold=True)

focus_items = [
    ("LLM Agent Development", "Autonomous LangGraph & LangChain multi-step reasoning", "ACTIVE DEPLOYMENT", (0, 217, 255)),
    ("RAG & Hybrid Retrieval", "Vector search, dense embeddings & re-ranking pipelines", "PRODUCTION OPTIMIZED", (52, 211, 153)),
    ("Healthcare AI Solutions", "Intelligent CRM, HCP analytics & medical compliance", "CLINICAL READY", (167, 139, 250)),
    ("Predictive ML Pipelines", "End-to-end data pipelines, inference & drift detection", "CONTINUOUS CI/CD", (251, 191, 36))
]

for f in range(N_FRAMES):
    img = Image.new("RGBA", (W_TWIN, H_TWIN), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer Border
    draw.rounded_rectangle([(1, 1), (W_TWIN - 2, H_TWIN - 2)], radius=12, fill=(22, 27, 34, 255), outline=(48, 54, 61, 255), width=1)
    
    # Header
    draw.text((18, 14), "CURRENT FOCUS & WORKFLOWS", font=f_twin_head, fill=(52, 211, 153, 255))
    draw.line([(18, 32), (W_TWIN - 18, 32)], fill=(48, 54, 61, 255), width=1)
    
    # 4 Items
    start_y = 42
    item_h = 52
    
    for i, (title, desc, badge_txt, col) in enumerate(focus_items):
        iy = start_y + i * item_h
        
        # Item container box
        draw.rounded_rectangle([(16, iy), (W_TWIN - 16, iy + 46)], radius=6, fill=(13, 17, 23, 220), outline=(33, 38, 45, 255), width=1)
        
        # Pulsing active dot
        pulse = 0.5 + 0.5 * math.sin((f + i * 6) * (2 * math.pi / N_FRAMES))
        dot_alpha = int(120 + pulse * 135)
        draw.ellipse([(26, iy + 13), (34, iy + 21)], fill=(col[0], col[1], col[2], dot_alpha))
        
        # Title
        draw.text((42, iy + 8), title, font=f_item_title, fill=(255, 255, 255, 255))
        
        # Description
        draw.text((42, iy + 26), desc, font=f_item_desc, fill=(139, 148, 158, 255))
        
        # Mini Badge (Right aligned)
        draw.rounded_rectangle([(W_TWIN - 138, iy + 8), (W_TWIN - 24, iy + 23)], radius=3, fill=(col[0], col[1], col[2], 30), outline=(col[0], col[1], col[2], 180), width=1)
        draw.text((W_TWIN - 132, iy + 10), badge_txt, font=f_item_badge, fill=col)
        
    frames_focus.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_focus[0].save("current_focus_animated.gif", save_all=True, append_images=frames_focus[1:], duration=70, loop=0)
print("current_focus_animated.gif generated successfully!")


# ==============================================================================
# 8. CORE EXPERTISE ANIMATED GIF (480 x 270)
# ==============================================================================
print("Rendering 8/8: core_expertise_animated.gif...")
frames_expertise = []

skills = [
    ("LLM Agents & RAG", 0.95, (0, 217, 255)),
    ("Python & ML Systems", 0.95, (52, 211, 153)),
    ("LangChain & LangGraph", 0.90, (167, 139, 250)),
    ("FastAPI & Microservices", 0.85, (251, 191, 36)),
    ("Deep Learning & PyTorch", 0.80, (244, 114, 182)),
    ("Cloud & MLOps (AWS/Docker)", 0.75, (96, 165, 250))
]

f_exp_head = get_font(12, bold=True)
f_skill = get_font(11, bold=True)
f_pct = get_mono_font(11, bold=True)

for f in range(N_FRAMES):
    img = Image.new("RGBA", (W_TWIN, H_TWIN), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer Border
    draw.rounded_rectangle([(1, 1), (W_TWIN - 2, H_TWIN - 2)], radius=12, fill=(22, 27, 34, 255), outline=(48, 54, 61, 255), width=1)
    
    # Header
    draw.text((18, 14), "CORE TECHNICAL COMPETENCIES", font=f_exp_head, fill=(0, 217, 255, 255))
    draw.line([(18, 32), (W_TWIN - 18, 32)], fill=(48, 54, 61, 255), width=1)
    
    bar_x = 195
    bar_w_max = 210
    start_y = 44
    row_h = 35
    
    for i, (name, target_pct, color) in enumerate(skills):
        y = start_y + i * row_h
        
        draw.text((185, y - 2), name, font=f_skill, fill=color, anchor="ra")
        draw.rounded_rectangle([(bar_x, y), (bar_x + bar_w_max, y + 13)], radius=6, fill=(33, 38, 45, 255))
        
        cur_pct = target_pct * (0.94 + 0.06 * math.sin((f + i * 4) * (2 * math.pi / N_FRAMES)))
        cur_w = int(bar_w_max * cur_pct)
        
        draw.rounded_rectangle([(bar_x, y), (bar_x + cur_w, y + 13)], radius=6, fill=color)
        
        dot_x = bar_x + cur_w
        dot_y = y + 6
        draw.ellipse([(dot_x - 3, dot_y - 3), (dot_x + 3, dot_y + 3)], fill=(255, 255, 255, 255))
        
        draw.text((bar_x + bar_w_max + 12, y - 1), f"{int(target_pct * 100)}%", font=f_pct, fill=color)
        
    frames_expertise.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_expertise[0].save("core_expertise_animated.gif", save_all=True, append_images=frames_expertise[1:], duration=70, loop=0)
print("core_expertise_animated.gif generated successfully!")
