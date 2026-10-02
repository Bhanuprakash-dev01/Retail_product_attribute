from __future__ import annotations


class VectorStore:
    def __init__(self) -> None:
        self.documents: list[dict] = []

    def add_documents(self, docs: list[dict]) -> None:
        self.documents.extend(docs)

    def search(self, query: str, limit: int = 5, metadata_filter: dict | None = None) -> list[dict]:
        filtered = self.documents
        if metadata_filter:
            filtered = [doc for doc in filtered if all(doc.get(k) == v for k, v in metadata_filter.items())]
        return filtered[:limit]

    def delete_document(self, document_id: str) -> None:
        self.documents = [doc for doc in self.documents if doc.get("document_id") != document_id]

    def update_document(self, document_id: str, new_data: dict) -> None:
        for doc in self.documents:
            if doc.get("document_id") == document_id:
                doc.update(new_data)
                return
