import os
import math
from PIL import Image, ImageDraw, ImageFont

os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")

W, H = 560, 260
N_FRAMES = 16

# Load fonts
try:
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 16)
    font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 12)
    font_bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 12)
    font_small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
    font_code = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 12)
    font_code_sm = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 11)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_bold = font_title
    font_small = font_title
    font_code = font_title
    font_code_sm = font_title

def draw_header_bar(draw, category, status_text, status_color, bg_color, border_color):
    draw.rounded_rectangle([(0, 0), (W, H)], radius=12, fill=bg_color, outline=border_color, width=2)
    draw.rounded_rectangle([(0, 0), (W, 30)], radius=12, fill=(15, 20, 28))
    draw.rectangle([(0, 15), (W, 30)], fill=(15, 20, 28))
    draw.line([(0, 30), (W, 30)], fill=border_color, width=1)
    
    # Category tag
    draw.text((16, 8), category, font=font_code, fill=(200, 220, 240))
    # Status indicator
    draw.ellipse([(W - 130, 11), (W - 122, 19)], fill=status_color)
    draw.text((W - 116, 8), status_text, font=font_code, fill=status_color)

def draw_metric_badge(draw, x, y, w, h, text, fill_bg, stroke_col, text_col):
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=6, fill=fill_bg, outline=stroke_col, width=1)
    draw.text((x + 10, y + 5), text, font=font_bold, fill=text_col)

# ==============================================================================
# 1. AIVOA-CRM-HCP (Animated ECG Pulse + Typing Interaction Log)
# ==============================================================================
frames_1 = []
for frame in range(N_FRAMES):
    img = Image.new("RGB", (W, H), (8, 18, 24))
    draw = ImageDraw.Draw(img)
    
    draw_header_bar(draw, "AIVOA-CRM-HCP // AI HEALTHCARE CRM", "ONLINE 99.8%", (52, 211, 153), (6, 20, 26), (5, 150, 105))
    
    # Title & Subtitle
    draw.ellipse([(20, 42), (48, 70)], fill=(6, 78, 59), outline=(16, 185, 129), width=1)
    draw.rectangle([(32, 48), (36, 64)], fill=(52, 211, 153))
    draw.rectangle([(26, 54), (42, 58)], fill=(52, 211, 153))
    draw.text((58, 42), "AIVOA-CRM-HCP", font=font_title, fill=(255, 255, 255))
    draw.text((58, 64), "AI Documentation & HCP Interaction Platform", font=font_sub, fill=(110, 231, 183))
    
    # ECG Pulse Monitor Box
    draw.rounded_rectangle([(20, 88), (W - 20, 190)], radius=8, fill=(4, 15, 20), outline=(6, 78, 59), width=1)
    
    # Grid lines inside ECG
    for gx in range(40, W - 20, 40):
        draw.line([(gx, 88), (gx, 190)], fill=(10, 30, 35), width=1)
    for gy in range(108, 190, 20):
        draw.line([(20, gy), (W - 20, gy)], fill=(10, 30, 35), width=1)
    
    # Animated ECG waveform
    pts = []
    offset = (frame / N_FRAMES) * 80
    base_y = 138
    for x in range(25, W - 25, 4):
        t = (x + offset) % 120
        y = base_y
        if 40 <= t < 48:
            y -= (t - 40) * 4
        elif 48 <= t < 56:
            y += (t - 48) * 9
        elif 56 <= t < 64:
            y -= (t - 56) * 5
        elif 64 <= t < 72:
            y += 8
        pts.append((x, y))
    
    if len(pts) > 1:
        draw.line(pts, fill=(52, 211, 153), width=2)
    
    # Live Interaction typing text
    if frame < 8:
        log_text = "> Dr. Sharma: Inquired dosage protocol -> Auto-logging..."
    else:
        log_text = "> AI Verified: Oncology note synced to CRM [Accuracy: 98%]"
    draw.text((32, 168), log_text, font=font_code_sm, fill=(167, 243, 208))
    
    # Metric Badges
    draw_metric_badge(draw, 20, 210, 160, 28, "⚡ 40-70% Less Effort", (6, 78, 59), (16, 185, 129), (167, 243, 208))
    draw_metric_badge(draw, 190, 210, 150, 28, "🏥 500+ HCP Users", (8, 51, 68), (8, 145, 178), (103, 232, 249))
    draw_metric_badge(draw, 350, 210, 190, 28, "🔗 FastAPI + React Native", (30, 27, 75), (79, 70, 229), (199, 210, 254))
    
    frames_1.append(img)

