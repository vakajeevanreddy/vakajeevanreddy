import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Load the transparent cartoon
base_char = Image.open("cartoon_transparent.png").convert("RGBA")
cw, ch = base_char.size

# We will separate:
# 1. Right arm & hand: approx region x: [111, 280], y: [320, 780]
# 2. Main body (torso, head, legs) with arm masked out on base
# 3. Head/Face features for blinking/talking

# Arm bounding box relative to base_char
# The character's waving hand is on the viewer's left (character's right)
# Let's crop the waving arm
arm_box = (110, 320, 275, 780)
arm_img = base_char.crop(arm_box)

# Mask out the arm from the body image so we can rotate the arm freely without ghosting
body_img = base_char.copy()
body_draw = ImageDraw.Draw(body_img)
# fill arm area on body with transparent
for y in range(320, 750):
    for x in range(110, 260):
        # preserve torso area on right side of x:260
        if x < 250:
            body_img.putpixel((x, y), (0, 0, 0, 0))

# Also create face variations (eye blink & mouth talk)
# Eye coordinates approx: x: [320, 480], y: [230, 280]
# Mouth coordinates approx: x: [360, 440], y: [315, 360]

interests = [
    ("🧠 LLM Agents & Generative AI", "#00D9FF"),
    ("🔍 RAG Architectures & Vector DBs", "#A78BFA"),
    ("📊 Predictive Analytics & ML", "#34D399"),
    ("🐍 Python, SQL & Data Pipelines", "#F472B6"),
    ("⚡ FastAPI, React & Modern Web", "#FBBF24"),
    ("☁️ MLOps, Docker & Cloud AI", "#60A5FA"),
]

# Canvas properties
CANVAS_SIZE = 560
FPS = 15
TOTAL_FRAMES = 90  # 6 seconds loop (15 fps * 6 = 90 frames, 15 frames per interest topic)

frames = []

try:
    font_large = ImageFont.truetype("arialbd.ttf", 22)
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
    font_small = ImageFont.truetype("arial.ttf", 13)
    font_hi = ImageFont.truetype("arialbd.ttf", 20)
except:
    font_large = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_hi = ImageFont.load_default()

# Target scaled character size
char_scale = 0.38
scaled_cw = int(cw * char_scale)
scaled_ch = int(ch * char_scale)

# Pivot point for arm rotation (shoulder/upper arm joint)
# in unscaled base coordinates: approx (240, 500)
pivot_x = 240 - arm_box[0]
pivot_y = 500 - arm_box[1]

