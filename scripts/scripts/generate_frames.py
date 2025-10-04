# scripts/generate_frames.py
"""
Akashic Gaia - simple demo generator
Generates sample frames combining a dark background and AI overlays.
Requires: Pillow (PIL)
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Paths (relative to repo root)
ASSETS_IMG = "assets/images"
OUTPUTS = "outputs"
OVERLAY1 = os.path.join(ASSETS_IMG, "overlay_01_watermarked.png")
OVERLAY2 = os.path.join(ASSETS_IMG, "overlay_02_watermarked.png")

os.makedirs(OUTPUTS, exist_ok=True)

def add_caption(img, text):
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except:
        font = ImageFont.load_default()
    w, h = img.size
    margin = 12
    text_pos = (margin, h - 36)
    draw.rectangle([text_pos, (w - margin, h - margin)], fill=(0,0,0,150))
    draw.text((text_pos[0]+6, text_pos[1]+4), text, font=font, fill=(255,255,255))
    return img

def make_frame(overlay_path, idx):
    base = Image.new("RGB", (1280, 720), (8, 12, 30))  # dark cosmic background
    if os.path.exists(overlay_path):
        overlay = Image.open(overlay_path).convert("RGBA")
        overlay = overlay.resize((int(1280*0.8), int(720*0.6)))
        # paste centered
        x = (1280 - overlay.width) // 2
        y = (720 - overlay.height) // 2
        base.paste(overlay, (x, y), overlay)
    caption = f"Akashic Gaia — frame {idx:03d}"
    base = add_caption(base, caption)
    out_path = os.path.join(OUTPUTS, f"frame_{idx:03d}.png")
    base.save(out_path, quality=90)
    print("Saved:", out_path)

def main():
    # create frames using overlays (if available)
    overlays = [OVERLAY1, OVERLAY2]
    for i, ov in enumerate(overlays, start=1):
        make_frame(ov, i)

if __name__ == "__main__":
    main()
