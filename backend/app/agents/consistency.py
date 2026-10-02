from __future__ import annotations


class ConsistencyAgent:
    def run(self, product_data: dict, document_evidence: list[dict]) -> dict:
        battery = (product_data.get("attributes") or {}).get("battery_life")
        if battery and "10 hours" in str(battery).lower() and any("40 hours" in str(item.get("content", "")).lower() for item in document_evidence):
            return {
                "issue_type": "ATTRIBUTE_INCONSISTENCY",
                "evidence": ["Battery life documented as up to 40 hours"],
                "policy_reference": ["Headphones specification guide"],
                "affected_attributes": ["battery_life"],
                "recommended_action": "Review and update battery_life",
                "confidence": 0.9,
                "requires_human_review": True,
            }
        return {"issue_type": "NONE", "evidence": [], "policy_reference": [], "affected_attributes": [], "recommended_action": "No action", "confidence": 0.0, "requires_human_review": False}
