import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("Initializing 3D Character Multi-Phase Animation...")

# Load transparent poses
waving_base = Image.open("pose_waving.png").convert("RGBA")
presenting_base = Image.open("pose_presenting.png").convert("RGBA")

# Isolate the waving arm from waving_base so we can articulate the waving hand smoothly
# Waving arm box approx: x: [500, 760], y: [130, 600] on waving_base (note: in pose_waving, character's left is on right side of image)
# Let's inspect coordinates for waving arm
w_box = (450, 100, 768, 600)
arm_waving = waving_base.crop(w_box)

body_waving = waving_base.copy()
# Clear arm region from body
for y in range(100, 520):
    for x in range(500, 768):
        body_waving.putpixel((x, y), (0, 0, 0, 0))

# Isolate presenting arms so both hands can gesture
# Left arm (viewer left): x: [100, 360], y: [220, 550]
# Right arm (viewer right): x: [420, 750], y: [300, 600]
left_arm_box = (100, 200, 360, 550)
right_arm_box = (420, 280, 720, 600)
left_arm_crop = presenting_base.crop(left_arm_box)
right_arm_crop = presenting_base.crop(right_arm_box)

body_presenting = presenting_base.copy()
for y in range(200, 520):
    for x in range(120, 340):
        body_presenting.putpixel((x, y), (0, 0, 0, 0))
    for x in range(440, 700):
        body_presenting.putpixel((x, y), (0, 0, 0, 0))

interests = [
    ("🧠 LLM Agents & Generative AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive Analytics & ML", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Modern Web", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud Deployment", "#60A5FA"),
]

CANVAS_SIZE = 540
FPS = 15
TOTAL_FRAMES = 120  # 8.0 seconds total loop (30 frames Say Hi + 90 frames Interests)

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 15)
    font_hi = ImageFont.truetype("arialbd.ttf", 19)
    font_small = ImageFont.truetype("arial.ttf", 12)
    font_sub = ImageFont.truetype("arialbd.ttf", 11)
except:
    font_bold = ImageFont.load_default()
    font_hi = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Scaling so the FULL character from top of hair to red sneakers fits comfortably!
