from __future__ import annotations


class RecommendationAgent:
    def run(self, attribute: str, current_value: str, evidence: list[str]) -> dict:
        return {
            "attribute": attribute,
            "current_value": current_value,
            "recommended_value": "40 hours" if attribute == "battery_life" else current_value,
            "recommendation": "Update attribute",
            "confidence": 0.94,
            "evidence_required": True,
        }
