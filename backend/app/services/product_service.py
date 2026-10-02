from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "data" / "products"


class ProductService:
    def __init__(self, products_path: str | None = None) -> None:
        self.products_path = Path(products_path) if products_path else DATA_DIR / "products.json"
        self.products = self._load_products()

    def _load_products(self) -> dict[str, dict[str, Any]]:
        if not self.products_path.exists():
            return {}
        with self.products_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        products = payload.get("products", [])
        return {product["product_id"]: product for product in products}

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self.products.get(product_id)

    def list_products(self) -> list[dict[str, Any]]:
        return list(self.products.values())

    def get_product_attributes(self, product_id: str) -> dict[str, Any]:
        product = self.get_product(product_id)
        return product.get("attributes", {}) if product else {}

    def get_product_category(self, product_id: str) -> str | None:
        product = self.get_product(product_id)
        return product.get("category") if product else None

    def analyze_product(self, product_id: str, user_query: str = "Analyze product") -> dict[str, Any]:
        product = self.get_product(product_id)
        if product is None:
            raise ValueError(f"Product {product_id} not found")

        to_return = dict(product)
        to_return["user_query"] = user_query
        return to_return

    def search_products(self, query: str) -> list[dict[str, Any]]:
        query_lower = query.lower()
        matches: list[dict[str, Any]] = []
        for product in self.products.values():
            haystack = " ".join([
                product.get("title", ""),
                product.get("brand", ""),
                product.get("category", ""),
                str(product.get("attributes", {})),
            ]).lower()
            if query_lower in haystack:
                matches.append(product)
        return matches
