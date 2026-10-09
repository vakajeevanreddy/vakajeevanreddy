import numpy as np
from PIL import Image
from scipy.ndimage import binary_fill_holes
from collections import deque

def extract_subject_flood(img_path, out_path):
    img = Image.open(img_path).convert("RGB")
    arr = np.array(img, dtype=float)
    h, w, _ = arr.shape
    
    # Sample background color from corners
    corners = np.array([arr[0,0], arr[0, w-1], arr[0, w//2], arr[h-1, 0], arr[h-1, w-1]])
    bg_color = np.median(corners, axis=0)
    
    # Distance from background color
    dist = np.linalg.norm(arr - bg_color, axis=2)
    
    # Threshold for background
    is_bg = dist < 32
    
    # Flood fill from border
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()
    
    # Add border pixels that match background
    for y in range(h):
        for x in [0, w-1]:
            if is_bg[y, x] and not visited[y, x]:
                visited[y, x] = True
                queue.append((y, x))
    for x in range(w):
        for y in [0, h-1]:
            if is_bg[y, x] and not visited[y, x]:
                visited[y, x] = True
                queue.append((y, x))
                
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny, nx] and dist[ny, nx] < 40:
                    visited[ny, nx] = True
                    queue.append((ny, nx))
                    
    alpha = np.where(visited, 0, 255).astype(np.uint8)
    
    rgba = np.dstack((np.array(img), alpha))
    out_img = Image.fromarray(rgba, "RGBA")
    bbox = out_img.getbbox()
    print(f"{img_path} extracted bbox: {bbox}")
    out_img.save(out_path, "PNG")

extract_subject_flood("pose_waving.jpg", "pose_waving.png")
extract_subject_flood("pose_presenting.jpg", "pose_presenting.png")
extract_subject_flood("pose_standing.jpg", "pose_standing.png")
print("High-quality flood cutout complete!")
