# Akashic Gaia - System Architecture

## 🧩 Overview
**Akashic Gaia** is a hybrid system that merges **NASA Earth observation data**, **AI-generated visual layers**, and **philosophical narrative design** to reimagine how humanity perceives Earth's self-awareness.

The architecture was tested and validated via **Replit Automation**, confirming the workflow and generation of visual outputs.

---

## 🔧 Components

### 1. Data Sources
- **NASA Open Data** (MODIS/Terra Satellite imagery via Worldview Snapshots)
- **AI-generated Overlays** (Google Gemini images labeled as “AI-generated”)

### 2. Processing Layer
- **Python + Pillow** for image composition
- **Flask (auto-installed by Replit)** for web visualization
- **GitHub Actions** (manual) for repository management

### 3. Scripts
- `/scripts/generate_frames.py` — creates base frames combining AI overlays with dark cosmic backgrounds and textual layers.

### 4. Outputs
- `/outputs/frame_001.png` and `/outputs/frame_002.png` — visual proof of concept combining NASA-like imagery and artificial intelligence synthesis.

---

## 🚀 Execution Flow

1. Repository cloned from GitHub → `akashic-gaia-spaceapps-2025`
2. Dependencies installed (`pip install Pillow`)
3. Script executed via `python scripts/generate_frames.py`
4. Outputs generated in `/outputs`
5. Flask web app hosted automatically by Replit
6. User downloads frames or views them live through the app

---

## 🧠 Philosophical Layer
The project symbolizes the moment when **Earth looks at herself through the eyes of data** — a poetic act of self-recognition.  
It bridges science, art, and consciousness through open NASA datasets and generative AI, echoing the tagline:  
> *“When Earth looks at herself, humanity awakens.”*
