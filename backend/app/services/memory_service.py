from __future__ import annotations

from typing import Any


class MemoryService:
    def __init__(self) -> None:
        self.short_term_memory: dict[str, Any] = {}
        self.workflow_state: dict[str, Any] = {}

    def remember(self, key: str, value: Any) -> None:
        self.short_term_memory[key] = value

    def get(self, key: str) -> Any:
        return self.short_term_memory.get(key)

    def set_workflow(self, workflow_id: str, state: dict[str, Any]) -> None:
        self.workflow_state[workflow_id] = state

    def get_workflow(self, workflow_id: str) -> dict[str, Any]:
        return self.workflow_state.get(workflow_id, {})
