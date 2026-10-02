from __future__ import annotations

from typing import Any


QUALITY_WEIGHTS = {
    "VALID": 100,
    "SUSPICIOUS": 70,
    "AMBIGUOUS": 60,
    "INCONSISTENT": 40,
    "INVALID": 20,
    "MISSING": 0,
    "NOT_APPLICABLE": 80,
    "NEEDS_HUMAN_REVIEW": 50,
}


def calculate_quality_score(classifications: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(classifications) or 1
    counts = {name: 0 for name in QUALITY_WEIGHTS}

    weighted_score = 0.0
    for item in classifications:
        label = str(item.get("classification", "VALID")).upper()
        counts[label] = counts.get(label, 0) + 1
        weighted_score += QUALITY_WEIGHTS.get(label, 50)

    quality_score = round((weighted_score / total), 2)
    if quality_score >= 85:
        quality_status = "EXCELLENT"
    elif quality_score >= 70:
        quality_status = "GOOD"
    elif quality_score >= 50:
        quality_status = "NEEDS_REVIEW"
    else:
        quality_status = "POOR"

    return {
        "quality_score": quality_score,
        "quality_status": quality_status,
        "total_attributes": total,
        "valid": counts.get("VALID", 0),
        "invalid": counts.get("INVALID", 0),
        "missing": counts.get("MISSING", 0),
        "inconsistent": counts.get("INCONSISTENT", 0),
        "suspicious": counts.get("SUSPICIOUS", 0),
        "ambiguous": counts.get("AMBIGUOUS", 0),
        "review_required": quality_status in {"NEEDS_REVIEW", "POOR"},
    }
