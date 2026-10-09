import numpy as np
from PIL import Image, ImageFilter

def isolate_clean_subject(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    arr = np.array(img)
    
    # Background in scene_waving is dark (R < 35, G < 40, B < 45)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    
    # Distance from dark background #0d1117 (13, 17, 23)
    bg_ref = np.array([13, 17, 23])
    dist = np.sqrt((r.astype(float) - 13)**2 + (g.astype(float) - 17)**2 + (b.astype(float) - 23)**2)
    
    # Floor reflections or floor plane in scene_waving might have some grey/white speckles below y=950
    # Let's clean anything outside the character's body
    # Character body is in x: [320, 750], y: [60, 980]
    is_subject = np.zeros((arr.shape[0], arr.shape[1]), dtype=bool)
    
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            # If distance from dark background is significant
            if dist[y, x] > 28:
                # Check if it's within character bounding area
                if 280 <= x <= 780 and 50 <= y <= 980:
                    is_subject[y, x] = True
                    
    # Fill small holes inside the subject
    from scipy.ndimage import binary_fill_holes, binary_dilation
    is_subject = binary_fill_holes(is_subject)
    
    # Feather edges for perfectly smooth anti-aliasing
    mask = Image.fromarray((is_subject * 255).astype(np.uint8), mode='L')
    mask = mask.filter(ImageFilter.GaussianBlur(1.0))
    
    out_img = img.copy()
    out_img.putalpha(mask)
    out_img.save(out_path, "PNG")
    print(f"Saved clean transparent subject to {out_path}")

isolate_clean_subject("scene_waving.jpg", "clean_3d_char.png")
isolate_clean_subject("scene_presenting.jpg", "clean_3d_presenting.png")
