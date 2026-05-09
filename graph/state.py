# from typing_extensions import TypedDict

# class GraphState(TypedDict):
#     question: str
#     rewritten_question: str
#     answer: str

from typing import List

from typing_extensions import TypedDict

class GraphState(TypedDict):

    question: str

    # user_id: str

    rewritten_question: str

    retrieved_docs: List

    answer: str