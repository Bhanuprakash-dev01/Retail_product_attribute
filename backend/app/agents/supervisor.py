from __future__ import annotations

from backend.app.graph.state import AgentState


class SupervisorAgent:
    def run(self, state: AgentState) -> AgentState:
        state["intent"] = {"intent": "ATTRIBUTE_QUALITY_CLASSIFICATION", "recommended_route": "FULL_ATTRIBUTE_VALIDATION"}
        return state
