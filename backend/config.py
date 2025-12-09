"""
Central config for environment keys and flags.
Keep minimal and safe: real API keys are not required for demo mode.
"""
import os

# Demo mode: use local placeholders (True) or integrate real remote models (False)
DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() in ("1", "true", "yes")

# Example environment variables for real integration (not required for demo)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", None)
