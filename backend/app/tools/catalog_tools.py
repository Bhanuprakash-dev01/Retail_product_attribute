from __future__ import annotations


CATEGORY_RULES = {
    "Headphones": {
        "required": ["brand", "connectivity", "battery_life", "weight"],
        "optional": ["color", "warranty"],
    },
    "Laptops": {
        "required": ["brand", "processor", "ram", "storage", "screen_size"],
        "optional": ["keyboard_type", "weight"],
    },
}


def get_category_rules(category: str) -> dict:
    return CATEGORY_RULES.get(category, {"required": [], "optional": []})


def validate_category(category: str) -> bool:
    return category in CATEGORY_RULES
