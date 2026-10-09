import numpy as np
from PIL import Image

img = Image.open("cartoon_transparent.png")
w, h = img.size
print(f"Size: {w}x{h}")

# Find bounding box of non-transparent pixels
bbox = img.getbbox()
print(f"Bounding box: {bbox}")
