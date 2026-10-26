import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction


def get_embedding_function():
    """
    Returns the default embedding function provided by ChromaDB.
    """

    embedding_function = DefaultEmbeddingFunction()

    return embedding_function