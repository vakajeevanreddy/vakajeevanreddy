import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("Rendering Animated Key Skills Circular Pinwheel GIF...")

# Load downloaded SVG icons converted or loaded
# Let's write a helper to render icon textures
W, H = 840, 560
CX, CY = W // 2, H // 2

# We have PNG icons or we can draw high-res stylized badges
# Let's check available fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 14)
    font_hub = ImageFont.truetype("arialbd.ttf", 16)
    font_hub_sub = ImageFont.truetype("arialbd.ttf", 13)
    font_icon = ImageFont.truetype("arialbd.ttf", 11)
    font_coord = ImageFont.truetype("arial.ttf", 12)
except:
    font_title = ImageFont.load_default()
    font_hub = ImageFont.load_default()
    font_hub_sub = ImageFont.load_default()
    font_icon = ImageFont.load_default()
    font_coord = ImageFont.load_default()

# 4 Quadrants configuration
quadrants = [
    {
        "name": "🤖 Data Science & AI/ML",
        "coord": "(0,0)",
        "color": (255, 87, 34),
        "border": (255, 112, 67),
        "rect": (25, 25, 285, 260),
        "skills": [
            ("Python", "#3776AB"), ("PyTorch", "#EE4C2C"), ("TensorFlow", "#FF6F00"),
            ("Scikit-Learn", "#F7931E"), ("Pandas", "#150458"), ("NumPy", "#013243")
        ]
    },
    {
        "name": "🗄️ Databases & Storage",
        "coord": "(0,1)",
        "color": (171, 71, 188),
        "border": (186, 104, 200),
        "rect": (555, 25, 815, 260),
        "skills": [
            ("PostgreSQL", "#4169E1"), ("MongoDB", "#47A248"), ("SQLite", "#003B57"),
            ("Redis", "#DC382D"), ("MySQL", "#4479A1"), ("Vector DB", "#00BCD4")
        ]
    },
    {
        "name": "🌐 Backend, Web & APIs",
        "coord": "(1,0)",
        "color": (0, 188, 212),
        "border": (77, 208, 225),
        "rect": (25, 300, 285, 535),
        "skills": [
            ("FastAPI", "#009688"), ("Flask", "#000000"), ("React", "#61DAFB"),
            ("JavaScript", "#F7DF1E"), ("HTML5/CSS3", "#E34F26"), ("REST APIs", "#FF9800")
        ]
    },
    {
        "name": "☁️ DevOps, Cloud & Tools",
        "coord": "(1,1)",
        "color": (41, 182, 246),
        "border": (129, 212, 250),
        "rect": (555, 300, 815, 535),
        "skills": [
            ("Docker", "#2496ED"), ("Git", "#F05032"), ("GitHub Actions", "#2088FF"),
            ("AWS", "#FF9900"), ("Linux", "#FCC624"), ("VS Code", "#007ACC")
        ]
    }
]

FPS = 15
TOTAL_FRAMES = 60  # 4 seconds smooth looping wheel

# 8 Pinwheel blade colors
blade_colors = [
    (255, 87, 34),   # Orange
    (255, 152, 0),  # Amber
    (255, 193, 7),  # Yellow
    (139, 195, 74), # Lime
    (0, 188, 212),  # Cyan
    (33, 150, 243), # Blue
    (156, 39, 176), # Purple
    (233, 30, 99),  # Pink
]

frames = []

