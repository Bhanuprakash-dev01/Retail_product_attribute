from __future__ import annotations

from backend.app.tools.catalog_tools import get_category_rules


class TaxonomyAgent:
    def run(self, product_category: str | None) -> dict:
        category = product_category or "Headphones"
        return {
            "category": category,
            "rules": get_category_rules(category),
            "required_attributes": get_category_rules(category).get("required", []),
            "optional_attributes": get_category_rules(category).get("optional", []),
        }
