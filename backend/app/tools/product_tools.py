from __future__ import annotations

from typing import Any

from backend.app.services.product_service import ProductService

product_service = ProductService()


def get_product(product_id: str) -> dict[str, Any]:
    product = product_service.get_product(product_id)
    if product is None:
        raise ValueError(f"Product {product_id} not found")
    return product


def get_product_attributes(product_id: str) -> dict[str, Any]:
    return product_service.get_product_attributes(product_id)


def get_product_category(product_id: str) -> str | None:
    return product_service.get_product_category(product_id)


def search_products(query: str) -> list[dict[str, Any]]:
    return product_service.search_products(query)
