"""
Vision client (Pillow-based demo).
- Returns simple metadata and a basic heuristic observation.
- Replace with Florence-2 / vision-LLaMA calls for production.
"""

from io import BytesIO
from PIL import Image, ImageStat

def analyze_image(image_bytes: bytes) -> dict:
    try:
        img = Image.open(BytesIO(image_bytes))
    except Exception as exc:
        return {"error": f"Invalid image: {exc}"}

    # Basic metadata
    fmt = img.format or "UNKNOWN"
    w, h = img.size
    mode = img.mode

    # Simple brightness heuristic (for demo)
    gray = img.convert("L")
    stat = ImageStat.Stat(gray)
    avg_brightness = stat.mean[0] if stat.mean else 0.0

    observation = "brightness normal"
    if avg_brightness < 60:
        observation = "image appears dark"
    elif avg_brightness > 200:
        observation = "image appears bright"

    return {
        "format": fmt,
        "size": {"width": w, "height": h},
        "mode": mode,
        "avg_brightness": round(avg_brightness, 1),
        "observation": observation,
        # leave space for more fields from production vision model:
        # e.g. "detected_findings": [...]
    }
