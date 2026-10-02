from __future__ import annotations

from pathlib import Path


class DocumentLoader:
    def __init__(self, root: str | Path | None = None) -> None:
        self.root = Path(root) if root else Path(__file__).resolve().parents[3] / "data" / "knowledge_base"

    def load(self) -> list[dict]:
        if not self.root.exists():
            return []
        docs: list[dict] = []
        for file in sorted(self.root.glob("**/*.*")):
            docs.append({
                "document_id": file.stem,
                "title": file.name,
                "source": str(file.relative_to(self.root.parent)),
                "content": file.read_text(encoding="utf-8", errors="ignore")[:3000],
                "category": "Headphones",
            })
        return docs
