from ingestion.loader import load_file
from ingestion.splitter import split_documents
from core.vectorstore import vectorstore

def ingest_file(path: str, user_id: str):

    docs = load_file(path)

    split_docs = split_documents(docs)

    vectorstore.add_documents(
        split_docs,
        namespace=user_id
    )

    return len(split_docs)