for f in range(TOTAL_FRAMES):
    t = f / FPS
    
    # 1. Base dark background
    canvas = Image.new("RGB", (W, H), (13, 17, 23))
    draw = ImageDraw.Draw(canvas)
    
    # Outer frame
    draw.rounded_rectangle([4, 4, W-4, H-4], radius=20, fill=(18, 24, 38), outline=(48, 54, 61), width=2)
    
    # Assembly progress for initial 15 frames (1.0s on refresh)
    assembly_p = min(1.0, f / 14.0)
    ease_in_out = math.sin(assembly_p * math.pi / 2.0)
    
    # 2. Draw 4 Quadrant Cards with assembly motion
    for idx, q in enumerate(quadrants):
        x0, y0, x1, y1 = q["rect"]
        qw, qh = x1 - x0, y1 - y0
        
        # Quadrant directional offset for fly-in on load
        if idx == 0:   # (0,0) Top-Left
            off_x = int(-80 * (1.0 - ease_in_out))
            off_y = int(-60 * (1.0 - ease_in_out))
        elif idx == 1: # (0,1) Top-Right
            off_x = int(80 * (1.0 - ease_in_out))
            off_y = int(-60 * (1.0 - ease_in_out))
        elif idx == 2: # (1,0) Bottom-Left
            off_x = int(-80 * (1.0 - ease_in_out))
            off_y = int(60 * (1.0 - ease_in_out))
        else:          # (1,1) Bottom-Right
            off_x = int(80 * (1.0 - ease_in_out))
            off_y = int(60 * (1.0 - ease_in_out))
            
        cur_x0, cur_y0 = x0 + off_x, y0 + off_y
        cur_x1, cur_y1 = x1 + off_x, y1 + off_y
        
        # Card body
        draw.rounded_rectangle([cur_x0, cur_y0, cur_x1, cur_y1], radius=16, fill=(24, 31, 46), outline=q["border"], width=2)
        # Header banner
        draw.rounded_rectangle([cur_x0, cur_y0, cur_x1, cur_y0 + 34], radius=16, fill=q["color"])
        draw.rectangle([cur_x0, cur_y0 + 20, cur_x1, cur_y0 + 34], fill=q["color"])
        
        # Title and (x,y) coordinate tag
        draw.text((cur_x0 + 12, cur_y0 + 10), q["name"], fill=(255, 255, 255), font=font_title)
        draw.text((cur_x1 - 12, cur_y0 + 10), q["coord"], fill=(255, 255, 255), font=font_coord, anchor="ra")
        
        # 6 Square Skill Badges inside each quadrant
        col_w = (qw - 24) // 3
        row_h = (qh - 46) // 2
        
        for s_idx, (skill_name, badge_color) in enumerate(q["skills"]):
            r = s_idx // 3
            c = s_idx % 3
            
            bx0 = cur_x0 + 12 + c * col_w + 4
            by0 = cur_y0 + 42 + r * row_h + 4
            bx1 = bx0 + col_w - 8
            by1 = by0 + row_h - 8
            
            # Subtle floating badge animation
            badge_float = math.sin(t * 3.0 + s_idx * 0.8) * 2.0
            
            # Square skill badge
            draw.rounded_rectangle([bx0, by0 + badge_float, bx1, by1 + badge_float], radius=10, fill=(32, 40, 60), outline=(60, 72, 100), width=1)
            # Accent color bar on top of square badge
            draw.rounded_rectangle([bx0 + 2, by0 + 2 + badge_float, bx1 - 2, by0 + 7 + badge_float], radius=4, fill=badge_color)
            
            # Skill label centered in badge
            draw.text(((bx0 + bx1)//2, (by0 + by1)//2 + 4 + badge_float), skill_name, fill=(230, 240, 255), font=font_icon, anchor="mm")

    # 3. Central Circular Pinwheel Wheel (Rotating continuous aperture blades)
    wheel_rot = (f / float(TOTAL_FRAMES)) * (2.0 * math.pi)
    
    # Draw 8 overlapping curved spiral blades around center (CX, CY)
    num_blades = 8
    radius_outer = 110
    radius_inner = 50
    
    for b_idx in range(num_blades):
        blade_angle = wheel_rot + (b_idx * 2.0 * math.pi / num_blades)
        color = blade_colors[b_idx % len(blade_colors)]
        
        # Arc points
        points = []
        for step in range(12):
            ang = blade_angle + (step / 11.0) * (math.pi / 2.2)
            r = radius_inner + (step / 11.0) * (radius_outer - radius_inner)
            px = CX + r * math.cos(ang)
            py = CY + r * math.sin(ang)
            points.append((px, py))
            
        # Complete sector back to center
        points.append((CX, CY))
        draw.polygon(points, fill=color)

    # 4. Central Circular Hub "KEY SKILLS"
    hub_pulse = math.sin(t * 3.0) * 2.0
    r_hub = 60 + hub_pulse
    
    # Outer glow ring
    draw.ellipse([CX - r_hub - 6, CY - r_hub - 6, CX + r_hub + 6, CY + r_hub + 6], outline=(0, 217, 255), width=3)
    # Inner hub circle
    draw.ellipse([CX - r_hub, CY - r_hub, CX + r_hub, CY + r_hub], fill=(22, 28, 44), outline=(48, 54, 61), width=2)
    
    # Text in Hub
    draw.text((CX, CY - 10), "KEY", fill=(0, 217, 255), font=font_hub, anchor="mm")
    draw.text((CX, CY + 12), "SKILLS", fill=(255, 255, 255), font=font_hub, anchor="mm")
    draw.circle((CX, CY + 26), 3, fill=(0, 217, 255))
    
    # Quantize to 128 colors for crisp colors
    frame_quant = canvas.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    frames.append(frame_quant)

print(f"Rendered {len(frames)} frames.")
out_file = "key_skills_wheel.gif"
frames[0].save(
    out_file,
    save_all=True,
    append_images=frames[1:],
    duration=int(1000 / FPS),
    loop=0,
    optimize=True
)
print(f"Saved {out_file} successfully ({os.path.getsize(out_file) / 1024:.1f} KB)")
