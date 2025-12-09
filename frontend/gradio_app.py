"""
Very small Gradio demo UI that talks to the backend.
Run this with: python frontend/gradio_app.py
"""

import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/analyze"  # run uvicorn backend.app:app

def analyze_endpoint(text, image, audio):
    # Prepare multipart form-data
    files = {}
    data = {"text": text or ""}

    if image:
        files["image"] = ("image.jpg", open(image, "rb"), "image/jpeg")

    if audio:
        files["audio"] = ("audio.wav", open(audio, "rb"), "audio/wav")

    r = requests.post(API_URL, data=data, files=files, timeout=20)
    return r.json()

iface = gr.Interface(
    fn=analyze_endpoint,
    inputs=[gr.Textbox(lines=3, label="Patient text (optional)"),
            gr.Image(type="filepath", label="Upload image (optional)"),
            gr.Audio(type="filepath", label="Upload audio (optional)")],
    outputs="json",
    title="Medical Agent Swarm — Demo UI"
)

if __name__ == "__main__":
    iface.launch()
