# Medical Agent Swarm 

**One-liner:** Modular multimodal medical agent pipeline (text, audio, image) designed to be production-ready and easily integrated with Whisper, Florence-2, Llama-3 and RAG.

**Overview:**  
This repo contains a compact, readable, and deterministic demo of a multimodal medical pipeline. The code is intentionally lightweight and safe for interviews (no API keys required). Each model client is implemented as a small module and can be replaced with real model API calls with minimal changes.

## Features

- Single `/analyze` endpoint (FastAPI) that accepts text, audio, and image (multipart).
- All files processed in-memory (`await file.read()`), no disk writes.
- Modular clients: audio, vision, RAG, LLM — each easily replaceable.
- Demo mode: deterministic placeholders for robustness during interview demos.
- Optional Gradio UI for quick demo.

## Quick start (Windows PowerShell)

```powershell
# create venv
python -m venv .venv
.\.venv\Scripts\activate

# install
pip install -r backend/requirements.txt

# run backend
cd backend
uvicorn app:app --reload --port 8000
```
