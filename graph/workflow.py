import streamlit as st

from langgraph.graph import StateGraph, END

from graph.state import GraphState
# from retrieval.chain import chain
from retrieval.query_transformer import query_rewriter

from retrieval.hybrid import HybridRetriever

from retrieval.reranker import rerank

from retrieval.compressor import compress_docs

from retrieval.generator import generate_answer

from core.vectorstore import vectorstore


# -----------------------------------
# Retriever
# -----------------------------------

hybrid = HybridRetriever(
    vectorstore
)

# -----------------------------------
# Query Rewrite
# -----------------------------------

def query_rewrite(state:GraphState):

    question = state["question"]

    rewritten_query = query_rewriter.invoke({
        "query": question
    })

    print("Rewritten Query:", rewritten_query)

    return {
        "rewritten_question": rewritten_query
    }

# def retrieve_and_generate(state: GraphState):

#     rewritten_question = state["rewritten_question"]

#     answer = chain.invoke(rewritten_question)

#     return {
#         "answer": answer
#     }



# -----------------------------------
# Retrieve
# -----------------------------------

def retrieve(state: GraphState):

    rewritten_question = (
        state["rewritten_question"]
    )

    docs = hybrid.retrieve(
        query=rewritten_question,
        user_id=state["user_id"]
    )

    # print("\n\nRETRIEVED DOCS:\n")

    # for doc in docs:

    #     print(doc.page_content[:500])

    #     print("\n-------------------\n")

    return {

        "retrieved_docs": docs
    }


# -----------------------------------
# Rerank
# -----------------------------------

def rerank_docs(state: GraphState):

    reranked_docs = rerank(

        state["rewritten_question"],

        state["retrieved_docs"]
    )

    return {

        "retrieved_docs": reranked_docs
    }

# -----------------------------------
# Compress
# -----------------------------------

def compress(state: GraphState):

    compressed_docs = compress_docs(

        state["rewritten_question"],

        state["retrieved_docs"]
    )

    return {

        "retrieved_docs": compressed_docs
    }

# -----------------------------------
# Generate
# -----------------------------------

def generate(state: GraphState):

    answer = generate_answer(

        state["question"],

        state["retrieved_docs"]
    )

    return {

        "answer": answer
    }

# -----------------------------------
# Build Graph
# -----------------------------------

@st.cache_resource
def build_graph():
    
    builder = StateGraph(GraphState)

    builder.add_node(
        "query_rewrite",
        query_rewrite
        )

    # builder.add_node(
    #     "rag",
    #     retrieve_and_generate
    # )

    builder.add_node(
        "retrieve",
        retrieve
    )

    builder.add_node(
        "rerank",
        rerank_docs
    )

    builder.add_node(
        "compress",
        compress
    )

    builder.add_node(
        "generate",
        generate
    )


    # -----------------------------------
    # Flow
    # -----------------------------------

    builder.set_entry_point("query_rewrite")
    # builder.add_edge("query_rewrite", "rag")

    # builder.add_edge("rag", END)

    builder.add_edge(
        "query_rewrite",
        "retrieve"
    )

    builder.add_edge(
        "retrieve",
        "rerank"
    )

    # builder.add_edge(
    #     "retrieve",
    #     "generate"
    # )

    builder.add_edge(
        "rerank",
        "compress"
    )

    builder.add_edge(
        "compress",
        "generate"
    )

    builder.add_edge(
        "generate",
        END
    )

    # -----------------------------------
    # Compile
    # -----------------------------------
    return builder.compile()

graph = build_graph()