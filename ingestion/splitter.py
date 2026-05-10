from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=250,
    separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
)

def split_documents(documents):
    return splitter.split_documents(documents)