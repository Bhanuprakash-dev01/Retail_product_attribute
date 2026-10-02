from __future__ import annotations

from backend.app.rag.loaders import DocumentLoader
from backend.app.rag.retriever import Retriever
from backend.app.rag.vector_store import VectorStore


class RetrievalAgent:
    def __init__(self) -> None:
        self.vector_store = VectorStore()
        docs = DocumentLoader().load()
        self.vector_store.add_documents(docs)
        self.retriever = Retriever(self.vector_store)

    def run(self, query: str) -> list[dict]:
        return self.retriever.retrieve(query=query, limit=3)
