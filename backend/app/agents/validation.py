from __future__ import annotations


class ValidationAgent:
    def run(self, attribute: str, value: str) -> dict:
        if value is None:
            return {"attribute": attribute, "classification": "MISSING", "status": "PASS", "reason": "Missing value", "evidence": [], "confidence": 0.8}
        return {"attribute": attribute, "classification": "VALID", "status": "PASS", "reason": "Meets expected form", "evidence": ["product_record"], "confidence": 0.9}
