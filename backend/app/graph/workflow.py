from __future__ import annotations

from typing import Any

from langgraph.graph import END, StateGraph

from backend.app.graph.state import AgentState


def triage_agent(state: AgentState) -> AgentState:
    user_query = state["user_query"]
    product_id = None
    category = None
    if "headphones" in user_query.lower() or "product_id" in user_query.lower():
        product_id = "P1001"
        category = "Headphones"
    state["intent"] = {"intent": "ATTRIBUTE_QUALITY_CLASSIFICATION", "recommended_route": "FULL_ATTRIBUTE_VALIDATION"}
    state["product_id"] = product_id
    state["product_category"] = category
    state["confidence"] = 0.9
    state["validation_result"] = "PASS"
    return state


def product_retrieval_agent(state: AgentState) -> AgentState:
    product_id = state.get("product_id") or "P1001"
    state["product_data"] = {
        "product_id": product_id,
        "title": "Wireless Noise Cancelling Headphones",
        "brand": "SoundWave",
        "category": "Headphones",
        "attributes": {
            "color": "Black",
            "battery_life": "10 hours",
            "connectivity": "Bluetooth",
            "weight": "250g",
        },
    }
    state["retrieved_data"] = [state["product_data"]]
    return state


def attribute_extraction_agent(state: AgentState) -> AgentState:
    product = state["product_data"]
    attributes = [
        {"attribute_name": "battery_life", "value": "10 hours", "unit": "hours", "source": "product_record", "confidence": 0.96, "evidence": "battery_life in product data"},
        {"attribute_name": "connectivity", "value": "Bluetooth", "unit": None, "source": "product_record", "confidence": 0.93, "evidence": "connectivity in product data"},
        {"attribute_name": "weight", "value": "250", "unit": "g", "source": "product_record", "confidence": 0.94, "evidence": "weight in product data"},
    ]
    state["extracted_attributes"] = attributes
    return state


def taxonomy_agent(state: AgentState) -> AgentState:
    state["product_category"] = state.get("product_category") or "Headphones"
    return state


def knowledge_retrieval_agent(state: AgentState) -> AgentState:
    state["retrieved_documents"] = [
        {
            "document_id": "doc-001",
            "title": "Headphones specification guide",
            "category": "Headphones",
            "source": "manufacturer_manual",
            "content": "Battery life up to 40 hours. Weight should not exceed 350g. Wireless Bluetooth is valid connectivity.",
            "attribute": "battery_life",
            "section": "Battery",
            "confidence": 0.91,
        }
    ]
    return state


def validation_agent(state: AgentState) -> AgentState:
    state["validation_results"] = [{
        "attribute": "battery_life",
        "classification": "INCONSISTENT",
        "status": "PASS",
        "reason": "Product record says 10 hours, but documentation supports up to 40 hours.",
        "evidence": ["manufacturer_manual: Battery life up to 40 hours"],
        "confidence": 0.9,
    }]
    state["validation_result"] = "PASS"
    return state


def consistency_agent(state: AgentState) -> AgentState:
    state["investigation_result"] = {
        "issue_type": "ATTRIBUTE_INCONSISTENCY",
        "evidence": ["Battery life mismatch"],
        "policy_reference": ["product_manual"],
        "affected_attributes": ["battery_life"],
        "recommended_action": "Review and update battery_life",
        "confidence": 0.9,
        "requires_human_review": True,
    }
    return state


def classification_agent(state: AgentState) -> AgentState:
    state["attribute_classifications"] = [{
        "product_id": state.get("product_id"),
        "attribute": "battery_life",
        "value": "10 hours",
        "classification": "INCONSISTENT",
        "confidence": 0.9,
        "reason": "Structured product data conflicts with product documentation.",
        "evidence": [{"source": "manufacturer_manual", "section": "Battery", "claim": "Up to 40 hours"}],
        "recommended_action": "Review and update battery_life",
    }]
    return state


def scoring_agent(state: AgentState) -> AgentState:
    from backend.app.services.quality_service import calculate_quality_score
    score = calculate_quality_score(state["attribute_classifications"])
    state["quality_score"] = score["quality_score"]
    state["validation_result"] = "HUMAN_REVIEW" if score["review_required"] else "PASS"
    return state


def decision_agent(state: AgentState) -> AgentState:
    if state.get("validation_result") == "HUMAN_REVIEW":
        state["human_approval"] = {
            "required": True,
            "product_id": state.get("product_id"),
            "attribute": "battery_life",
            "current_value": "10 hours",
            "proposed_value": "40 hours",
        }
    else:
        state["human_approval"] = None
    return state


def response_agent(state: AgentState) -> AgentState:
    state["final_response"] = (
        "The product was analyzed. The battery_life attribute is inconsistent with the manufacturer documentation. "
        "A review is recommended before updating the catalog value."
    )
    return state


def build_workflow() -> StateGraph:
    workflow = StateGraph(AgentState)
    workflow.add_node("triage", triage_agent)
    workflow.add_node("product_retrieval", product_retrieval_agent)
    workflow.add_node("attribute_extraction", attribute_extraction_agent)
    workflow.add_node("taxonomy", taxonomy_agent)
    workflow.add_node("knowledge_retrieval", knowledge_retrieval_agent)
    workflow.add_node("validation", validation_agent)
    workflow.add_node("consistency", consistency_agent)
    workflow.add_node("classification", classification_agent)
    workflow.add_node("scoring", scoring_agent)
    workflow.add_node("decision", decision_agent)
    workflow.add_node("response", response_agent)

    workflow.set_entry_point("triage")
    workflow.add_edge("triage", "product_retrieval")
    workflow.add_edge("product_retrieval", "attribute_extraction")
    workflow.add_edge("attribute_extraction", "taxonomy")
    workflow.add_edge("taxonomy", "knowledge_retrieval")
    workflow.add_edge("knowledge_retrieval", "validation")
    workflow.add_edge("validation", "consistency")
    workflow.add_edge("consistency", "classification")
    workflow.add_edge("classification", "scoring")
    workflow.add_edge("scoring", "decision")
    workflow.add_edge("decision", "response")
    workflow.add_edge("response", END)
    return workflow
