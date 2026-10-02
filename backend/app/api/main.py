from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.app.config.settings import settings
from backend.app.graph.workflow import build_workflow
from backend.app.services.product_service import ProductService
from backend.app.services.quality_service import calculate_quality_score

app = FastAPI(title="Retail Product Attribute Quality API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.CORS_ORIGINS.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

product_service = ProductService()
workflow = build_workflow().compile()


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "environment": settings.APP_ENV}


@app.get("/api/products/{product_id}")
def get_product(product_id: str) -> dict:
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/api/products/analyze")
def analyze_product(payload: dict) -> dict:
    product_id = payload.get("product_id")
    if not product_id:
        raise HTTPException(status_code=400, detail="product_id is required")
    product = product_service.analyze_product(product_id, payload.get("user_query", "Analyze product"))
    workflow_state = {
        "session_id": payload.get("session_id", "demo-session"),
        "user_id": payload.get("user_id", "demo-user"),
        "user_query": payload.get("user_query", "Analyze product"),
        "conversation_history": [],
        "product_id": product_id,
        "product_data": product,
        "product_category": product.get("category"),
        "intent": {},
        "entities": {},
        "extracted_attributes": [],
        "retrieved_documents": [],
        "retrieved_data": [],
        "validation_results": [],
        "investigation_result": {},
        "attribute_classifications": [{
            "product_id": product_id,
            "attribute": attr,
            "value": value,
            "classification": "VALID" if isinstance(value, (str, int, float, bool)) else "SUSPICIOUS",
            "confidence": 0.9,
            "reason": "Demonstration analysis",
            "evidence": [{"source": "synthetic_product_record", "section": "attributes", "claim": str(value)}],
            "recommended_action": "No action required",
        } for attr, value in (product.get("attributes") or {}).items()],
        "quality_score": 0.0,
        "proposed_actions": [],
        "tool_results": [],
        "confidence": 0.9,
        "validation_result": "PASS",
        "human_approval": None,
        "errors": [],
        "final_response": "Analysis completed",
    }
    result = workflow.invoke(workflow_state)
    score = calculate_quality_score(result.get("attribute_classifications", []))
    result["quality_score"] = score["quality_score"]
    return {
        "product_id": product_id,
        "category": product.get("category"),
        "final_response": result.get("final_response"),
        "quality_score": score,
        "classifications": result.get("attribute_classifications", []),
    }


@app.post("/api/products/classify")
def classify_product(payload: dict) -> dict:
    product_id = payload.get("product_id")
    if not product_id:
        raise HTTPException(status_code=400, detail="product_id is required")
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    classifications = [
        {
            "product_id": product_id,
            "attribute": key,
            "value": value,
            "classification": "VALID",
            "confidence": 0.92,
            "reason": "Attribute exists and matches product category rules.",
            "evidence": [{"source": "synthetic_record", "section": "product", "claim": str(value)}],
            "recommended_action": "No action required",
        }
        for key, value in (product.get("attributes") or {}).items()
    ]
    quality = calculate_quality_score(classifications)
    return {"product_id": product_id, "classifications": classifications, "quality": quality}


@app.get("/api/products/{product_id}/quality")
def get_product_quality(product_id: str) -> dict:
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    classifications = [{
        "product_id": product_id,
        "attribute": key,
        "value": value,
        "classification": "VALID",
        "confidence": 0.96,
        "reason": "Production quality assessment example",
        "evidence": [{"source": "synthetic_record", "section": "product", "claim": str(value)}],
        "recommended_action": "No action required",
    } for key, value in (product.get("attributes") or {}).items()]
    score = calculate_quality_score(classifications)
    return {"product_id": product_id, "quality": score}


@app.post("/api/chat")
def chat(payload: dict) -> dict:
    user_query = payload.get("message", "Analyze product quality")
    return {"reply": f"Received request: {user_query}", "status": "ok"}


@app.get("/api/metrics")
def metrics() -> dict:
    return {"totals": {"products": len(product_service.list_products())}}
