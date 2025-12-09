"""
Audio client.
- Demo: returns deterministic placeholder transcription.
- To integrate Whisper (OpenAI) or other ASR, replace implementation below.
"""

import asyncio
from config import DEMO_MODE, OPENAI_API_KEY

async def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Demo transcription: returns a short deterministic message.
    Replace this function with real ASR calls if OPENAI_API_KEY is provided.
    """
    if not audio_bytes:
        return ""

    # If you decide to integrate real ASR: add SDK calls here (guarded by OPENAI_API_KEY)
    if not DEMO_MODE and OPENAI_API_KEY:
        # Example: call OpenAI Whisper here (pseudocode)
        # return call_whisper_api(audio_bytes)
        await asyncio.sleep(0.01)  # keep async-compatible placeholder
        return "Live ASR response (placeholder for production)."

    # Demo behavior (safe, deterministic)
    return "Patient reports fever and sore throat for 3 days. (demo transcription)"
