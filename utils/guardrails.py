BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "bypass security"
]

def validate_input(query: str):

    lower_query = query.lower()

    for pattern in BLOCKED_PATTERNS:

        if pattern in lower_query:
            raise ValueError(
                "Potential prompt injection detected."
            )

    return query