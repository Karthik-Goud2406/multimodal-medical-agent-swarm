"""
Small input validators (optional).
Keep this file minimal for interview clarity.
"""

def is_text_empty(s: str) -> bool:
    return not (s and s.strip())
