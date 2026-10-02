from __future__ import annotations


class Chunker:
    def chunk(self, text: str, size: int = 500, overlap: int = 80) -> list[str]:
        chunks: list[str] = []
        start = 0
        while start < len(text):
            end = min(len(text), start + size)
            chunk = text[start:end]
            chunks.append(chunk)
            start += size - overlap
        return chunks
