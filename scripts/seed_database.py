from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
products_path = ROOT / "data" / "products" / "products.json"

with products_path.open("r", encoding="utf-8") as handle:
    payload = json.load(handle)

print(f"Seeded {len(payload.get('products', []))} products into the local data store.")
print("This demo project uses a JSON-backed product store for local execution.")