frames_1[0].save("project_aivoa_crm.gif", save_all=True, append_images=frames_1[1:], duration=120, loop=0)
print("Saved project_aivoa_crm.gif")

# ==============================================================================
# 2. Customer Health Care CRM (Animated Bar Equalizer + Pulsing Clusters)
# ==============================================================================
frames_2 = []
for frame in range(N_FRAMES):
    img = Image.new("RGB", (W, H), (20, 10, 30))
    draw = ImageDraw.Draw(img)
    
    draw_header_bar(draw, "CUSTOMER HEALTHCARE CRM // ML ANALYTICS", "AUC: 0.94", (244, 114, 182), (24, 10, 36), (168, 85, 247))
    
    draw.ellipse([(20, 42), (48, 70)], fill=(59, 7, 100), outline=(192, 132, 252), width=1)
    draw.text((27, 46), "🧠", font=font_title)
    draw.text((58, 42), "Customer Health Care CRM App", font=font_title, fill=(255, 255, 255))
    draw.text((58, 64), "Predictive Patient Health Risk Scoring & Churn Modeling", font=font_sub, fill=(244, 114, 182))
    
    # Analytics Box
    draw.rounded_rectangle([(20, 88), (W - 20, 190)], radius=8, fill=(15, 6, 22), outline=(88, 28, 135), width=1)
    
    # Dynamic Cohort Bars (Animated Equalizer)
    bar_data = [45, 75, 30, 90, 60, 40, 80]
    bx_start = 40
    for idx, base_h in enumerate(bar_data):
        phase = (frame / N_FRAMES) * 2 * math.pi + idx * 0.9
        var_h = base_h + int(14 * math.sin(phase))
        bx = bx_start + idx * 26
        by = 175 - var_h
        draw.rounded_rectangle([(bx, by), (bx + 16, 175)], radius=3, fill=(236, 72, 153))
    
    draw.line([(30, 176), (230, 176)], fill=(120, 50, 150), width=1)
    draw.text((40, 96), "Patient Cohort Risk Distribution", font=font_code_sm, fill=(216, 180, 254))
    
    # Clustering scatter plot on right side
    cx_base, cy_base = 320, 100
    draw.text((cx_base, cy_base), "Clustering Embeddings (t-SNE)", font=font_code_sm, fill=(147, 197, 253))
    
    # Cluster points with pulsing animation
    pulse = math.sin((frame / N_FRAMES) * 2 * math.pi) * 3
    # Low Risk (Cyan)
    for px, py in [(340, 135), (355, 145), (365, 130), (375, 142)]:
        draw.ellipse([(px - 3, py - 3), (px + 3, py + 3)], fill=(56, 189, 248))
    # High Risk (Pink)
    for px, py in [(430, 130), (445, 140), (460, 125), (475, 135)]:
        draw.ellipse([(px - 4 - pulse, py - 4 - pulse), (px + 4 + pulse, py + 4 + pulse)], fill=(244, 114, 182))
    
    # Badges
    draw_metric_badge(draw, 20, 210, 155, 28, "🎯 +30% Accuracy", (74, 4, 78), (192, 38, 211), (245, 208, 254))
    draw_metric_badge(draw, 185, 210, 175, 28, "🤖 Scikit-Learn + XGBoost", (46, 16, 101), (124, 58, 237), (221, 214, 254))
    draw_metric_badge(draw, 370, 210, 170, 28, "📊 Pandas Risk Pipelines", (30, 41, 59), (100, 116, 139), (226, 232, 240))
    
    frames_2.append(img)

