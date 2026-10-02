from __future__ import annotations


class ActionAgent:
    def run(self, product_id: str, attribute: str, new_value: str) -> dict:
        return {
            "success": True,
            "action_id": f"ACT-{product_id}-{attribute}",
            "product_id": product_id,
            "updated_attribute": attribute,
            "new_value": new_value,
        }
