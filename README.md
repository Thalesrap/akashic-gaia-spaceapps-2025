# 🌍 Akashic Gaia
**When Earth looks at herself, humanity awakens.**  
*A project by Team System Breakdown for NASA Space Apps Challenge 2025*

---

## 🚀 Project Overview
Akashic Gaia is a poetic, scientific, and artistic experience built upon 25 years of NASA’s Terra satellite data.  
Our mission is to transform open data — vegetation, temperature, pollution, and fire activity — into a **Cartography of Collapse**: a living map of Earth’s memory.

By merging data science, artificial intelligence, and storytelling, Akashic Gaia reveals invisible planetary patterns and makes them emotionally accessible.  
It demonstrates that collaboration between humans and AIs can generate not just information, but wisdom.

---

## 🎥 Demo & Slides
- **Video Demo (30s):** https://youtu.be/fGw6XGAAS-s?si=vTFn8xurbecls-au  
- **Slides / Project Site:** https://project-akashic-gaia-nas-xzpe4lv.gamma.site/

(Click the video link above to watch the official demo.)

---

## 🔧 Tools & Data
**NASA Data (references):**
- MODIS (NDVI, Land Surface Temperature) — sample images via Worldview Snapshots.
- MOPITT (Carbon Monoxide) — pollution indicators.
- CERES (Cloud and Earth Radiation) — energy budgets.
- VIIRS (Active Fire) — hotspot detection.

**AI & Tools used:**
- Google Gemini — generated artistic overlays (images are labeled as AI-generated).  
- Nova (GPT-5) — narrative design and strategic writing.  
- Replit — runtime, script execution and temporary hosting.  
- Pillow (PIL) — image processing (used in `scripts/generate_frames.py`).  
- ElevenLabs (TTS) — narration used in the demo video.

---

## 🌌 Proof of Execution (Prova de Execução)
This project was executed successfully on **Replit** as part of the NASA Space Apps Challenge 2025.  
The automated workflow cloned this GitHub repository, installed dependencies, executed the image-generation script, and produced demonstrable outputs.

**Execution summary:**
- Repository cloned from GitHub.
- Dependencies installed (Pillow and Flask for the temporary web interface).
- Script executed: `/scripts/generate_frames.py`
- Frames generated:  
  - `/outputs/frame_001.png`  
  - `/outputs/frame_002.png`
- A small Flask app was created by Replit to preview and download the frames (optional public URL provided by Replit).

**Quick links to outputs:**
- [`/outputs/frame_001.png`](outputs/frame_001.png)  
- [`/outputs/frame_002.png`](outputs/frame_002.png)

**Replit public demo (if available):**  
Replace the placeholder below with your actual Replit URL:
https://YOUR-REPLIT-APP-URL.repl.co

---

## ▶️ How to run (local or Replit)
A minimal demonstration script is included to reproduce the visual outputs.

**Requirements:** Python 3.x, Pillow (PIL)

1. Install dependencies:
   ```bash
   pip install Pillow

2. Run the generator script:
python scripts/generate_frames.py

3. Generated outputs will be saved to:
outputs/frame_001.png
outputs/frame_002.png

🧩 Architecture & Execution Flow (summary)

High level flow:

Data & Assets — NASA open data (visual samples via Worldview snapshots) + AI overlays created with Google Gemini (files in /assets/images/).

Processing — scripts/generate_frames.py composes overlays onto a background using Pillow (this is the minimal proof-of-concept).

Outputs — resulting PNG frames placed in /outputs/.

Presentation — demo video, slides (Gamma) and optional temporary Flask app for live preview (Replit).

Why this matters:
This flow proves the pipeline from data + AI assets → automated processing → public output and allows others to reproduce the steps.

📝 AI Usage & Transparency

We document all AI usage and make the assets available in this repository:

Visual assets: overlays created with Google Gemini — files in /assets/images/ are watermarked with:
AI-generated (Google Gemini).

Prompts used: see /assets/prompts_used.txt for the exact prompts submitted to Gemini.

Narration: generated with ElevenLabs (TTS) (audio used in the video).

Narrative & orchestration: assisted by Nova (GPT-5).

See also AI_USAGE.md for more details.

👥 Team & Contact

Team System Breakdown

Thales Rodrigues Andrade Pires — Vision & Narrative
📧 thalesrap@gmail.com
