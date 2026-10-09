import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("Rendering True Walking-In + Presentation Animation...")

# Load transparent character images
char_walk = Image.open("clean_3d_char.png").convert("RGBA")
char_present = Image.open("clean_3d_presenting.png").convert("RGBA")

# Bounding box of character is (277, 61, 784, 984)
# Crop the character tightly to its bounding box
bbox_w = char_walk.getbbox()
bbox_p = char_present.getbbox()

char_w_tight = char_walk.crop(bbox_w)
char_p_tight = char_present.crop(bbox_p)

# We can also isolate the left leg and right leg for walking stride articulation:
# In char_w_tight:
# Left leg (viewer left): x: [0, 240], y: [480, 923]
# Right leg (viewer right): x: [240, 507], y: [480, 923]
# Upper body (head + torso + arms): y: [0, 480]

cw, ch = char_w_tight.size
upper_body = char_w_tight.crop((0, 0, cw, 500))
left_leg = char_w_tight.crop((0, 480, int(cw * 0.52), ch))
right_leg = char_w_tight.crop((int(cw * 0.48), 480, cw, ch))

CANVAS_SIZE = 580
FPS = 15
TOTAL_FRAMES = 120  # 8.0 seconds loop

# --- SCENE TIMELINE ---
# 1. Frames 0 to 36 (0.0s - 2.4s): WALKING IN from left of screen into center
#    - Walks across X: from -200px (off-screen left) to center
#    - Realistic walking stride: alternating legs scissor swing, body up/down walking bounce, counter arm swing
# 2. Frames 36 to 48 (2.4s - 3.2s): ARRIVES in center, plants feet, smiles & waves right hand
# 3. Frames 48 to 120 (3.2s - 8.0s): PRESENTING INTERESTS at center
#    - Hands gesturing forward passionately, explaining specializations
#    - Rotating interest headers slide in on top

interests = [
    ("🧠 LLM Agents & Multi-Agent AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive ML & Decision Analytics", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Full-Stack AI", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud Deployment", "#60A5FA"),
]

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
    font_hi = ImageFont.truetype("arialbd.ttf", 19)
    font_small = ImageFont.truetype("arial.ttf", 12)
    font_sub = ImageFont.truetype("arialbd.ttf", 11)
except:
    font_bold = ImageFont.load_default()
    font_hi = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Target scaled size for character (fits comfortably from head to shoes on canvas)