for f in range(TOTAL_FRAMES):
    # Time variable
    t = f / FPS
    
    # 1. Base canvas with rich dark modern background
    frame = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23, 255))
    draw = ImageDraw.Draw(frame)
    
    # Background subtle radial/ambient glow
    # Draw soft glowing gradient circles
    glow_color = (16, 32, 60, 255)
    draw.rounded_rectangle([15, 15, CANVAS_SIZE-15, CANVAS_SIZE-15], radius=24, fill=(18, 24, 38, 255), outline=(48, 54, 61, 255), width=2)
    
    # Gentle breathing/body bobbing
    body_bob_y = math.sin(t * 3.0) * 3.0
    
    # Hand waving angle calculation (fast wave: 2 cycles per second)
    wave_angle = math.sin(t * 7.5) * 16.0  # -16 to +16 degrees
    
    # Rotate arm around pivot
    # Create larger transparent pad for rotation
    pad = 120
    padded_arm = Image.new("RGBA", (arm_img.width + pad*2, arm_img.height + pad*2), (0, 0, 0, 0))
    padded_arm.paste(arm_img, (pad, pad))
    
    # Rotate with smooth bicubic interpolation
    rotated_arm = padded_arm.rotate(wave_angle, resample=Image.BICUBIC, center=(pivot_x + pad, pivot_y + pad))
    
    # Scale body and arm
    s_body = body_img.resize((scaled_cw, scaled_ch), Image.Resampling.LANCZOS)
    s_arm = rotated_arm.resize((int((arm_img.width + pad*2) * char_scale), int((arm_img.height + pad*2) * char_scale)), Image.Resampling.LANCZOS)
    
    # Character position on canvas (centered-lower)
    char_base_x = int((CANVAS_SIZE - scaled_cw) / 2) + 15
    char_base_y = 115 + int(body_bob_y)
    
    # Paste body
    frame.paste(s_body, (char_base_x, char_base_y), s_body)
    
    # Paste rotated arm matching shoulder position
    arm_paste_x = char_base_x + int((arm_box[0] - pad) * char_scale)
    arm_paste_y = char_base_y + int((arm_box[1] - pad) * char_scale)
    frame.paste(s_arm, (arm_paste_x, arm_paste_y), s_arm)
    
    # 2. Dynamic Facial Gestures (Blinking & Mouth movement)
    # Eyes blink periodically: e.g., frames 25-28, 70-73
    is_blinking = (24 <= (f % 45) <= 27)
    if is_blinking:
        # Draw closed curved happy eyelid lines
        eye_y = char_base_y + int(255 * char_scale)
        left_eye_x = char_base_x + int(360 * char_scale)
        right_eye_x = char_base_x + int(430 * char_scale)
        draw.arc([left_eye_x - 14, eye_y - 8, left_eye_x + 14, eye_y + 8], start=20, end=160, fill=(35, 25, 20, 255), width=3)
        draw.arc([right_eye_x - 14, eye_y - 8, right_eye_x + 14, eye_y + 8], start=20, end=160, fill=(35, 25, 20, 255), width=3)
        
    # Mouth subtle talking/happy animation
    mouth_open = (math.sin(t * 9.0) > 0.3) and not is_blinking
    mouth_x = char_base_x + int(395 * char_scale)
    mouth_y = char_base_y + int(336 * char_scale)
    if mouth_open:
        # Happy open speaking mouth
        draw.chord([mouth_x - 10, mouth_y - 5, mouth_x + 10, mouth_y + 11], start=0, end=180, fill=(195, 60, 70, 255), outline=(40, 20, 20, 255), width=2)
    
    # 3. Speech Bubble "Say Hi..! 👋" on Top-Right
    bubble_pulse = math.sin(t * 4.0) * 2.0
    bx, by, bw, bh = 370, 70 + int(bubble_pulse), 140, 54
    # Speech bubble pill
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(0, 217, 255, 240), outline=(255, 255, 255, 200), width=2)
    # Bubble tail pointing to character's mouth
    tail_points = [(bx + 15, by + bh - 2), (bx - 14, by + bh + 16), (bx + 35, by + bh - 2)]
    draw.polygon(tail_points, fill=(0, 217, 255, 240))
    # Hi Text inside bubble
    draw.text((bx + 16, by + 12), "Hi..! 👋", fill=(10, 15, 25, 255), font=font_hi)
    draw.text((bx + 16, by + 34), "I'm Jeevan", fill=(20, 30, 45, 255), font=font_small)

    # 4. Floating Animated Topic Badge ABOVE HEAD
    # Current topic index (changes every 15 frames)
    topic_idx = (f // 15) % len(interests)
    topic_text, topic_color = interests[topic_idx]
    
    # Smooth transition alpha/slide
    topic_frame = f % 15
    if topic_frame < 3:
        slide_offset = (3 - topic_frame) * 4
    elif topic_frame > 12:
        slide_offset = (topic_frame - 12) * -4
    else:
        slide_offset = 0
        
    badge_y = 35 + slide_offset
    badge_w = 420
    badge_x = int((CANVAS_SIZE - badge_w) / 2)
    
    # Header label "🎯 I'M INTERESTED IN:"
    draw.text((CANVAS_SIZE // 2, badge_y - 12), "✨ PASSIONATE ABOUT & BUILDING", fill=(160, 175, 200, 255), font=font_small, anchor="mm")
    
    # Glowing Badge container
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + 40], radius=12, fill=(26, 33, 50, 245), outline=topic_color, width=2)
    draw.text((CANVAS_SIZE // 2, badge_y + 20), topic_text, fill=topic_color, font=font_bold, anchor="mm")
    
    # Subtle connector dots from head to badge
    head_top_x = char_base_x + int(scaled_cw / 2)
    head_top_y = char_base_y + int(70 * char_scale)
    draw.circle((head_top_x, badge_y + 46), 3, fill=(120, 140, 180, 180))
    draw.circle((head_top_x, badge_y + 54), 2, fill=(120, 140, 180, 140))
    
    # Convert RGBA to RGB for GIF palette optimization
    # Alpha composite on solid background
    bg_solid = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (13, 17, 23))
    bg_solid.paste(frame, (0, 0), frame)
    
    frame_quant = bg_solid.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Generated {len(frames)} animation frames.")
output_gif = "cartoon_animated.gif"
frames[0].save(
    output_gif,
    save_all=True,
    append_images=frames[1:],
    duration=int(1000 / FPS),
    loop=0,
    optimize=True
)
print(f"Successfully saved {output_gif} ({os.path.getsize(output_gif) / 1024:.1f} KB)")
