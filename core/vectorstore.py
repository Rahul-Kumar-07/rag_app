from pinecone import Pinecone
from pinecone import ServerlessSpec

from langchain_community.vectorstores import Pinecone as PineconeVectorStore

from core.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME
)

from core.embeddings import embeddings

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

existing_indexes = [
    index["name"]
    for index in pc.list_indexes()
]

if PINECONE_INDEX_NAME not in existing_indexes:

    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=3072,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(
    PINECONE_INDEX_NAME
)

vectorstore = PineconeVectorStore(
    index,
    embeddings,
    text_key="text"
)