target_h = 420
scale = target_h / float(ch)
scaled_cw = int(cw * scale)
scaled_ch = int(ch * scale)

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # 1. Base modern dark card canvas (#0d1117 / #161b22)
    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Outer card border
    draw.rounded_rectangle([6, 6, CANVAS_SIZE-6, CANVAS_SIZE-6], radius=20, fill=(16, 21, 30, 255), outline=(48, 54, 61, 255), width=2)
    
    # Center ambient studio spotlight on floor
    draw.ellipse([CANVAS_SIZE//2 - 160, CANVAS_SIZE - 90, CANVAS_SIZE//2 + 160, CANVAS_SIZE - 40], fill=(22, 34, 55, 140))
    
    # --- PHASE 1: WALKING IN FROM LEFT TO CENTER (Frames 0 to 36) ---
    if f < 36:
        # Walk progress from 0.0 (left) to 1.0 (center)
        # Easing: smooth deceleration as he reaches center
        p = f / 36.0
        ease_p = math.sin(p * math.pi / 2.0)  # smooth ease-out
        
        # X position: from -160 to center
        center_x = (CANVAS_SIZE - scaled_cw) // 2
        start_x = -140
        current_x = int(start_x + (center_x - start_x) * ease_p)
        
        # Walking cycle physics (3 full steps per second = 6 Hz)
        walk_phase = (f / 36.0) * (3.5 * 2.0 * math.pi)
        
        # Walking vertical bounce (up on single-leg support, down on double-support)
        walk_bounce = abs(math.sin(walk_phase)) * 8.0
        current_y = 110 - int(walk_bounce)
        
        # Leg stride scissor angles
        l_leg_angle = math.sin(walk_phase) * 18.0
        r_leg_angle = -math.sin(walk_phase) * 18.0
        
        # Render walking character with articulated legs
        pad = 60
        # Left leg rotate around hip joint
        p_l = Image.new("RGBA", (left_leg.width + pad*2, left_leg.height + pad*2), (0, 0, 0, 0))
        p_l.paste(left_leg, (pad, pad))
        rot_l = p_l.rotate(l_leg_angle, resample=Image.BICUBIC, center=(int(left_leg.width*0.5 + pad), pad))
        
        # Right leg rotate around hip joint
        p_r = Image.new("RGBA", (right_leg.width + pad*2, right_leg.height + pad*2), (0, 0, 0, 0))
        p_r.paste(right_leg, (pad, pad))
        rot_r = p_r.rotate(r_leg_angle, resample=Image.BICUBIC, center=(int(right_leg.width*0.5 + pad), pad))
        
        # Scale parts
        s_upper = upper_body.resize((scaled_cw, int(upper_body.height * scale)), Image.Resampling.LANCZOS)
        s_rot_l = rot_l.resize((int(rot_l.width * scale), int(rot_l.height * scale)), Image.Resampling.LANCZOS)
        s_rot_r = rot_r.resize((int(rot_r.width * scale), int(rot_r.height * scale)), Image.Resampling.LANCZOS)
        
        # Paste legs first (hip attachment point at y=480)
        hip_y = current_y + int(480 * scale)
        canvas.paste(s_rot_l, (current_x - int(pad * scale), hip_y - int(pad * scale)), s_rot_l)
        canvas.paste(s_rot_r, (current_x + int(cw * 0.48 * scale) - int(pad * scale), hip_y - int(pad * scale)), s_rot_r)
        
        # Paste upper body on top
        canvas.paste(s_upper, (current_x, current_y), s_upper)
        
        # Walking shadow on floor following character
        shadow_w = int(scaled_cw * 0.9)
        draw.ellipse([current_x + 5, CANVAS_SIZE - 65, current_x + shadow_w, CANVAS_SIZE - 45], fill=(10, 14, 20, 200))
        
        # Top walk-in intro text
        draw.text((CANVAS_SIZE // 2, 35), "👋 WELCOME TO MY PORTFOLIO", fill=(0, 217, 255, 255), font=font_bold, anchor="mm")

    # --- PHASE 2: ARRIVED AT CENTER & WAVING / SAY HI (Frames 36 to 52) ---
    elif f < 52:
        center_x = (CANVAS_SIZE - scaled_cw) // 2
        char_y = 105
        
        # Stand solidly at center
        s_char = char_w_tight.resize((scaled_cw, scaled_ch), Image.Resampling.LANCZOS)
        canvas.paste(s_char, (center_x, char_y), s_char)
        
        # Ground shadow
        shadow_w = int(scaled_cw * 0.9)
        draw.ellipse([center_x + 5, CANVAS_SIZE - 65, center_x + shadow_w, CANVAS_SIZE - 45], fill=(10, 14, 20, 200))
        
        # Speech Bubble pops in at center
        bx, by, bw, bh = center_x + scaled_cw - 20, 75, 160, 54
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=15, fill=(0, 217, 255, 250), outline=(255, 255, 255, 220), width=2)
        draw.polygon([(bx + 18, by + bh), (bx - 12, by + bh + 14), (bx + 38, by + bh)], fill=(0, 217, 255, 250))
        draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25, 255), font=font_hi)
        draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45, 255), font=font_small)
        
        draw.text((CANVAS_SIZE // 2, 35), "✨ LET'S EXPLORE MY SKILLS & PROJECTS", fill=(160, 180, 210, 255), font=font_sub, anchor="mm")

    # --- PHASE 3: PRESENTING SPECIALIZATIONS AT CENTER (Frames 52 to 120) ---
    else:
        # Scale presenting character
        pw, ph = char_p_tight.size
        p_scale = target_h / float(ph)
        scaled_pw = int(pw * p_scale)
        scaled_ph = int(ph * p_scale)
        
        center_x = (CANVAS_SIZE - scaled_pw) // 2
        
        # Subtle organic breathing & gesture sway
        breathe = math.sin((f - 52) * 0.25) * 3.0
        char_y = 105 + int(breathe)
        
        s_pres = char_p_tight.resize((scaled_pw, scaled_ph), Image.Resampling.LANCZOS)
        canvas.paste(s_pres, (center_x, char_y), s_pres)
        
        # Ground shadow
        shadow_w = int(scaled_pw * 0.9)
        draw.ellipse([center_x + 5, CANVAS_SIZE - 65, center_x + shadow_w, CANVAS_SIZE - 45], fill=(10, 14, 20, 200))
        
        # DYNAMIC SPECIALIZATION BADGE (Cycles every 11 frames)
        topic_idx = ((f - 52) // 11) % len(interests)
        topic_text, topic_color = interests[topic_idx]
        
        badge_w = 460
        badge_x = int((CANVAS_SIZE - badge_w) / 2)
        badge_y = 28
        
        # Header subtitle
        draw.text((CANVAS_SIZE // 2, badge_y - 12), "🎯 MY FOCUS & SPECIALIZATION", fill=(140, 160, 195, 255), font=font_sub, anchor="mm")
        # Glowing Badge container
        draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 38], radius=12, fill=(22, 28, 44, 250), outline=topic_color, width=2)
        draw.text((CANVAS_SIZE // 2, badge_y + 19), topic_text, fill=topic_color, font=font_bold, anchor="mm")

    # Convert to RGB and adaptive palette for small file size and crisp rendering
    bg_solid = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23))
    bg_solid.paste(canvas, (0, 0), canvas)
    frame_quant = bg_solid.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Generated {len(frames)} walking-in animation frames.")
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
