# Enterprise RAG Backend Service

A production-oriented backend service that integrates Retrieval-Augmented Generation (RAG) into an enterprise-style API to answer domain-specific queries reliably while minimizing hallucinations.

This project focuses on **backend design, retrieval reliability, and safe LLM integration**, not demos.

---

## Problem Statement

Large Language Models do not have access to private or domain-specific documents and can hallucinate when asked factual questions.

This service solves that by:
- Externalizing knowledge into a vector database
- Retrieving only relevant context at query time
- Forcing the LLM to answer strictly from retrieved evidence

---

## High-Level Architecture

1. **Offline Ingestion**
   - Parse and clean documents (PDFs)
   - Semantically chunk content
   - Generate embeddings
   - Store vectors with metadata (source, section, version)

2. **Online Query Flow**
   - User query → embedding
   - Top-K similarity retrieval
   - Context-aware prompt construction
   - Structured LLM response

---

## Key Design Decisions

- **RAG instead of fine-tuning**  
  Allows faster updates, lower cost, and explicit control over knowledge sources.

- **Semantic chunking with metadata**  
  Improves retrieval precision while preserving context.

- **Relevance thresholds & refusal logic**  
  Prevents the model from guessing when confidence is low.

- **Stateless API design**  
  Enables horizontal scaling and easier deployment.

---

## Tech Stack

- **Backend:** Python, FastAPI  
- **LLM:** GPT-4 / Llama (pluggable)  
- **Vector DB:** Pinecone / ChromaDB  
- **Data:** PostgreSQL (metadata), Redis (caching)  
- **Infra:** Docker, GitHub Actions

---

## API Overview

### POST `/query`

**Request**
```json
{
  "question": "What are the clinical guidelines for X?"
}
```


Response
{
  "answer": "...",
  "sources": ["doc_123", "doc_456"],
  "confidence": "high"
}


Failure Handling & Safety :

Returns “insufficient data” if retrieval confidence is low
Filters outdated documents using metadata
Structured outputs to avoid downstream parsing errors
Logs retrieval scores for observability



Limitations & Future Improvements :

No cross-encoder re-ranking (planned)
Evaluation currently manual
Auth & rate-limiting can be extended


How to Run Locally

cp .env.example .env
docker compose up
