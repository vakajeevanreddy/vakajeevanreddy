"""
Create animated GIF from two 3D avatar images:
  Frame 1: waving pose (aiml_avatar.jpg)     — held 3 seconds
  Frame 2: presenting pose (aiml_avatar_presenting.jpg) — held 4 seconds

Smooth cross-fade transition between them.
"""
import os, glob
from PIL import Image

os.chdir(r"C:\Users\lenovo\OneDrive\Desktop\github_profile")

# ── Find the presenting image ──────────────────────────────────────────────────
src_wave = "aiml_avatar.jpg"

# The presenting image was saved to the brain dir; copy it in if not already here
brain_dir = r"C:\Users\lenovo\.gemini\antigravity\brain\acdc7091-6569-4db3-83ec-c5e735ab7bd6"
presenting_files = glob.glob(os.path.join(brain_dir, "aiml_avatar_presenting*.jpg"))
if presenting_files:
    import shutil
    dst = "aiml_avatar_presenting.jpg"
    shutil.copy2(presenting_files[0], dst)
    print(f"Copied presenting image: {dst}")
    src_present = dst
else:
    print("ERROR: presenting image not found!")
    exit(1)

# ── Load and resize both images to same size ──────────────────────────────────
TARGET_W = 480
img_wave    = Image.open(src_wave).convert("RGBA")
img_present = Image.open(src_present).convert("RGBA")

# Both should be portrait 9:16 — resize to same height
h_wave = int(TARGET_W * img_wave.height / img_wave.width)
img_wave    = img_wave.resize((TARGET_W, h_wave), Image.LANCZOS)

h_pres = int(TARGET_W * img_present.height / img_present.width)
img_present = img_present.resize((TARGET_W, h_pres), Image.LANCZOS)

# Crop both to same height (use the shorter one)
H_FINAL = min(h_wave, h_pres)
img_wave    = img_wave.crop((0, 0, TARGET_W, H_FINAL))
img_present = img_present.crop((0, 0, TARGET_W, H_FINAL))

print(f"Frame size: {TARGET_W}x{H_FINAL}")

# ── Build frames ──────────────────────────────────────────────────────────────
HOLD_FRAMES     = 30   # frames to hold each pose (at ~100ms = 3s)
FADE_FRAMES     = 8    # transition frames

frames, durations = [], []

# Hold wave pose
for _ in range(HOLD_FRAMES):
    frames.append(img_wave.convert("RGB"))
    durations.append(100)

# Fade wave → presenting
for k in range(FADE_FRAMES):
    alpha = k / FADE_FRAMES
    blended = Image.blend(img_wave, img_present, alpha).convert("RGB")
    frames.append(blended)
    durations.append(60)

# Hold presenting pose (longer — 4 seconds)
for _ in range(40):
    frames.append(img_present.convert("RGB"))
    durations.append(100)

# Fade presenting → wave
for k in range(FADE_FRAMES):
    alpha = k / FADE_FRAMES
    blended = Image.blend(img_present, img_wave, alpha).convert("RGB")
    frames.append(blended)
    durations.append(60)

print(f"Total frames: {len(frames)}")

# ── Convert to palette mode and save GIF ─────────────────────────────────────
palette_frames = [f.convert("P", palette=Image.Palette.ADAPTIVE, colors=200) for f in frames]

palette_frames[0].save(
    "aiml_avatar_animated.gif",
    save_all=True,
    append_images=palette_frames[1:],
    loop=0,
    duration=durations,
    optimize=False,
)

size_kb = os.path.getsize("aiml_avatar_animated.gif") // 1024
print(f"Saved: aiml_avatar_animated.gif ({size_kb} KB, {len(frames)} frames)")
