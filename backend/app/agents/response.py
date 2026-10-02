from __future__ import annotations


class ResponseAgent:
    def run(self, product_id: str, findings: list[str]) -> str:
        return f"Product {product_id} analysis complete. Findings: {', '.join(findings) if findings else 'No critical issues found.'}"
