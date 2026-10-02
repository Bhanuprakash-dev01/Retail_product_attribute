from __future__ import annotations


class ClassificationAgent:
    def run(self, product_id: str, attribute: str, value: str, reason: str) -> dict:
        return {
            "product_id": product_id,
            "attribute": attribute,
            "value": value,
            "classification": "INCONSISTENT" if "conflicts" in reason.lower() else "VALID",
            "confidence": 0.9,
            "reason": reason,
            "evidence": [{"source": "manufacturer_manual", "section": "Battery", "claim": "Up to 40 hours"}],
            "recommended_action": "Review and update",
        }
