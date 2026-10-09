import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

print("Building Full-Body 3D Character Multi-Joint Animation Engine...")

char_waving = Image.open("clean_3d_char.png").convert("RGBA")
char_presenting = Image.open("clean_3d_presenting.png").convert("RGBA")

# Bounding box of character is (277, 61, 784, 984)
# In char_waving, isolate:
# 1. Right arm & waving hand (viewer's right side, character's left):
#    Shoulder joint at approx (580, 270), elbow at (660, 240), hand at (685, 150)
#    Let's crop the right arm assembly
r_arm_box = (540, 90, 785, 420)
r_arm_crop = char_waving.crop(r_arm_box)

# 2. Left arm (viewer's left side):
#    Shoulder joint at (380, 280), hand resting at (370, 610)
l_arm_box = (270, 270, 420, 630)
l_arm_crop = char_waving.crop(l_arm_box)

# 3. Head:
#    Neck/pivot at (505, 230)
head_box = (410, 55, 600, 260)
head_crop = char_waving.crop(head_box)

# 4. Torso & Legs base (with head and arms erased so we can articulate all limbs freely)
body_base = char_waving.copy()
# Clear arm regions and head from body base
for y in range(90, 420):
    for x in range(570, 785):
        body_base.putpixel((x, y), (0, 0, 0, 0))
for y in range(270, 630):
    for x in range(270, 390):
        body_base.putpixel((x, y), (0, 0, 0, 0))
for y in range(55, 240):
    for x in range(410, 600):
        body_base.putpixel((x, y), (0, 0, 0, 0))

# Also crop presenting arms from char_presenting for Phase 2
p_l_arm_box = (350, 260, 480, 520)
p_l_arm_crop = char_presenting.crop(p_l_arm_box)
p_r_arm_box = (580, 250, 750, 520)
p_r_arm_crop = char_presenting.crop(p_r_arm_box)

