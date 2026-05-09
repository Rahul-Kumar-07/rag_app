from typing_extensions import TypedDict

class GraphState(TypedDict):
    question: str
    rewritten_question: str
    answer: str