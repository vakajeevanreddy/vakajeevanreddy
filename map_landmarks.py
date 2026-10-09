from PIL import Image, ImageDraw

img = Image.open("scene_presenting.jpg").convert("RGB")
draw = ImageDraw.Draw(img)

landmarks = {
    "Head": (512, 175),
    "Left_Eye": (485, 175),
    "Right_Eye": (540, 175),
    "Mouth": (512, 220),
    "Neck": (512, 265),
    "Torso": (512, 400),
    "L_Shoulder": (410, 310),
    "L_Elbow": (375, 410),
    "L_Hand": (420, 480),
    "R_Shoulder": (610, 310),
    "R_Elbow": (665, 400),
    "R_Hand": (710, 380),
    "Hips": (512, 550),
    "L_Knee": (450, 720),
    "L_Foot": (430, 940),
    "R_Knee": (570, 720),
    "R_Foot": (585, 940),
}

for name, (x, y) in landmarks.items():
    draw.circle((x, y), 8, fill="red", outline="white")

img.save("landmarks_test.jpg")
print("Landmarks mapped and saved to landmarks_test.jpg")
