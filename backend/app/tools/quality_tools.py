from __future__ import annotations


def create_quality_issue(product_id: str, issue_type: str, details: str) -> dict:
    return {
        "success": True,
        "issue_id": f"ISSUE-{product_id}-{issue_type}",
        "product_id": product_id,
        "issue_type": issue_type,
        "details": details,
    }


def create_review_task(product_id: str, attribute: str, reason: str) -> dict:
    return {
        "success": True,
        "task_id": f"TASK-{product_id}-{attribute}",
        "product_id": product_id,
        "attribute": attribute,
        "reason": reason,
    }


def generate_quality_report(product_id: str, summary: dict) -> dict:
    return {
        "success": True,
        "report_id": f"REPORT-{product_id}",
        "product_id": product_id,
        "summary": summary,
    }
