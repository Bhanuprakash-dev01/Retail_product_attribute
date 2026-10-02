from __future__ import annotations

from backend.app.services.quality_service import calculate_quality_score


class ScoringAgent:
    def run(self, classifications: list[dict]) -> dict:
        return calculate_quality_score(classifications)
