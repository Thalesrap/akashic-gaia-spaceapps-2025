scripts/generate_frames.py

import os
from PIL import Image, ImageDraw, ImageFont

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# List of AI images used as overlays
ai_images = ["assets/images/overlay_01_watermarked.png",
             "assets/images/overlay_02_watermarked.png"]

# Generate sample frames
for idx, ai_img_path in enumerate(ai_images, start=1):
    try:
        base = Image.new("RGB", (800, 600), (10, 10, 30))  # dark cosmic background
        overlay = Image.open(ai_img_path).resize((400, 300))
        base.paste(overlay, (200, 150))
        
        # Add poetic label
        draw = ImageDraw.Draw(base)
        draw.text((10, 10), f"Frame {idx}: Akashic Gaia Vision", fill=(200, 200, 255))
        
        # Save output frame
        output_path = f"outputs/frame_{idx:03d}.png"
        base.save(output_path)
        print(f"Generated: {output_path}")
    except Exception as e:
        print(f"Error processing {ai_img_path}: {e}")
