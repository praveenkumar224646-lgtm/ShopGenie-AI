
from rag.retriever import retrieve_documents


def test_retrieve_documents_returns_results():
    results = retrieve_documents("laptop", top_k=5)

    assert isinstance(results, list)
    assert len(results) <= 5
