import os
import chromadb

from .embeddings import get_embedding_function


# ---------------------------------------------------------
# Vector database configuration
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHROMA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "chroma_db"
)

COLLECTION_NAME = "shopgenie_products"


# ---------------------------------------------------------
# Create / Get ChromaDB
# ---------------------------------------------------------

def get_vector_store():

    os.makedirs(CHROMA_PATH, exist_ok=True)

    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    embedding_function = get_embedding_function()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function,
        metadata={
            "description": "ShopGenie AI product knowledge base"
        }
    )

    return collection


# ---------------------------------------------------------
# Add documents
# ---------------------------------------------------------

def add_documents(
    documents,
    ids,
    metadatas=None
):

    collection = get_vector_store()

    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    return {
        "status": "success",
        "message": f"{len(documents)} documents added."
    }


# ---------------------------------------------------------
# Update documents
# ---------------------------------------------------------

def update_documents(
    documents,
    ids,
    metadatas=None
):

    collection = get_vector_store()

    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    return {
        "status": "success",
        "message": f"{len(documents)} documents updated."
    }


# ---------------------------------------------------------
# Delete document
# ---------------------------------------------------------

def delete_document(document_id):

    collection = get_vector_store()

    collection.delete(
        ids=[document_id]
    )

    return {
        "status": "success",
        "message": f"Document {document_id} deleted."
    }


# ---------------------------------------------------------
# Get collection information
# ---------------------------------------------------------

def get_collection_count():

    collection = get_vector_store()

    return collection.count()