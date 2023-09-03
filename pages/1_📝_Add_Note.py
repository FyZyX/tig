import time
import typing
import uuid

import chromadb
import streamlit
from chromadb.utils import embedding_functions

import config

VectorCollection: typing.TypeAlias = chromadb.Collection


def initialize_vector_store(collection_name: str) -> VectorCollection:
    chroma_client = chromadb.PersistentClient()
    embedding_function = embedding_functions.CohereEmbeddingFunction(
        api_key=config.COHERE_API_KEY,
        model_name="large",
    )
    collection = chroma_client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function,
    )
    return collection


def main():
    collection = initialize_vector_store("notes")

    content = streamlit.text_area("Note")

    if streamlit.button("Save"):
        collection.add(
            ids=[f"note-{uuid.uuid4()}"],
            metadatas=[{"timestamp": int(time.time())}],
            documents=[content],
        )


if __name__ == '__main__':
    main()
