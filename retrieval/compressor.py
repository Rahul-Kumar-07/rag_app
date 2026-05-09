from langchain.retrievers.document_compressors import (
    EmbeddingsFilter
)

from core.embeddings import embeddings

compressor = EmbeddingsFilter(
    embeddings=embeddings,
    similarity_threshold=0.75
)

async def compress_docs(query, docs):

    return await compressor.acompress_documents(
        docs,
        query
    )