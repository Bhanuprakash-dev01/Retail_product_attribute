from __future__ import annotations

from backend.app.models.schemas import TriageResult


class TriageAgent:
    def run(self, user_query: str, product_id: str | None = None) -> TriageResult:
        category = "Headphones" if "headphone" in user_query.lower() else "General" if product_id is None else "Unknown"
        return TriageResult(
            intent="ATTRIBUTE_QUALITY_CLASSIFICATION",
            category=category,
            product_id=product_id,
            entities={},
            missing_information=[],
            confidence=0.9,
            recommended_route="FULL_ATTRIBUTE_VALIDATION",
        )