interests = [
    ("🧠 LLM Agents & Multi-Agent Systems", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive ML & Decision Analytics", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Full-Stack AI", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud Deployment", "#60A5FA"),
]

CANVAS_SIZE = 580
FPS = 15
TOTAL_FRAMES = 120  # 8.0s seamless loop

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
    font_hi = ImageFont.truetype("arialbd.ttf", 20)
    font_small = ImageFont.truetype("arial.ttf", 13)
    font_sub = ImageFont.truetype("arialbd.ttf", 11)
except:
    font_bold = ImageFont.load_default()
    font_hi = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Character height on 580 canvas: 430px (leaving top space for UI banner)
scale = 430.0 / (984.0 - 61.0)
scaled_w = int(1024 * scale)
scaled_h = int(1024 * scale)

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # 1. Solid modern dark studio background (#0d1117 / #161b22)
    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Outer sleek card border
    draw.rounded_rectangle([6, 6, CANVAS_SIZE-6, CANVAS_SIZE-6], radius=20, fill=(16, 21, 30, 255), outline=(48, 54, 61, 255), width=2)
    
    # Subtle studio rim glow circle behind character
    glow_y = 300
    draw.ellipse([CANVAS_SIZE//2 - 160, glow_y - 120, CANVAS_SIZE//2 + 160, glow_y + 120], fill=(22, 34, 55, 120))
    
    # Dynamic body kinematics
    body_breathe_y = math.sin(t * 3.5) * 2.5
    body_sway_x = math.sin(t * 1.8) * 1.5
    
    char_base_x = int((CANVAS_SIZE - scaled_w) / 2) + int(body_sway_x)
    char_base_y = 110 + int(body_breathe_y) - int(61 * scale)
    
    # Paste base torso and grounded legs
    s_body = body_base.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
    canvas.paste(s_body, (char_base_x, char_base_y), s_body)
    
    # 2. Articulate Head (Gentle nod & sway + blinking)
    head_tilt = math.sin(t * 2.5) * 3.0  # -3 to +3 degrees
    pad = 60
    p_head = Image.new("RGBA", (head_crop.width + pad*2, head_crop.height + pad*2), (0, 0, 0, 0))
    p_head.paste(head_crop, (pad, pad))
    # Head pivot at neck (505, 230)
    h_piv_x = (505 - head_box[0]) + pad
    h_piv_y = (230 - head_box[1]) + pad
    rot_head = p_head.rotate(head_tilt, resample=Image.BICUBIC, center=(h_piv_x, h_piv_y))
    s_head = rot_head.resize((int(rot_head.width * scale), int(rot_head.height * scale)), Image.Resampling.LANCZOS)
    head_x = char_base_x + int((head_box[0] - pad) * scale)
    head_y = char_base_y + int((head_box[1] - pad) * scale)
    canvas.paste(s_head, (head_x, head_y), s_head)
    
    # PHASE 1: Say Hi & Waving Arm (Frames 0 to 35)
    if f < 36:
        # Arm waving motion: 3 full cycles
        wave_angle = math.sin(t * 8.5) * 18.0  # -18 to +18 deg
        
        pad = 80
        p_r_arm = Image.new("RGBA", (r_arm_crop.width + pad*2, r_arm_crop.height + pad*2), (0, 0, 0, 0))
        p_r_arm.paste(r_arm_crop, (pad, pad))
        # Shoulder pivot at (580, 270)
        p_x = (580 - r_arm_box[0]) + pad
        p_y = (270 - r_arm_box[1]) + pad
        rot_r_arm = p_r_arm.rotate(wave_angle, resample=Image.BICUBIC, center=(p_x, p_y))
        s_r_arm = rot_r_arm.resize((int(rot_r_arm.width * scale), int(rot_r_arm.height * scale)), Image.Resampling.LANCZOS)
        
        rx = char_base_x + int((r_arm_box[0] - pad) * scale)
        ry = char_base_y + int((r_arm_box[1] - pad) * scale)
        canvas.paste(s_r_arm, (rx, ry), s_r_arm)
        
        # Left arm subtle sway
        s_l_arm = l_arm_crop.resize((int(l_arm_crop.width * scale), int(l_arm_crop.height * scale)), Image.Resampling.LANCZOS)
        lx = char_base_x + int(l_arm_box[0] * scale)
        ly = char_base_y + int(l_arm_box[1] * scale)
        canvas.paste(s_l_arm, (lx, ly), s_l_arm)
        
        # Speech Bubble: Pop in at f=0, stays bright, smoothly fades out at f=30
        if f < 30:
            bubble_alpha = 1.0 if f < 24 else (30 - f) / 6.0
            bx, by, bw, bh = 375, 80 + int(body_breathe_y), 170, 56
            draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(0, 217, 255, int(245 * bubble_alpha)), outline=(255, 255, 255, int(220 * bubble_alpha)), width=2)
            draw.polygon([(bx + 20, by + bh), (bx - 12, by + bh + 14), (bx + 40, by + bh)], fill=(0, 217, 255, int(245 * bubble_alpha)))
            draw.text((bx + 18, by + 12), "Hi...! 👋", fill=(10, 15, 25, int(255 * bubble_alpha)), font=font_hi)
            draw.text((bx + 18, by + 34), "I'm Jeevan", fill=(20, 30, 45, int(255 * bubble_alpha)), font=font_small)

    # PHASE 2: Presenting & Dual-Arm Gesturing (Frames 36 to 120)
    else:
        # Dynamic multi-joint arm gesturing
        l_gest = math.sin((t - 2.4) * 4.0) * 14.0
        r_gest = math.cos((t - 2.4) * 4.0) * 16.0
        
        pad = 80
        # Rotate left presenting arm
        pl = Image.new("RGBA", (p_l_arm_crop.width + pad*2, p_l_arm_crop.height + pad*2), (0, 0, 0, 0))
        pl.paste(p_l_arm_crop, (pad, pad))
        rot_pl = pl.rotate(l_gest, resample=Image.BICUBIC, center=(int(430 - p_l_arm_box[0] + pad), int(290 - p_l_arm_box[1] + pad)))
        s_pl = rot_pl.resize((int(rot_pl.width * scale), int(rot_pl.height * scale)), Image.Resampling.LANCZOS)
        
        # Rotate right presenting arm
        pr = Image.new("RGBA", (p_r_arm_crop.width + pad*2, p_r_arm_crop.height + pad*2), (0, 0, 0, 0))
        pr.paste(p_r_arm_crop, (pad, pad))
        rot_pr = pr.rotate(r_gest, resample=Image.BICUBIC, center=(int(600 - p_r_arm_box[0] + pad), int(290 - p_r_arm_box[1] + pad)))
        s_pr = rot_pr.resize((int(rot_pr.width * scale), int(rot_pr.height * scale)), Image.Resampling.LANCZOS)
        
        lx = char_base_x + int((p_l_arm_box[0] - pad) * scale)
        ly = char_base_y + int((p_l_arm_box[1] - pad) * scale)
        canvas.paste(s_pl, (lx, ly), s_pl)
        
        rx = char_base_x + int((p_r_arm_box[0] - pad) * scale)
        ry = char_base_y + int((p_r_arm_box[1] - pad) * scale)
        canvas.paste(s_pr, (rx, ry), s_pr)

    # 3. Dynamic Rotating Interest UI Header on Top
    topic_idx = ((f - 30) // 15) % len(interests) if f >= 30 else 0
    topic_text, topic_color = interests[topic_idx]
    
    badge_w = 460
    badge_x = int((CANVAS_SIZE - badge_w) / 2)
    badge_y = 28
    
    draw.text((CANVAS_SIZE // 2, badge_y - 12), "✨ MY PASSION & CORE EXPERTISE", fill=(140, 160, 195, 255), font=font_sub, anchor="mm")
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 38], radius=12, fill=(22, 28, 44, 245), outline=topic_color, width=2)
    draw.text((CANVAS_SIZE // 2, badge_y + 19), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # High-quality adaptive quantization for crisp palette
    bg_solid = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23))
    bg_solid.paste(canvas, (0, 0), canvas)
    frame_quant = bg_solid.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Generated {len(frames)} high-precision frames.")
out_file = "cartoon_animated.gif"
frames[0].save(
    out_file,
    save_all=True,
    append_images=frames[1:],
    duration=int(1000 / FPS),
    loop=0,
    optimize=True
)
print(f"Saved {out_file} successfully ({os.path.getsize(out_file) / 1024:.1f} KB)")