frames_2[0].save("project_customer_healthcare.gif", save_all=True, append_images=frames_2[1:], duration=120, loop=0)
print("Saved project_customer_healthcare.gif")

# ==============================================================================
# 3. SkC Jeevan Tutor (Animated Real Python Typing IDE)
# ==============================================================================
frames_3 = []
full_code = [
    "def train_learning_path(user):",
    "    concepts = ['Data Science', 'AI/ML', 'Python']",
    "    return [c.master() for c in concepts]"
]
for frame in range(N_FRAMES):
    img = Image.new("RGB", (W, H), (11, 19, 43))
    draw = ImageDraw.Draw(img)
    
    draw_header_bar(draw, "SkC JEEVAN TUTOR // INTERACTIVE PYTHON LAB", "LIVE COMPILER", (56, 189, 248), (11, 25, 44), (56, 189, 248))
    
    draw.ellipse([(20, 42), (48, 70)], fill=(12, 74, 110), outline=(56, 189, 248), width=1)
    draw.text((27, 46), "💻", font=font_title)
    draw.text((58, 42), "SkC Jeevan Tutor", font=font_title, fill=(255, 255, 255))
    draw.text((58, 64), "Interactive Python Learning Platform with Live Sandbox", font=font_sub, fill=(56, 189, 248))
    
    # Code Window
    draw.rounded_rectangle([(20, 88), (W - 20, 195)], radius=8, fill=(6, 10, 20), outline=(30, 41, 59), width=1)
    
    # Editor window header
    draw.ellipse([(32, 100), (38, 106)], fill=(239, 68, 68))
    draw.ellipse([(44, 100), (50, 106)], fill=(245, 158, 11))
    draw.ellipse([(56, 100), (62, 106)], fill=(16, 185, 129))
    draw.text((75, 96), "main.py - Interactive Exercise 04", font=font_code_sm, fill=(100, 116, 139))
    draw.line([(20, 114), (W - 20, 114)], fill=(20, 30, 45), width=1)
    
    # Line 1
    draw.text((32, 122), "def ", font=font_code_sm, fill=(244, 114, 182))
    draw.text((60, 122), "train_learning_path(user):", font=font_code_sm, fill=(56, 189, 248))
    
    # Line 2 typing
    chars_to_show = int((frame / N_FRAMES) * len(full_code[1]))
    typed_l2 = full_code[1][:chars_to_show]
    draw.text((46, 140), typed_l2, font=font_code_sm, fill=(253, 224, 71))
    
    # Line 3 + blinking cursor
    if frame >= 8:
        draw.text((46, 158), full_code[2], font=font_code_sm, fill=(52, 211, 153))
        # Cursor
        if frame % 2 == 0:
            cx = 46 + len(full_code[2]) * 6.5
            draw.rectangle([(cx, 158), (cx + 6, 172)], fill=(56, 189, 248))
    
    # Test passed indicator
    draw.text((32, 178), "[RUNNER] Test Cases: 10/10 Passed (0.02s) 🚀", font=font_code_sm, fill=(52, 211, 153))
    
    # Badges
    draw_metric_badge(draw, 20, 212, 140, 28, "🐍 Python 3.12 Engine", (30, 58, 138), (37, 99, 235), (147, 197, 253))
    draw_metric_badge(draw, 170, 212, 160, 28, "🌐 HTML5 + Vanilla JS", (67, 20, 7), (234, 88, 12), (253, 186, 116))
    draw_metric_badge(draw, 340, 212, 200, 28, "⚡ Live Sandbox Compiler", (6, 78, 59), (5, 150, 105), (110, 231, 183))
    
    frames_3.append(img)

