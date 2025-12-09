"""
RAG client stub.
- Demo: returns short synthetic context.
- Production: embed retrieval via Pinecone/FAISS and return top docs / snippets.
"""

from config import DEMO_MODE, PINECONE_API_KEY

def retrieve_context(query: str, image_findings: dict | None = None) -> dict:
    """
    For demo purposes we return a small context object which shows where
    RAG output would appear. Replace with real vector DB retrieval later.
    """
    if not query.strip() and not image_findings:
        return {"note": "no context available"}

    if not DEMO_MODE and PINECONE_API_KEY:
        # Pseudocode: run embedding, query vector DB, return top-k snippets
        return {"top_docs": ["Real doc snippet A", "Real doc snippet B"]}

    # Demo placeholder
    sample = (
        "Relevant clinical guideline: for acute fever + cough, check vitals, "
        "consider CBC and chest X-ray if respiratory distress is present. (demo context)"
    )
    return {"snippet": sample}
