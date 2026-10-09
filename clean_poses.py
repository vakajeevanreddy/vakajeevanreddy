import numpy as np
from PIL import Image, ImageFilter

def make_transparent(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    arr = np.array(img)
    
    # The background is light greyish/white: R,G,B are similar and > 210
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    
    # Calculate difference between channels (greyness) and lightness
    max_c = np.maximum(np.maximum(r, g), b)
    min_c = np.minimum(np.minimum(r, g), b)
    diff = max_c.astype(int) - min_c.astype(int)
    
    # Background pixels are light (avg > 215) and neutral (diff < 20)
    avg = (r.astype(int) + g.astype(int) + b.astype(int)) / 3.0
    is_bg = (avg > 215) & (diff < 20)
    
    # Smooth alpha near edges
    alpha = np.where(is_bg, 0, 255).astype(np.uint8)
    arr[:,:,3] = alpha
    
    out_img = Image.fromarray(arr, "RGBA")
    
    # Clean up isolated noise
    bbox = out_img.getbbox()
    print(f"{img_path} bbox: {bbox}")
    out_img.save(out_path, "PNG")
    return out_img

make_transparent("pose_waving.jpg", "pose_waving.png")
make_transparent("pose_presenting.jpg", "pose_presenting.png")
make_transparent("pose_standing.jpg", "pose_standing.png")
print("Backgrounds removed successfully!")
