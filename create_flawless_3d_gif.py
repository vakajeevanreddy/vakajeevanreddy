import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

print("Rendering Flawless 3D Pixar Character Animation...")

# Load intact 3D scenes (1024x1024)
scene_w = Image.open("scene_waving.jpg").convert("RGB")
scene_p = Image.open("scene_presenting.jpg").convert("RGB")

TARGET_SIZE = 560

# Resize with high-quality Lanczos filter
img_w = scene_w.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
img_p = scene_p.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)

interests = [
    ("🧠 LLM Agents & Multi-Agent AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive ML & Data Science", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Full-Stack AI", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud Deployment", "#60A5FA"),
]

FPS = 15
# 90 frames = 6 seconds loop
# Frames 0 to 24: Phase 1 (Say Hi - Waving Pose with Speech Bubble)
# Frames 25 to 29: Crisp Quick Transition
# Frames 30 to 90: Phase 2 (Presenting Pose with Both Hands Gesturing & Cycling Badges)
TOTAL_FRAMES = 90

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

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # 1. Select the base intact character pose (NO OVERLAPPING LIMBS = NO 4 HANDS)
    if f < 25:
        # Phase 1: Say Hi / Waving pose
        current_pose = img_w.copy()
        is_phase1 = True
    elif f < 30:
        # Quick, clean cross-fade transition between the two poses
        blend = (f - 25) / 5.0
        arr_w = np.array(img_w, dtype=float)
        arr_p = np.array(img_p, dtype=float)
        blended = (1.0 - blend) * arr_w + blend * arr_p
        current_pose = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8))
        is_phase1 = False
    else:
        # Phase 2: Presenting pose with both hands open
        current_pose = img_p.copy()
        is_phase1 = False
        
    # 2. Apply organic whole-body breathing & dynamic posture sway
    # Vertical breathing expansion (2.5px up/down)
    body_y = int(math.sin(t * 3.6) * 3.0)
    # Subtle horizontal weight shift (1.5px)
    body_x = int(math.sin(t * 2.0) * 1.5)
    
    # Canvas with GitHub dark background #0d1117
    canvas = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), (13, 17, 23))
    canvas.paste(current_pose, (body_x, body_y))
    
    draw = ImageDraw.Draw(canvas)
    
    # Outer modern card outline (clean rounded borders)
    draw.rounded_rectangle([4, 4, TARGET_SIZE-4, TARGET_SIZE-4], radius=18, outline=(48, 54, 61), width=2)
    
    # PHASE 1: Speech Bubble "Hi...! 👋 I'm Jeevan" (Only in Intro, then completely vanishes)
    if is_phase1 and f < 23:
        pop = min(1.0, f / 4.0)
        bx, by, bw, bh = 370, 75 + body_y, int(165 * pop), int(54 * pop)
        if bw > 30 and bh > 20:
            draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=15, fill=(0, 217, 255), outline=(255, 255, 255), width=2)
            draw.polygon([(bx + 20, by + bh), (bx - 12, by + bh + 14), (bx + 40, by + bh)], fill=(0, 217, 255))
            draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25), font=font_hi)
            draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45), font=font_small)

    # PHASE 2: Dynamic Interest Badge Header (Changes every 10 frames in Phase 2)
    if not is_phase1:
        topic_idx = ((f - 30) // 10) % len(interests)
    else:
        topic_idx = 0
        
    topic_text, topic_color = interests[topic_idx]
    
    badge_w = 460
    badge_x = int((TARGET_SIZE - badge_w) / 2)
    badge_y = 26
    
    # Header label
    draw.text((TARGET_SIZE // 2, badge_y - 11), "✨ MY PASSION & CORE EXPERTISE", fill=(140, 160, 195), font=font_sub, anchor="mm")
    
    # Glowing Badge container
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 36], radius=12, fill=(22, 28, 44), outline=topic_color, width=2)
    draw.text((TARGET_SIZE // 2, badge_y + 18), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # Adaptive palette quantization for zero color noise & crisp animation
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
print(f"Saved {out_file} ({os.path.getsize(out_file) / 1024:.1f} KB)")
