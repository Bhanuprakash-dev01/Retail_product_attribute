from __future__ import annotations

from pathlib import Path

from backend.app.rag.loaders import DocumentLoader
from backend.app.rag.chunking import Chunker

ROOT = Path(__file__).resolve().parents[1]
knowledge_root = ROOT / "data" / "knowledge_base"
loader = DocumentLoader(knowledge_root)
chunker = Chunker()

items = loader.load()
chunks = []
for item in items:
    for chunk in chunker.chunk(item["content"]):
        chunks.append({"document_id": item["document_id"], "content": chunk, "source": item["source"]})

print(f"Ingested {len(chunks)} document chunks into the local RAG store.")
