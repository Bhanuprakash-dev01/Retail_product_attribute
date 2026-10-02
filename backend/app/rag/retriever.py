from __future__ import annotations


class Retriever:
    def __init__(self, vector_store) -> None:
        self.vector_store = vector_store

    def retrieve(self, query: str, metadata_filter: dict | None = None, limit: int = 5) -> list[dict]:
        return self.vector_store.search(query=query, limit=limit, metadata_filter=metadata_filter)
