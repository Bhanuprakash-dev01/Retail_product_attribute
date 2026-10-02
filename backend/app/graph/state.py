from __future__ import annotations

from typing import TypedDict


class AgentState(TypedDict):
    session_id: str
    user_id: str
    user_query: str
    conversation_history: list
    product_id: str | None
    product_data: dict
    product_category: str | None
    intent: dict
    entities: dict
    extracted_attributes: list
    retrieved_documents: list
    retrieved_data: list
    validation_results: list
    investigation_result: dict
    attribute_classifications: list
    quality_score: float | None
    proposed_actions: list
    tool_results: list
    confidence: float
    validation_result: str
    human_approval: dict | None
    errors: list
    final_response: str
