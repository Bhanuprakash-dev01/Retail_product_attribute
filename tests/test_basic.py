from __future__ import annotations

from backend.app.services.product_service import ProductService
from backend.app.services.quality_service import calculate_quality_score


def test_product_service_loads_samples() -> None:
    service = ProductService()
    products = service.list_products()
    assert len(products) >= 1
    assert "P1001" in {product["product_id"] for product in products}


def test_quality_score_returns_expected_shape() -> None:
    result = calculate_quality_score([
        {"classification": "VALID"},
        {"classification": "INVALID"},
        {"classification": "MISSING"},
    ])
    assert result["total_attributes"] == 3
    assert result["quality_score"] >= 0
    assert "quality_status" in result
