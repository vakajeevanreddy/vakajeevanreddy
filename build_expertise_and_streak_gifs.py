import math
import os
from PIL import Image, ImageDraw, ImageFont

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

# ==============================================================================
# 1. CORE EXPERTISE ANIMATED GIF (500 x 270)
# ==============================================================================
print("Generating core_expertise_animated.gif...")
W_CE, H_CE = 480, 270
N_FRAMES = 24
frames_ce = []

skills = [
    ("LLM Agents & RAG", 0.95, (0, 217, 255)),
    ("Python & ML Systems", 0.95, (52, 211, 153)),
    ("LangChain & LangGraph", 0.90, (167, 139, 250)),
    ("FastAPI & Microservices", 0.85, (251, 191, 36)),
    ("Deep Learning & PyTorch", 0.80, (244, 114, 182)),
    ("Cloud & MLOps (AWS/Docker)", 0.75, (96, 165, 250))
]

f_head = get_font(12, bold=True)
f_skill = get_font(11, bold=True)
f_pct = get_mono_font(11, bold=True)

for f in range(N_FRAMES):
    img = Image.new("RGBA", (W_CE, H_CE), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer Card
    draw.rounded_rectangle([(2, 2), (W_CE - 3, H_CE - 3)], radius=12, fill=(22, 27, 34, 255), outline=(48, 54, 61, 255), width=1)
    
    # Header
    draw.text((18, 14), "⚡ PRODUCTION COMPETENCIES", font=f_head, fill=(0, 217, 255, 255))
    draw.line([(18, 32), (W_CE - 18, 32)], fill=(48, 54, 61, 255), width=1)
    
    # Skills rows
    bar_x = 195
    bar_w_max = 210
    start_y = 44
    row_h = 35
    
    # Sinusoidal breathing phase
    pulse = math.sin(f * (2 * math.pi / N_FRAMES))
    
    for i, (name, target_pct, color) in enumerate(skills):
        y = start_y + i * row_h
        
        # Skill Name
        draw.text((185, y - 2), name, font=f_skill, fill=color, anchor="ra")
        
        # Track Background
        draw.rounded_rectangle([(bar_x, y), (bar_x + bar_w_max, y + 13)], radius=6, fill=(33, 38, 45, 255))
        
        # Current animated width
        # Slight dynamic shimmer around target
        cur_pct = target_pct * (0.94 + 0.06 * math.sin((f + i * 4) * (2 * math.pi / N_FRAMES)))
        cur_w = int(bar_w_max * cur_pct)
        
        # Filled Bar
        draw.rounded_rectangle([(bar_x, y), (bar_x + cur_w, y + 13)], radius=6, fill=color)
        
        # Glowing head dot
        dot_x = bar_x + cur_w
        dot_y = y + 6
        draw.ellipse([(dot_x - 3, dot_y - 3), (dot_x + 3, dot_y + 3)], fill=(255, 255, 255, 255))
        
        # Percentage text
        draw.text((bar_x + bar_w_max + 12, y - 1), f"{int(target_pct * 100)}%", font=f_pct, fill=color)
        
    frames_ce.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_ce[0].save("core_expertise_animated.gif", save_all=True, append_images=frames_ce[1:], duration=70, loop=0)
print("core_expertise_animated.gif generated successfully!")

# ==============================================================================
# 2. GITHUB STREAK ANIMATED GIF (860 x 200)
# ==============================================================================
print("Generating streak_animated.gif...")
W_ST, H_ST = 860, 200
frames_st = []

f_title = get_font(12, bold=True)
f_big_val = get_font(42, bold=True)
f_med_val = get_font(22, bold=True)
f_sub = get_font(12, bold=False)
f_small = get_font(11, bold=False)

commit_data = [
    (11, 0.4), (22, 0.5), (5, 0.3), (0, 0.0), (16, 0.45), (27, 0.55),
    (11, 0.4), (44, 0.65), (33, 0.55), (66, 0.8), (83, 0.9), (100, 1.0)
]

for f in range(N_FRAMES):
    img = Image.new("RGBA", (W_ST, H_ST), (13, 17, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer frame
    draw.rounded_rectangle([(2, 2), (W_ST - 3, H_ST - 3)], radius=16, fill=(13, 17, 28, 255), outline=(48, 54, 61, 255), width=1)
    
    # ------------------ PANEL 1: CURRENT STREAK (Left) ------------------
    p1_w = 205
    draw.rounded_rectangle([(14, 14), (14 + p1_w, H_ST - 14)], radius=12, fill=(22, 27, 34, 200), outline=(48, 54, 61, 255), width=1)
    draw.text((14 + p1_w // 2, 28), "CURRENT STREAK", font=f_title, fill=(88, 166, 255, 255), anchor="mm")
    
    # Pulsing fire icon representation
    fire_scale = 1.0 + 0.12 * math.sin(f * (2 * math.pi / N_FRAMES))
    draw.text((14 + p1_w // 2, 72), "🔥", font=get_font(int(36 * fire_scale)), fill=(255, 102, 0, 255), anchor="mm")
    
    # Streak number
    draw.text((14 + p1_w // 2, 122), "14", font=f_big_val, fill=(57, 211, 83, 255), anchor="mm")
    draw.text((14 + p1_w // 2, 155), "day streak", font=f_sub, fill=(139, 148, 158, 255), anchor="mm")
    
    # ------------------ PANEL 2: CONTRIBUTIONS (Middle) ------------------
    p2_x = 230
    p2_w = 195
    draw.rounded_rectangle([(p2_x, 14), (p2_x + p2_w, H_ST - 14)], radius=12, fill=(22, 27, 34, 200), outline=(48, 54, 61, 255), width=1)
    draw.text((p2_x + p2_w // 2, 28), "CONTRIBUTIONS", font=f_title, fill=(88, 166, 255, 255), anchor="mm")
    
    draw.text((p2_x + p2_w // 2, 76), "278", font=f_big_val, fill=(255, 255, 255, 255), anchor="mm")
    draw.text((p2_x + p2_w // 2, 108), "last 12 months", font=f_sub, fill=(139, 148, 158, 255), anchor="mm")
    
    draw.line([(p2_x + 16, 126), (p2_x + p2_w - 16, 126)], fill=(48, 54, 61, 255), width=1)
    
    # Longest streak & active repos
    draw.text((p2_x + 50, 145), "21", font=f_med_val, fill=(245, 158, 11, 255), anchor="mm")
    draw.text((p2_x + 50, 166), "longest", font=f_small, fill=(139, 148, 158, 255), anchor="mm")
    
    draw.text((p2_x + 145, 145), "5+", font=f_med_val, fill=(167, 139, 250, 255), anchor="mm")
    draw.text((p2_x + 145, 166), "active repos", font=f_small, fill=(139, 148, 158, 255), anchor="mm")
    
    # ------------------ PANEL 3: WEEKLY COMMITS (Right) ------------------
    p3_x = 438
    p3_w = W_ST - p3_x - 14
    draw.rounded_rectangle([(p3_x, 14), (p3_x + p3_w, H_ST - 14)], radius=12, fill=(22, 27, 34, 200), outline=(48, 54, 61, 255), width=1)
    draw.text((p3_x + p3_w // 2, 28), "WEEKLY COMMIT DYNAMICS (3 MONTHS)", font=f_title, fill=(88, 166, 255, 255), anchor="mm")
    
    # Baseline
    base_y = 150
    draw.line([(p3_x + 20, base_y), (p3_x + p3_w - 20, base_y)], fill=(48, 54, 61, 255), width=1)
    
    # Commit bars
    bar_width = 22
    bar_gap = 9
    start_bx = p3_x + 28
    
    # Wave pulse moving through the bars
    for idx, (height_val, op) in enumerate(commit_data):
        bx = start_bx + idx * (bar_width + bar_gap)
        if height_val == 0:
            draw.rectangle([(bx, base_y - 4), (bx + bar_width, base_y)], fill=(45, 51, 59, 255))
            continue
            
        # Wave modulation
        wave = math.sin((f + idx * 2) * (2 * math.pi / N_FRAMES))
        dynamic_h = max(6, int(height_val * 0.95 + wave * 6))
        
        by1 = base_y - dynamic_h
        by2 = base_y
        
        # Color with intensity
        green_r = int(57 * op)
        green_g = int(211 * op)
        green_b = int(83 * op)
        
        draw.rounded_rectangle([(bx, by1), (bx + bar_width, by2)], radius=3, fill=(green_r, green_g, green_b, 255))
        
        # Highlight on top of bar
        draw.line([(bx + 2, by1), (bx + bar_width - 2, by1)], fill=(110, 231, 183, 255), width=1)
        
    # Month labels
    draw.text((start_bx + 15, base_y + 14), "AUG", font=f_small, fill=(139, 148, 158, 255), anchor="mm")
    draw.text((start_bx + 140, base_y + 14), "SEP", font=f_small, fill=(139, 148, 158, 255), anchor="mm")
    draw.text((start_bx + 270, base_y + 14), "OCT", font=f_small, fill=(139, 148, 158, 255), anchor="mm")
    
    frames_st.append(img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

frames_st[0].save("streak_animated.gif", save_all=True, append_images=frames_st[1:], duration=70, loop=0)
print("streak_animated.gif generated successfully!")
