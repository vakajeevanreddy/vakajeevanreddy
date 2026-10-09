import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

print("Creating animated character GIF...")

# Load source image
img = Image.open("cartoon.jpg").convert("RGBA")
w, h = img.size

# Remove white background to get clean transparent character
# Sample background color (corners)
bg_color = (255, 255, 255)
datas = img.getdata()
new_data = []
for item in datas:
    # If pixel is near white (background)
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
img.putdata(new_data)
img.save("cartoon_transparent.png", "PNG")
print("Saved transparent character")
