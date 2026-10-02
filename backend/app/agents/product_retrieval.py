from __future__ import annotations

from backend.app.services.product_service import ProductService


class ProductRetrievalAgent:
    def __init__(self) -> None:
        self.service = ProductService()

    def run(self, product_id: str) -> dict:
        product = self.service.get_product(product_id)
        if product is None:
            raise ValueError(f"Product {product_id} not found")
        return product