frames_3[0].save("project_skc_tutor.gif", save_all=True, append_images=frames_3[1:], duration=120, loop=0)
print("Saved project_skc_tutor.gif")

# ==============================================================================
# 4. California Housing (Animated Regression Fit Curve + R2 Metric)
# ==============================================================================
frames_4 = []
for frame in range(N_FRAMES):
    img = Image.new("RGB", (W, H), (25, 18, 12))
    draw = ImageDraw.Draw(img)
    
    draw_header_bar(draw, "CALIFORNIA HOUSING // SUPERVISED ML", "R² = 0.86", (251, 191, 36), (28, 18, 10), (245, 158, 11))
    
    draw.ellipse([(20, 42), (48, 70)], fill=(69, 26, 3), outline=(245, 158, 11), width=1)
    draw.text((27, 46), "🏠", font=font_title)
    draw.text((58, 42), "California House Price Prediction", font=font_title, fill=(255, 255, 255))
    draw.text((58, 64), "Advanced Regression, Geospatial EDA & Feature Engineering", font=font_sub, fill=(251, 191, 36))
    
    # Plot box
    draw.rounded_rectangle([(20, 88), (W - 20, 195)], radius=8, fill=(18, 11, 6), outline=(68, 40, 19), width=1)
    
    # Axes
    draw.line([(50, 175), (W - 40, 175)], fill=(120, 53, 15), width=1)
    draw.line([(50, 100), (50, 175)], fill=(120, 53, 15), width=1)
    draw.text((W - 130, 178), "Median Income ($10k)", font=font_small, fill=(180, 120, 80))
    draw.text((25, 94), "Price ($)", font=font_small, fill=(180, 120, 80))
    
    # Scatter points
    scatter_pts = [
        (80, 160), (110, 152), (140, 142), (170, 138), (200, 126),
        (230, 120), (260, 114), (290, 108), (320, 102), (350, 98),
        (380, 92), (410, 88), (440, 84), (470, 80)
    ]
    for px, py in scatter_pts:
        draw.ellipse([(px - 3, py - 3), (px + 3, py + 3)], fill=(253, 230, 138))
    
    # Animated Regression Best-Fit Line (drawing from left to right)
    curr_len = int((frame / N_FRAMES) * (W - 120))
    x_end = 60 + curr_len
    y_end = 168 - int(curr_len * 0.22)
    draw.line([(60, 168), (x_end, y_end)], fill=(239, 68, 68), width=3)
    
    # Metric callout
    draw.text((W - 150, 105), "Model Fit: R² = 0.86", font=font_code, fill=(245, 158, 11))
    draw.text((W - 150, 125), "RMSE: $48,200", font=font_code_sm, fill=(253, 230, 138))
    
    # Badges
    draw_metric_badge(draw, 20, 212, 160, 28, "📈 Random Forest Regressor", (69, 26, 3), (217, 119, 6), (253, 230, 138))
    draw_metric_badge(draw, 190, 212, 175, 28, "🗺️ Lat/Long Spatial Features", (59, 7, 100), (126, 34, 206), (233, 213, 255))
    draw_metric_badge(draw, 375, 212, 165, 28, "📊 Scikit-Learn Pipelines", (28, 25, 23), (120, 113, 108), (245, 245, 244))
    
    frames_4.append(img)

frames_4[0].save("project_california_housing.gif", save_all=True, append_images=frames_4[1:], duration=120, loop=0)
print("Saved project_california_housing.gif")