# Target height on 540 canvas is ~400px (from y=100 to y=500), leaving room for header and bottom margin
scale_factor = 390.0 / 1376.0

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # Base dark canvas matching GitHub
    frame = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23, 255))
    draw = ImageDraw.Draw(frame)
    
    # Outer card styling
    draw.rounded_rectangle([10, 10, CANVAS_SIZE-10, CANVAS_SIZE-10], radius=22, fill=(18, 24, 38, 255), outline=(48, 54, 61, 255), width=2)
    
    # Subtle ambient background glow behind character
    glow_pulse = 0.5 + 0.5 * math.sin(t * 3.0)
    
    # Body bobbing / natural breathing
    body_bob = math.sin(t * 3.5) * 2.5
    
    # PHASE 1: Say Hi Phase (Frames 0 to 32)
    if f < 32:
        # Arm wave angle
        wave_angle = math.sin(t * 8.0) * 15.0
        
        # Rotate waving arm
        pad = 80
        padded_arm = Image.new("RGBA", (arm_waving.width + pad*2, arm_waving.height + pad*2), (0, 0, 0, 0))
        padded_arm.paste(arm_waving, (pad, pad))
        # Pivot point around shoulder
        p_x = (540 - w_box[0]) + pad
        p_y = (380 - w_box[1]) + pad
        rot_arm = padded_arm.rotate(wave_angle, resample=Image.BICUBIC, center=(p_x, p_y))
        
        # Scale parts
        s_w = int(waving_base.width * scale_factor)
        s_h = int(waving_base.height * scale_factor)
        s_body = body_waving.resize((s_w, s_h), Image.Resampling.LANCZOS)
        s_rot_arm = rot_arm.resize((int(rot_arm.width * scale_factor), int(rot_arm.height * scale_factor)), Image.Resampling.LANCZOS)
        
        # Position centered
        char_x = int((CANVAS_SIZE - s_w) / 2)
        char_y = 105 + int(body_bob)
        
        # Paste body & arm
        frame.paste(s_body, (char_x, char_y), s_body)
        arm_x = char_x + int((w_box[0] - pad) * scale_factor)
        arm_y = char_y + int((w_box[1] - pad) * scale_factor)
        frame.paste(s_rot_arm, (arm_x, arm_y), s_rot_arm)
        
        # "Hi...!" Speech Bubble (only in Phase 1, pops in and fades out before f=32)
        if f < 28:
            # Pop-in scaling
            pop = min(1.0, f / 6.0)
            bx, by, bw, bh = 345, int(65 + body_bob), int(160 * pop), int(54 * pop)
            if bw > 30 and bh > 20:
                draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=14, fill=(0, 217, 255, 245), outline=(255, 255, 255, 210), width=2)
                # Tail pointing to mouth
                draw.polygon([(bx + 20, by + bh), (bx - 12, by + bh + 14), (bx + 40, by + bh)], fill=(0, 217, 255, 245))
                draw.text((bx + 16, by + 12), "Hi...! 👋", fill=(10, 15, 25, 255), font=font_hi)
                draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45, 255), font=font_small)
                
    # PHASE 2: Telling Interests & Both Hands Moving (Frames 32 to 120)
    else:
        # Left and right arm gesturing angles
        left_gesture = math.sin((t - 2.0) * 4.5) * 12.0
        right_gesture = math.cos((t - 2.0) * 4.5) * 14.0
        
        pad = 80
        # Left arm rotate
        p_l = Image.new("RGBA", (left_arm_crop.width + pad*2, left_arm_crop.height + pad*2), (0, 0, 0, 0))
        p_l.paste(left_arm_crop, (pad, pad))
        rot_l = p_l.rotate(left_gesture, resample=Image.BICUBIC, center=(int(200 - left_arm_box[0] + pad), int(340 - left_arm_box[1] + pad)))
        
        # Right arm rotate
        p_r = Image.new("RGBA", (right_arm_crop.width + pad*2, right_arm_crop.height + pad*2), (0, 0, 0, 0))
        p_r.paste(right_arm_crop, (pad, pad))
        rot_r = p_r.rotate(right_gesture, resample=Image.BICUBIC, center=(int(520 - right_arm_box[0] + pad), int(350 - right_arm_box[1] + pad)))
        
        s_w = int(presenting_base.width * scale_factor)
        s_h = int(presenting_base.height * scale_factor)
        s_body = body_presenting.resize((s_w, s_h), Image.Resampling.LANCZOS)
        s_rot_l = rot_l.resize((int(rot_l.width * scale_factor), int(rot_l.height * scale_factor)), Image.Resampling.LANCZOS)
        s_rot_r = rot_r.resize((int(rot_r.width * scale_factor), int(rot_r.height * scale_factor)), Image.Resampling.LANCZOS)
        
        char_x = int((CANVAS_SIZE - s_w) / 2)
        char_y = 105 + int(body_bob)
        
        # Paste body and both animated arms
        frame.paste(s_body, (char_x, char_y), s_body)
        lx = char_x + int((left_arm_box[0] - pad) * scale_factor)
        ly = char_y + int((left_arm_box[1] - pad) * scale_factor)
        frame.paste(s_rot_l, (lx, ly), s_rot_l)
        
        rx = char_x + int((right_arm_box[0] - pad) * scale_factor)
        ry = char_y + int((right_arm_box[1] - pad) * scale_factor)
        frame.paste(s_rot_r, (rx, ry), s_rot_r)

    # Dynamic Facial Blink Gesture (around f=18, f=60, f=100)
    if (17 <= f <= 19) or (58 <= f <= 60) or (98 <= f <= 100):
        # Eyes blink closed line
        ey = char_y + int(210 * scale_factor)
        draw.line([char_x + int(360 * scale_factor), ey, char_x + int(390 * scale_factor), ey], fill=(45, 30, 25, 255), width=2)
        draw.line([char_x + int(420 * scale_factor), ey, char_x + int(450 * scale_factor), ey], fill=(45, 30, 25, 255), width=2)

    # DYNAMIC INTERESTS HEADER ON TOP (Synchronized with Phase 2)
    # Interest topic changes every 15 frames
    topic_idx = ((f - 30) // 15) % len(interests) if f >= 30 else 0
    topic_text, topic_color = interests[topic_idx]
    
    badge_w = 440
    badge_x = int((CANVAS_SIZE - badge_w) / 2)
    badge_y = 35
    
    # Top subtitle
    draw.text((CANVAS_SIZE // 2, 22), "🎯 MY FOCUS & SPECIALIZATION", fill=(140, 160, 190, 255), font=font_sub, anchor="mm")
    
    # Pill container
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 38], radius=12, fill=(24, 30, 48, 245), outline=topic_color, width=2)
    draw.text((CANVAS_SIZE // 2, badge_y + 19), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # Convert RGBA to RGB for optimized palette
    bg_solid = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23))
    bg_solid.paste(frame, (0, 0), frame)
    frame_quant = bg_solid.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Total animation frames generated: {len(frames)}")
output_gif = "cartoon_animated.gif"
frames[0].save(
    output_gif,
    save_all=True,
    append_images=frames[1:],
    duration=int(1000 / FPS),
    loop=0,
    optimize=True
)
print(f"Saved {output_gif} successfully ({os.path.getsize(output_gif) / 1024:.1f} KB)")
