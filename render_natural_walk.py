import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("Rendering Natural Walking Entry & Clean Presentation...")

# Load intact high-res 3D character images
char_waving = Image.open("clean_3d_char.png").convert("RGBA")
char_presenting = Image.open("clean_3d_presenting.png").convert("RGBA")

# Crop to tight bounds
bbox_w = char_waving.getbbox()
bbox_p = char_presenting.getbbox()

cw_img = char_waving.crop(bbox_w)
cp_img = char_presenting.crop(bbox_p)

CANVAS_SIZE = 580
FPS = 15
TOTAL_FRAMES = 105  # 7.0 seconds clean loop

# Scale character so full height (head to shoes) is 420px
target_h = 420
scale_w = target_h / float(cw_img.height)
scaled_w_w = int(cw_img.width * scale_w)
scaled_w_h = target_h

scale_p = target_h / float(cp_img.height)
scaled_p_w = int(cp_img.width * scale_p)
scaled_p_h = target_h

s_waving = cw_img.resize((scaled_w_w, scaled_w_h), Image.Resampling.LANCZOS)
s_presenting = cp_img.resize((scaled_p_w, scaled_p_h), Image.Resampling.LANCZOS)

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

center_w_x = (CANVAS_SIZE - scaled_w_w) // 2
center_p_x = (CANVAS_SIZE - scaled_p_w) // 2

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # 1. Base dark studio card (#0d1117 / #161b22)
    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Outer card border
    draw.rounded_rectangle([6, 6, CANVAS_SIZE-6, CANVAS_SIZE-6], radius=20, fill=(16, 21, 30, 255), outline=(48, 54, 61, 255), width=2)
    
    # Ambient floor studio light
    draw.ellipse([CANVAS_SIZE//2 - 170, CANVAS_SIZE - 90, CANVAS_SIZE//2 + 170, CANVAS_SIZE - 40], fill=(22, 34, 55, 130))
    
    # --- PHASE 1: NATURAL WALKING IN (Frames 0 to 28) ---
    # Walks across from left (-120px) to center with natural walking stride pace
    if f < 28:
        # Smooth ease-out walk progress
        progress = f / 28.0
        ease = math.sin(progress * math.pi / 2.0)
        
        start_x = -130
        current_x = int(start_x + (center_w_x - start_x) * ease)
        
        # Natural vertical step cadence (1.5 steps per sec = smooth step bounce, not dancing)
        step_bounce = abs(math.sin(progress * 4.0 * math.pi)) * 4.0
        current_y = 110 - int(step_bounce)
        
        # Ground shadow follows feet
        shadow_w = int(scaled_w_w * 0.85)
        draw.ellipse([current_x + 10, CANVAS_SIZE - 60, current_x + 10 + shadow_w, CANVAS_SIZE - 42], fill=(10, 14, 20, 220))
        
        # Draw intact character walking smoothly
        canvas.paste(s_waving, (current_x, current_y), s_waving)
        
        # Walk-in header
        draw.text((CANVAS_SIZE // 2, 35), "👋 WELCOME TO MY PORTFOLIO", fill=(0, 217, 255, 255), font=font_bold, anchor="mm")

    # --- PHASE 2: ARRIVED AT CENTER & SAYS HI (Frames 28 to 44) ---
    elif f < 44:
        current_x = center_w_x
        current_y = 110
        
        # Ground shadow
        shadow_w = int(scaled_w_w * 0.85)
        draw.ellipse([current_x + 10, CANVAS_SIZE - 60, current_x + 10 + shadow_w, CANVAS_SIZE - 42], fill=(10, 14, 20, 220))
        
        canvas.paste(s_waving, (current_x, current_y), s_waving)
        
        # Speech Bubble pops in smoothly
        bx, by, bw, bh = current_x + scaled_w_w - 25, 75, 160, 54
        draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=15, fill=(0, 217, 255, 250), outline=(255, 255, 255, 220), width=2)
        draw.polygon([(bx + 18, by + bh), (bx - 12, by + bh + 14), (bx + 38, by + bh)], fill=(0, 217, 255, 250))
        draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25, 255), font=font_hi)
        draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45, 255), font=font_small)
        
        draw.text((CANVAS_SIZE // 2, 35), "✨ LET'S EXPLORE MY SKILLS & PROJECTS", fill=(160, 180, 210, 255), font=font_sub, anchor="mm")

    # --- PHASE 3: PRESENTING SPECIALIZATIONS AT CENTER (Frames 44 to 105) ---
    else:
        current_x = center_p_x
        current_y = 110
        
        # Ground shadow
        shadow_w = int(scaled_p_w * 0.85)
        draw.ellipse([current_x + 10, CANVAS_SIZE - 60, current_x + 10 + shadow_w, CANVAS_SIZE - 42], fill=(10, 14, 20, 220))
        
        canvas.paste(s_presenting, (current_x, current_y), s_presenting)
        
        # DYNAMIC ROTATING SPECIALIZATION BADGES (Changes every 10 frames)
        topic_idx = ((f - 44) // 10) % len(interests)
        topic_text, topic_color = interests[topic_idx]
        
        badge_w = 460
        badge_x = int((CANVAS_SIZE - badge_w) / 2)
        badge_y = 28
        
        # Header subtitle
        draw.text((CANVAS_SIZE // 2, badge_y - 12), "🎯 MY FOCUS & SPECIALIZATION", fill=(140, 160, 195, 255), font=font_sub, anchor="mm")
        # Glowing Badge container
        draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 38], radius=12, fill=(22, 28, 44, 250), outline=topic_color, width=2)
        draw.text((CANVAS_SIZE // 2, badge_y + 19), topic_text, fill=topic_color, font=font_bold, anchor="mm")

    # Optimized palette quantization for crisp visual quality
    bg_solid = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23))
    bg_solid.paste(canvas, (0, 0), canvas)
    frame_quant = bg_solid.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Generated {len(frames)} frames.")
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
