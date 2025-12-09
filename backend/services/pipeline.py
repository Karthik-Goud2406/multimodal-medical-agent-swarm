"""
Pipeline orchestrator:
- collects inputs (text, audio, image)
- calls modular clients (audio, vision, rag, llm)
- returns structured JSON-like dict
Design: each client is minimal and swap-able.
"""

from typing import Optional, Any, Dict
from models.audio_client import transcribe_audio
from models.vision_client import analyze_image
from models.rag_client import retrieve_context
from models.llm_client import generate_report

async def medical_pipeline(text: str, audio, image) -> Dict[str, Any]:
    """
    Orchestrate all steps; run minimal local processing in demo mode.
    In production you would call remote models inside client modules.
    """
    # Collect inputs
    collected = {"text_input": text.strip() if text else ""}

    # Audio (bytes read in-memory)
    if audio:
        audio_bytes = await audio.read()
        collected["transcription"] = await transcribe_audio(audio_bytes)
    else:
        collected["transcription"] = ""

    # Image (bytes read in-memory)
    if image:
        img_bytes = await image.read()
        collected["image_findings"] = analyze_image(img_bytes)
    else:
        collected["image_findings"] = {}

    # Build context for retrieval (simple concatenation)
    retrieval_query = " ".join([collected.get("text_input", ""), collected.get("transcription", "")])
    # RAG module returns a short context snippet; demo returns placeholder
    retrieved_context = retrieve_context(retrieval_query, image_findings=collected["image_findings"])
    collected["retrieved_context"] = retrieved_context

    # Final LLM stage: generate structured JSON-like report
    final_report = generate_report(
        symptoms_text=collected["text_input"],
        transcription=collected["transcription"],
        image_findings=collected["image_findings"],
        context=retrieved_context
    )

    # Pack everything clearly for easy debugging / interview demo
    return {
        "inputs": collected,
        "final_report": final_report
    }
