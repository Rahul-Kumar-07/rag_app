from langgraph.graph import StateGraph, END

from graph.state import GraphState
from retrieval.chain import chain
from retrieval.query_transformer import query_rewriter


def query_rewrite(state:GraphState):

    question = state["question"]

    rewritten_query = query_rewriter.invoke({
        "query": question
    })

    print("Rewritten Query:", rewritten_query)

    return {
        "rewritten_question": rewritten_query
    }

def retrieve_and_generate(state: GraphState):

    rewritten_question = state["rewritten_question"]

    answer = chain.invoke(rewritten_question)

    return {
        "answer": answer
    }

builder = StateGraph(GraphState)

builder.add_node(
    "query_rewrite",
    query_rewrite
    )

builder.add_node(
    "rag",
    retrieve_and_generate
)

builder.set_entry_point("query_rewrite")
builder.add_edge("query_rewrite", "rag")

builder.add_edge("rag", END)

graph = builder.compile()