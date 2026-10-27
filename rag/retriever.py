
from .vector_store import get_vector_store


def retrieve_documents(query, top_k=5, category=None):
    collection = get_vector_store()

    total_documents = collection.count()

    if total_documents == 0:
        return []

    where_filter = None

    if category and category.lower() != "all":
        where_filter = {"category": {"$eq": category}}

    query_args = {
        "query_texts": [query],
        "n_results": min(top_k, total_documents),
        "include": ["documents", "metadatas", "distances"]
    }

    if where_filter:
        query_args["where"] = where_filter

    results = collection.query(**query_args)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    retrieved = []

    for i, content in enumerate(documents):
        metadata = metadatas[i] if i < len(metadatas) else {}
        distance = distances[i] if i < len(distances) else None

        retrieved.append({
            "content": content,
            "metadata": metadata or {},
            "distance": distance
        })

    return retrieved


def build_context_from_documents(documents):
    if not documents:
        return "No relevant information was found."

    parts = []

    for i, document in enumerate(documents, start=1):
        metadata = document["metadata"]
        source = metadata.get("source", "Unknown")

        parts.append(
            f"SOURCE {i}\n"
            f"Source: {source}\n\n"
            f"{document['content']}"
        )

    return "\n\n".join(parts)


def build_context(query, top_k=5, category=None):
    documents = retrieve_documents(
        query=query,
        top_k=top_k,
        category=category
    )

    return build_context_from_documents(documents)


def rag_search(query, top_k=5, category=None):
    documents = retrieve_documents(
        query=query,
        top_k=top_k,
        category=category
    )

    return {
        "query": query,
        "results": documents,
        "context": build_context_from_documents(documents)
    }
