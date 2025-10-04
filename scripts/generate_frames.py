# scripts/generate_frames.py

"""
Akashic Gaia - simple demo generator
Generates sample frames combining NASA data images and AI overlays.
Requires: Pillow (PIL)
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Paths (relative to repo root)
ASSETS_IMG = "assets/images"
OUTPUTS = "outputs"

# Nomes dos arquivos de overlay AI (gerados com Gemini)
OVERLAY1 = os.path.join(ASSETS_IMG, "overlay_01_watermarked.png")
OVERLAY2 = os.path.join(ASSETS_IMG, "overlay_02_watermarked.png")

# Nomes dos arquivos base com dados da NASA (baixados do Worldview)
NASA_BASE1 = os.path.join(ASSETS_IMG, "nasa_data_base_01.png") # Ex: NDVI
NASA_BASE2 = os.path.join(ASSETS_IMG, "nasa_data_base_02.png") # Ex: Land Surface Temp

os.makedirs(OUTPUTS, exist_ok=True)

def add_caption(img, text):
    draw = ImageDraw.Draw(img)
    try:
        # Tenta usar uma fonte padrão, se não, usa a default
        font = ImageFont.truetype("DejaVuSans.ttf", 20) 
    except IOError: # Captura o erro específico se a fonte não for encontrada
        font = ImageFont.load_default()
    w, h = img.size
    margin = 12
    # Define a posição do texto na parte inferior da imagem
    text_pos = (margin, h - 36)
    # Desenha um retângulo escuro para o fundo da legenda
    draw.rectangle([text_pos, (w - margin, h - margin)], fill=(0,0,0,150))
    # Desenha o texto da legenda
    draw.text((text_pos[0]+6, text_pos[1]+4), text, font=font, fill=(255,255,255))
    return img

def make_frame(overlay_path, nasa_base_path, idx):
    # Carrega a imagem base da NASA ou cria um fundo escuro se não encontrar
    if os.path.exists(nasa_base_path):
        base = Image.open(nasa_base_path).convert("RGB").resize((1280, 720))
    else:
        base = Image.new("RGB", (1280, 720), (8, 12, 30)) # Fundo escuro fallback
        print(f"Warning: NASA base image not found at {nasa_base_path}, using dark background.")

    # Cola o overlay AI sobre a imagem base (da NASA ou fundo escuro)
    if os.path.exists(overlay_path):
        overlay = Image.open(overlay_path).convert("RGBA")
        overlay = overlay.resize((int(1280*0.8), int(720*0.6)))
        x = (1280 - overlay.width) // 2
        y = (720 - overlay.height) // 2
        base.paste(overlay, (x, y), overlay)
    
    # Adiciona a legenda ao frame, mencionando o uso de dados da NASA
    caption = f"Akashic Gaia — frame {idx:03d} (NASA Data + AI Vision)"
    base = add_caption(base, caption)
    
    out_path = os.path.join(OUTPUTS, f"frame_{idx:03d}.png")
    base.save(out_path, quality=90)
    print("Saved:", out_path)

def main():
    # Define a configuração para cada frame: (overlay AI, imagem base NASA)
    frame_configs = [
        (OVERLAY1, NASA_BASE1),
        (OVERLAY2, NASA_BASE2)
    ]
    
    for i, (ov, nb) in enumerate(frame_configs, start=1):
        make_frame(ov, nb, i)

if __name__ == "__main__":
    main()
