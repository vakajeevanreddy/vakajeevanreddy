import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("Rendering Studio-Grade 3D Pixar Animation...")

img_waving = Image.open("scene_waving.jpg").convert("RGB")
img_presenting = Image.open("scene_presenting.jpg").convert("RGB")

TARGET_SIZE = 580
img_w = img_waving.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
img_p = img_presenting.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)

arr_w = np.array(img_w, dtype=float)
arr_p = np.array(img_p, dtype=float)

interests = [
    ("🧠 LLM Agents & Generative AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive ML & Data Science", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Modern Web", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud AI", "#60A5FA"),
]

FPS = 15
TOTAL_FRAMES = 120  # 8 seconds loop

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

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # Motion blending between Pose 1 (Say Hi) and Pose 2 (Both Hands Presenting)
    # Frames 0-30: Pose 1 (Say Hi) with waving dynamics
    # Frames 30-45: Smooth cinematic morph transition into Pose 2
    # Frames 45-120: Pose 2 (Both Hands Presenting) with fluid gesturing & breathing
    if f < 28:
        blend = 0.0
    elif f < 42:
        # Smooth S-curve transition
        prog = (f - 28) / 14.0
        blend = 0.5 - 0.5 * math.cos(prog * math.pi)
    else:
        blend = 1.0

    # Cross-blended base image
    blended_arr = (1.0 - blend) * arr_w + blend * arr_p
    base_frame = Image.fromarray(np.clip(blended_arr, 0, 255).astype(np.uint8))
    
    # Apply natural subtle breathing / body sway
    sway_y = int(math.sin(t * 3.5) * 3.0)
    sway_x = int(math.sin(t * 2.0) * 1.5)
    
    # Canvas setup with smooth rounded dark card
    frame = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), (13, 17, 23))
    frame.paste(base_frame, (sway_x, sway_y))
    
    draw = ImageDraw.Draw(frame)
    
    # Outer modern card outline
    draw.rounded_rectangle([6, 6, TARGET_SIZE-6, TARGET_SIZE-6], radius=20, outline=(48, 54, 61), width=2)
    
    # PHASE 1: Say Hi Speech Bubble (only active in frames 0 to 26, then cleanly fades out)
    if f < 26:
        pop = min(1.0, f / 5.0)
        bx, by, bw, bh = 380, 75 + sway_y, int(165 * pop), int(56 * pop)
        if bw > 30 and bh > 20:
            # High-contrast bright cyan speech bubble
            draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=15, fill=(0, 217, 255), outline=(255, 255, 255), width=2)
            # Bubble tail pointing to mouth
            draw.polygon([(bx + 20, by + bh), (bx - 12, by + bh + 14), (bx + 40, by + bh)], fill=(0, 217, 255))
            draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25), font=font_hi)
            draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45), font=font_small)

    # PHASE 2: Dynamic Rotating Interest Banner (Synchronized with presenting phase)
    topic_idx = ((f - 28) // 15) % len(interests) if f >= 28 else 0
    topic_text, topic_color = interests[topic_idx]
    
    badge_w = 460
    badge_x = int((TARGET_SIZE - badge_w) / 2)
    badge_y = 28
    
    # Top Category Subtitle
    draw.text((TARGET_SIZE // 2, badge_y - 12), "✨ MY PASSION & CORE EXPERTISE", fill=(140, 160, 195), font=font_sub, anchor="mm")
    
    # Glowing Badge container
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 38], radius=12, fill=(22, 28, 44), outline=topic_color, width=2)
    draw.text((TARGET_SIZE // 2, badge_y + 19), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # Optimized palette quantization for crisp colors & zero artifacts
    frame_quant = frame.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Rendered {len(frames)} frames successfully.")
out_file = "cartoon_animated.gif"
frames[0].save(
    out_file,
    save_all=True,
    append_images=frames[1:],
    duration=int(1000 / FPS),
    loop=0,
    optimize=True
)
print(f"Saved {out_file} ({os.path.getsize(out_file) / 1024:.1f} KB)")