# ==============================================================================
# 5. Deep Learning Projects (Animated Neural Synapse Signals)
# ==============================================================================
frames_5 = []
for frame in range(N_FRAMES):
    img = Image.new("RGB", (W, H), (22, 8, 38))
    draw = ImageDraw.Draw(img)
    
    draw_header_bar(draw, "DEEP LEARNING // NEURAL NETS & VISION", "ACCURACY: 99.2%", (244, 114, 182), (25, 7, 42), (236, 72, 153))
    
    draw.ellipse([(20, 42), (48, 70)], fill=(80, 7, 36), outline=(244, 114, 182), width=1)
    draw.text((27, 46), "🤖", font=font_title)
    draw.text((58, 42), "Deep Learning Projects Suite", font=font_title, fill=(255, 255, 255))
    draw.text((58, 64), "CNNs, RNNs, Transformers & Multi-Layer Neural Architectures", font=font_sub, fill=(244, 114, 182))
    
    # Net Box
    draw.rounded_rectangle([(20, 88), (W - 20, 195)], radius=8, fill=(12, 4, 20), outline=(112, 26, 117), width=1)
    
    # Layer definitions: (x, [y_nodes])
    l1 = (70, [115, 142, 168])
    l2 = (190, [105, 125, 142, 160, 178])
    l3 = (310, [110, 130, 152, 172])
    l4 = (430, [125, 155])
    
    # Draw connections
    for y1 in l1[1]:
        for y2 in l2[1]:
            draw.line([(l1[0], y1), (l2[0], y2)], fill=(45, 15, 60), width=1)
    for y1 in l2[1]:
        for y2 in l3[1]:
            draw.line([(l2[0], y1), (l3[0], y2)], fill=(45, 15, 60), width=1)
    for y1 in l3[1]:
        for y2 in l4[1]:
            draw.line([(l3[0], y1), (l4[0], y2)], fill=(45, 15, 60), width=1)
            
    # Animated Signal pulse moving through layers
    progress = frame / N_FRAMES
    if progress < 0.33:
        p_t = progress / 0.33
        px = l1[0] + (l2[0] - l1[0]) * p_t
        py = l1[1][1] + (l2[1][2] - l1[1][1]) * p_t
        draw.ellipse([(px - 4, py - 4), (px + 4, py + 4)], fill=(56, 189, 248))
    elif progress < 0.66:
        p_t = (progress - 0.33) / 0.33
        px = l2[0] + (l3[0] - l2[0]) * p_t
        py = l2[1][2] + (l3[1][1] - l2[1][2]) * p_t
        draw.ellipse([(px - 5, py - 5), (px + 5, py + 5)], fill=(244, 114, 182))
    else:
        p_t = (progress - 0.66) / 0.34
        px = l3[0] + (l4[0] - l3[0]) * p_t
        py = l3[1][1] + (l4[1][0] - l3[1][1]) * p_t
        draw.ellipse([(px - 5, py - 5), (px + 5, py + 5)], fill=(52, 211, 153))
    
    # Draw Nodes
    for y in l1[1]:
        draw.ellipse([(l1[0] - 6, y - 6), (l1[0] + 6, y + 6)], fill=(56, 189, 248))
    for y in l2[1]:
        draw.ellipse([(l2[0] - 6, y - 6), (l2[0] + 6, y + 6)], fill=(168, 85, 247))
    for y in l3[1]:
        draw.ellipse([(l3[0] - 6, y - 6), (l3[0] + 6, y + 6)], fill=(236, 72, 153))
    for y in l4[1]:
        draw.ellipse([(l4[0] - 7, y - 7), (l4[0] + 7, y + 7)], fill=(52, 211, 153))
        
    draw.text((60, 94), "INPUT", font=font_small, fill=(56, 189, 248))
    draw.text((170, 94), "CONV2D", font=font_small, fill=(168, 85, 247))
    draw.text((290, 94), "DENSE", font=font_small, fill=(236, 72, 153))
    draw.text((410, 94), "OUTPUT", font=font_small, fill=(52, 211, 153))
    
    # Badges
    draw_metric_badge(draw, 20, 212, 145, 28, "🔥 PyTorch Models", (67, 20, 7), (234, 88, 12), (253, 186, 116))
    draw_metric_badge(draw, 175, 212, 160, 28, "⚡ TensorFlow & Keras", (69, 26, 3), (217, 119, 6), (253, 230, 138))
    draw_metric_badge(draw, 345, 212, 195, 28, "🧠 CNNs, RNNs & Attention", (59, 7, 100), (126, 34, 206), (233, 213, 255))
    
    frames_5.append(img)

