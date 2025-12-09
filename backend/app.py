"""
FastAPI entrypoint. Single /analyze endpoint accepts text, audio, and image.
All files processed in-memory (await file.read()).
"""

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from services.pipeline import medical_pipeline
from config import DEMO_MODE

app = FastAPI(title="Medical Agent Swarm (Demo-ready)")

@app.post("/analyze")
async def analyze(
    text: str = Form(""),
    audio: UploadFile | None = File(None),
    image: UploadFile | None = File(None)
):
    """
    Accepts text, optional audio and optional image.
    Returns a structured JSON report dictionary.
    """
    # Require at least one input
    if not (text.strip() or audio or image):
        raise HTTPException(status_code=422, detail="Provide text OR audio OR image")

    # Pipeline may raise; let FastAPI return 500 with stacktrace in dev
    report = await medical_pipeline(text=text, audio=audio, image=image)
    return {"report": report}
