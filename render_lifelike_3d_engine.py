import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import scipy.ndimage as ndi

print("Building Realistic 3D Organic Bone & Mesh Deformation Engine...")

# Load source 3D render (1024x1024)
src_img = Image.open("scene_presenting.jpg").convert("RGB")
src_arr = np.array(src_img, dtype=float)
h, w, c = src_arr.shape

# Coordinate meshgrid for 1024x1024
y_grid, x_grid = np.mgrid[0:h, 0:w].astype(float)

# Define landmark centers
HEAD_C = np.array([512.0, 175.0])
R_SHOULDER = np.array([610.0, 310.0])
R_HAND = np.array([710.0, 380.0])
L_SHOULDER = np.array([410.0, 310.0])
L_HAND = np.array([420.0, 480.0])
HIPS = np.array([512.0, 550.0])
L_KNEE = np.array([450.0, 720.0])
R_KNEE = np.array([570.0, 720.0])
MOUTH_C = np.array([512.0, 222.0])
EYES_C = np.array([512.0, 175.0])

interests = [
    ("🧠 LLM Agents & Multi-Agent AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive ML & Decision Analytics", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Full-Stack AI", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud Deployment", "#60A5FA"),
]

FPS = 15
TOTAL_FRAMES = 90  # 6.0 seconds smooth loop
TARGET_SIZE = 560

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
    
    # 1. Initialize deformation displacement field
    dx = np.zeros((h, w), dtype=float)
    dy = np.zeros((h, w), dtype=float)
    
    # --- Whole Body Breathing & Subtle Sway ---
    breathe = math.sin(t * 3.5) * 4.0
    sway = math.sin(t * 2.0) * 3.0
    
    # --- Head Nodding, Tilting & Expression ---
    head_nod = math.sin(t * 3.0) * 5.0
    head_tilt_angle = math.sin(t * 2.2) * 0.04
    
    # Head mask (radial falloff around HEAD_C)
    dist_head = np.sqrt((x_grid - HEAD_C[0])**2 + (y_grid - HEAD_C[1])**2)
    w_head = np.clip(1.0 - dist_head / 140.0, 0.0, 1.0)**2
    
    # Head rotation displacement
    hx_rel = x_grid - HEAD_C[0]
    hy_rel = y_grid - HEAD_C[1]
    dx += w_head * (-hy_rel * head_tilt_angle + sway * 0.5)
    dy += w_head * (hx_rel * head_tilt_angle + head_nod + breathe * 0.8)
    
    # --- Mouth Speaking / Smiling Morph ---
    # Syllable cadence for expressive talking motion
    speech_cadence = max(0.0, math.sin(t * 11.0)) * math.sin(t * 4.5)**2
    dist_mouth = np.sqrt((x_grid - MOUTH_C[0])**2 + (y_grid - MOUTH_C[1])**2)
    w_mouth = np.clip(1.0 - dist_mouth / 45.0, 0.0, 1.0)**2
    # Open mouth vertically
    dy += w_mouth * (y_grid - MOUTH_C[1]) * (speech_cadence * 0.35)
    
    # --- Right Arm & Hand Motion (Active Gesturing / Waving) ---
    r_arm_angle = math.sin(t * 6.5) * 0.12 + (math.sin(t * 13.0) * 0.08 if f < 25 else 0.0)
    dist_r_arm = np.sqrt((x_grid - R_HAND[0])**2 + (y_grid - R_HAND[1])**2)
    w_r_arm = np.clip(1.0 - dist_r_arm / 180.0, 0.0, 1.0)**1.5
    rx_rel = x_grid - R_SHOULDER[0]
    ry_rel = y_grid - R_SHOULDER[1]
    dx += w_r_arm * (-ry_rel * r_arm_angle)
    dy += w_r_arm * (rx_rel * r_arm_angle + math.sin(t * 6.0) * 8.0)
    
    # --- Left Arm & Hand Motion (Dynamic Presenting Gestures) ---
    l_arm_angle = math.cos(t * 5.5) * 0.10
    dist_l_arm = np.sqrt((x_grid - L_HAND[0])**2 + (y_grid - L_HAND[1])**2)
    w_l_arm = np.clip(1.0 - dist_l_arm / 180.0, 0.0, 1.0)**1.5
    lx_rel = x_grid - L_SHOULDER[0]
    ly_rel = y_grid - L_SHOULDER[1]
    dx += w_l_arm * (-ly_rel * l_arm_angle)
    dy += w_l_arm * (lx_rel * l_arm_angle + math.cos(t * 5.0) * 7.0)
    
    # --- Legs & Hips Weight Shift ---
    hip_sway = math.sin(t * 2.5) * 4.0
    dist_hips = np.sqrt((x_grid - HIPS[0])**2 + (y_grid - HIPS[1])**2)
    w_hips = np.clip(1.0 - dist_hips / 220.0, 0.0, 1.0)**2
    dx += w_hips * hip_sway
    
    # Knee flexing & dynamic leg weight shift
    dist_l_knee = np.sqrt((x_grid - L_KNEE[0])**2 + (y_grid - L_KNEE[1])**2)
    dist_r_knee = np.sqrt((x_grid - R_KNEE[0])**2 + (y_grid - R_KNEE[1])**2)
    w_l_knee = np.clip(1.0 - dist_l_knee / 140.0, 0.0, 1.0)**2
    w_r_knee = np.clip(1.0 - dist_r_knee / 140.0, 0.0, 1.0)**2
    dy += w_l_knee * (math.sin(t * 2.5) * 4.0)
    dy += w_r_knee * (-math.sin(t * 2.5) * 4.0)
    
    # 2. Warp image using inverse mapping coordinates
    map_y = y_grid - dy
    map_x = x_grid - dx
    
    warped_arr = np.zeros_like(src_arr)
    for ch_idx in range(3):
        warped_arr[:, :, ch_idx] = ndi.map_coordinates(
            src_arr[:, :, ch_idx], [map_y, map_x], order=1, mode='nearest'
        )
        
    warped_img = Image.fromarray(np.clip(warped_arr, 0, 255).astype(np.uint8))
    
    # Eye Blinking Simulation (Frames 20-22, 55-57, 80-82)
    is_blinking = (20 <= (f % 35) <= 22)
    if is_blinking:
        draw_blink = ImageDraw.Draw(warped_img)
        # Smooth anime eye blink arcs
        draw_blink.arc([475, 172, 502, 185], start=10, end=170, fill=(35, 20, 15), width=4)
        draw_blink.arc([528, 172, 555, 185], start=10, end=170, fill=(35, 20, 15), width=4)

    # 3. Resize and place on modern studio dark card
    scaled_img = warped_img.resize((TARGET_SIZE, TARGET_SIZE), Image.Resampling.LANCZOS)
    
    canvas = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), (13, 17, 23))
    canvas.paste(scaled_img, (0, 0))
    draw = ImageDraw.Draw(canvas)
    
    # Card outer border
    draw.rounded_rectangle([4, 4, TARGET_SIZE-4, TARGET_SIZE-4], radius=18, outline=(48, 54, 61), width=2)
    
    # PHASE 1: Speech Bubble "Hi...! 👋 I'm Jeevan" (Active 0s to 1.8s, pops in, stays bright, fades out)
    if f < 25:
        pop = min(1.0, f / 4.0)
        bx, by, bw, bh = 370, 75 + int(head_nod * 0.5), int(165 * pop), int(54 * pop)
        if bw > 30 and bh > 20:
            draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=15, fill=(0, 217, 255), outline=(255, 255, 255), width=2)
            draw.polygon([(bx + 20, by + bh), (bx - 12, by + bh + 14), (bx + 40, by + bh)], fill=(0, 217, 255))
            draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25), font=font_hi)
            draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45), font=font_small)

    # PHASE 2: Dynamic Rotating Interest Banner (Changes every 15 frames)
    topic_idx = ((f - 15) // 15) % len(interests) if f >= 15 else 0
    topic_text, topic_color = interests[topic_idx]
    
    badge_w = 460
    badge_x = int((TARGET_SIZE - badge_w) / 2)
    badge_y = 26
    
    draw.text((TARGET_SIZE // 2, badge_y - 11), "✨ MY PASSION & CORE EXPERTISE", fill=(140, 160, 195), font=font_sub, anchor="mm")
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 36], radius=12, fill=(22, 28, 44), outline=topic_color, width=2)
    draw.text((TARGET_SIZE // 2, badge_y + 18), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # Palette quantization
    frame_quant = canvas.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Generated {len(frames)} lifelike deformed animation frames.")
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
