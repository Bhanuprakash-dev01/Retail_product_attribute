ROLE = "Quality Scoring Agent"
GOAL = "Compute deterministic product quality score from attribute classifications."
CONSTRAINTS = ["Use configurable status weights.", "Separate attribute-level from product-level scores."]
OUTPUT_SCHEMA = "QualityScore"
FAILURE_BEHAVIOR = "Return a conservative score and review flag when classification data is incomplete."
GROUNDING = "Use only the final attribute classifications."
NO_HALLUCINATION = "Never invent counts or statuses."
