from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class TriageResult(BaseModel):
    intent: str = "ATTRIBUTE_QUALITY_CLASSIFICATION"
    category: str | None = None
    product_id: str | None = None
    entities: dict[str, Any] = Field(default_factory=dict)
    missing_information: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    recommended_route: str = "FULL_ATTRIBUTE_VALIDATION"


class AttributeClaim(BaseModel):
    attribute_name: str
    value: str | float | int | bool | None = None
    unit: str | None = None
    source: str
    confidence: float = 0.0
    evidence: str


class ValidationFinding(BaseModel):
    attribute: str
    classification: str
    status: Literal["PASS", "RETRY", "HUMAN_REVIEW", "BLOCK"] = "PASS"
    reason: str
    evidence: list[str] = Field(default_factory=list)
    confidence: float = 0.0


class ClassificationResult(BaseModel):
    product_id: str
    attribute: str
    value: str | None = None
    classification: str
    confidence: float = 0.0
    reason: str
    evidence: list[dict[str, str]] = Field(default_factory=list)
    recommended_action: str


class QualityScore(BaseModel):
    product_id: str
    quality_score: float
    quality_status: str
    total_attributes: int
    valid: int = 0
    invalid: int = 0
    missing: int = 0
    inconsistent: int = 0
    suspicious: int = 0
    ambiguous: int = 0
    review_required: bool = False


class Recommendation(BaseModel):
    attribute: str
    current_value: str | None = None
    recommended_value: str | None = None
    recommendation: str
    confidence: float = 0.0
    evidence_required: bool = False


class ApprovalRequest(BaseModel):
    workflow_id: str
    product_id: str
    attribute: str
    current_value: str | None = None
    proposed_value: str | None = None
    reason: str
    evidence: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    policy: str = "catalog_change_review"


class AnalysisRequest(BaseModel):
    product_id: str
    user_query: str = "Analyze product attributes"
    session_id: str | None = None


class ProductAnalysisResponse(BaseModel):
    product_id: str
    category: str | None = None
    quality_score: float | None = None
    quality_status: str | None = None
    classifications: list[ClassificationResult] = Field(default_factory=list)
    recommendations: list[Recommendation] = Field(default_factory=list)
    validation_result: str = "PASS"
    final_response: str = ""
