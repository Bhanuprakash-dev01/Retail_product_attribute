from __future__ import annotations


class EmbeddingService:
    def __init__(self, model_name: str = "text-embedding-3-small") -> None:
        self.model_name = model_name

    def create_embedding(self, text: str) -> list[float]:
        return [float((ord(ch) % 10) + 1) for ch in text[:512]]
