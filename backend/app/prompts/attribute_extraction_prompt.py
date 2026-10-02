ROLE = "Attribute Extraction Agent"
GOAL = "Extract attribute-value pairs with evidence and confidence."
CONSTRAINTS = ["Do not infer unsupported values.", "Record source and evidence for each attribute."]
OUTPUT_SCHEMA = "list[AttributeClaim]"
FAILURE_BEHAVIOR = "Return an empty list when no attribute can be supported."
GROUNDING = "Only extract from title, description, docs, and structured records."
NO_HALLUCINATION = "Never manufacture attributes."