frames_5[0].save("project_deep_learning.gif", save_all=True, append_images=frames_5[1:], duration=120, loop=0)
print("Saved project_deep_learning.gif")

# ==============================================================================
# 6. Deep-ML Practice (Animated Gradient Descent Loss Surface Scan)
# ==============================================================================
frames_6 = []
for frame in range(N_FRAMES):
    img = Image.new("RGB", (W, H), (4, 30, 54))
    draw = ImageDraw.Draw(img)
    
    draw_header_bar(draw, "DEEP-ML PRACTICE // ALGORITHMS FROM SCRATCH", "PURE NUMPY", (56, 189, 248), (2, 30, 54), (2, 132, 199))
    
    draw.ellipse([(20, 42), (48, 70)], fill=(12, 74, 110), outline=(56, 189, 248), width=1)
    draw.text((27, 44), "∑", font=font_title, fill=(186, 230, 253))
    draw.text((58, 42), "Deep-ML Mathematical Practice", font=font_title, fill=(255, 255, 255))
    draw.text((58, 64), "Vectorized Neural Network Forward & Backward Passes in NumPy", font=font_sub, fill=(56, 189, 248))
    
    # Math Terminal Box
    draw.rounded_rectangle([(20, 88), (W - 20, 195)], radius=8, fill=(3, 20, 36), outline=(3, 105, 161), width=1)
    
    # Left side: Formulas
    draw.text((35, 100), "GRADIENT DESCENT UPDATE RULE:", font=font_code_sm, fill=(56, 189, 248))
    draw.text((35, 118), "θ := θ - α · ∇J(θ)", font=font_code, fill=(74, 222, 128))
    draw.text((35, 140), "Z = np.dot(X, W) + b", font=font_code_sm, fill=(125, 211, 252))
    draw.text((35, 158), "dW = (1/m) * X.T @ (A - Y)", font=font_code_sm, fill=(244, 114, 182))
    draw.text((35, 174), "db = (1/m) * np.sum(dZ, axis=1)", font=font_code_sm, fill=(253, 224, 71))
    
    # Right side: Animated Loss Surface Descent Map
    cx, cy = 420, 140
    # Contour ellipses
    for r in [45, 32, 20, 10]:
        draw.ellipse([(cx - r * 1.5, cy - r), (cx + r * 1.5, cy + r)], outline=(7, 89, 133), width=1)
        
    # Animated descent point stepping into minimum
    step = frame / N_FRAMES
    px = cx - 55 + step * 55
    py = cy - 35 + step * 35
    draw.ellipse([(px - 4, py - 4), (px + 4, py + 4)], fill=(239, 68, 68))
    draw.text((cx - 30, cy + 38), "Loss -> Min", font=font_small, fill=(74, 222, 128))
    
    # Badges
    draw_metric_badge(draw, 20, 212, 160, 28, "📐 Vectorized Matrix Math", (12, 74, 110), (2, 132, 199), (186, 230, 253))
    draw_metric_badge(draw, 190, 212, 170, 28, "⚡ Zero External Libraries", (20, 83, 45), (22, 163, 74), (187, 247, 208))
    draw_metric_badge(draw, 370, 212, 170, 28, "🎓 Theoretical Derivations", (30, 27, 75), (67, 56, 202), (199, 210, 254))
    
    frames_6.append(img)

frames_6[0].save("project_deep_ml.gif", save_all=True, append_images=frames_6[1:], duration=120, loop=0)
print("Saved project_deep_ml.gif")

print("ALL 6 HIGH-RESOLUTION ANIMATED PROJECT GIFS CREATED SUCCESSFULLY!")
