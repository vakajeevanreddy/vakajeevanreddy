import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("Rendering Pristine Studio 3D Presentation Card...")

# Load intact 3D character images
scene_w = Image.open("scene_waving.jpg").convert("RGB")
scene_p = Image.open("scene_presenting.jpg").convert("RGB")

TARGET_SIZE = 560
img_w = scene_w.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
img_p = scene_p.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)

interests = [
    ("🧠 LLM Agents & Multi-Agent AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive ML & Decision Analytics", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Full-Stack AI", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud Deployment", "#60A5FA"),
]

FPS = 15
TOTAL_FRAMES = 90  # 6.0 seconds loop

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
    font_hi = ImageFont.truetype("arialbd.ttf", 20)
    font_small = ImageFont.truetype("arial.ttf", 12)
    font_sub = ImageFont.truetype("arialbd.ttf", 11)
except:
    font_bold = ImageFont.load_default()
    font_hi = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_sub = ImageFont.load_default()

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # 1. Base modern dark card canvas (#0d1117 / #161b22)
    canvas = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), (13, 17, 23))
    
    # PHASE 1: GREETING & WAVE (Frames 0 to 26 - 1.7s)
    # Character in centered waving pose greeting visitor
    if f < 24:
        current_img = img_w
        is_greeting = True
    elif f < 28:
        # Smooth cinematic cross-blend transition
        prog = (f - 24) / 4.0
        arr_w = np.array(img_w, dtype=float)
        arr_p = np.array(img_p, dtype=float)
        blended = (1.0 - prog) * arr_w + prog * arr_p
        current_img = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8))
        is_greeting = False
    else:
        # PHASE 2: PRESENTING INTERESTS (Frames 28 to 90)
        # Character in centered presenting pose with both hands gesturing
        current_img = img_p
        is_greeting = False

    canvas.paste(current_img, (0, 0))
    draw = ImageDraw.Draw(canvas)
    
    # Outer modern card outline
    draw.rounded_rectangle([4, 4, TARGET_SIZE-4, TARGET_SIZE-4], radius=18, outline=(48, 54, 61), width=2)
    
    # PHASE 1: Speech Bubble "Hi...! 👋 I'm Jeevan" (Only in Intro, pops in and cleanly dissolves)
    if is_greeting and f < 22:
        pop = min(1.0, f / 4.0)
        bx, by, bw, bh = 370, 75, int(165 * pop), int(54 * pop)
        if bw > 30 and bh > 20:
            draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=15, fill=(0, 217, 255), outline=(255, 255, 255), width=2)
            draw.polygon([(bx + 20, by + bh), (bx - 12, by + bh + 14), (bx + 40, by + bh)], fill=(0, 217, 255))
            draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25), font=font_hi)
            draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45), font=font_small)

    # PHASE 2: Dynamic Interest Badge Header (Changes every 10 frames in presenting phase)
    if not is_greeting:
        topic_idx = ((f - 28) // 10) % len(interests)
    else:
        topic_idx = 0
        
    topic_text, topic_color = interests[topic_idx]
    
    badge_w = 460
    badge_x = int((TARGET_SIZE - badge_w) / 2)
    badge_y = 26
    
    # Subtitle Header
    draw.text((TARGET_SIZE // 2, badge_y - 11), "✨ MY PASSION & CORE EXPERTISE", fill=(140, 160, 195), font=font_sub, anchor="mm")
    
    # Glowing Badge container
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 36], radius=12, fill=(22, 28, 44), outline=topic_color, width=2)
    draw.text((TARGET_SIZE // 2, badge_y + 18), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # Convert with adaptive palette for crisp studio colors
    frame_quant = canvas.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Rendered {len(frames)} frames.")
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
