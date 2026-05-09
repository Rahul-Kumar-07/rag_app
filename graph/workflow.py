from langgraph.graph import StateGraph, END

from graph.state import GraphState
from retrieval.chain import chain

def retrieve_and_generate(state: GraphState):

    question = state["question"]

    answer = chain.invoke(question)

    return {
        "answer": answer
    }

builder = StateGraph(GraphState)

builder.add_node(
    "rag",
    retrieve_and_generate
)

builder.set_entry_point("rag")

builder.add_edge("rag", END)

graph = builder.compile()