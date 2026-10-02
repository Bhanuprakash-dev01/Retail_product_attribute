from __future__ import annotations


class AttributeExtractionAgent:
    def run(self, product_data: dict) -> list[dict]:
        extracted = []
        for attribute_name, value in (product_data.get("attributes") or {}).items():
            extracted.append({
                "attribute_name": attribute_name,
                "value": value,
                "unit": None,
                "source": "product_record",
                "confidence": 0.93,
                "evidence": f"{attribute_name} recorded in product data",
            })
        return extracted
