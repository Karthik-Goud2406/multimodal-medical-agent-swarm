"""
LLM client stub.
- Demo: returns a simple structured medical report.
- Production: call Llama-3/GPT via SDK and use function-calling or JSON schema enforcement.
"""

from config import DEMO_MODE, OPENAI_API_KEY
import json

def generate_report(symptoms_text: str, transcription: str, image_findings: dict, context: dict) -> dict:
    """
    Return a structured report dict (summary, possible_diagnosis, recommended_tests, advices).
    In production, this logic lives in the LLM prompt and post-processing.
    """
    # Compose a short combined narrative (demo)
    narrative = " ; ".join(filter(None, [symptoms_text, transcription]))
    if not narrative:
        narrative = "No symptoms text provided."

    # Demo deterministic report
    report = {
        "summary": narrative[:600],
        "image_summary": image_findings,
        "possible_diagnosis": "Viral upper respiratory infection (demo)",
        "recommended_tests": ["CBC", "Chest X-ray if symptoms worsen"],
        "advice": ["Rest", "Hydration", "Paracetamol for fever"],
        "context_used": context
    }

    # Production hint: When integrating LLM, parse JSON output into the same schema.
    return report
