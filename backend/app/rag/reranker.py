from __future__ import annotations


class Reranker:
    def rerank(self, documents: list[dict]) -> list[dict]:
        return sorted(documents, key=lambda x: x.get("confidence", 0.0), reverse=True)
