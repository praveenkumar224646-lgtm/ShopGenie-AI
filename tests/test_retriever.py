
from rag.retriever import retrieve_documents


def test_retrieve_documents_returns_results():
    results = retrieve_documents("laptop", top_k=5)

    assert isinstance(results, list)
    assert len(results) <= 5

from rag.retriever import retrieve_documents


def test_retrieve_documents_returns_results():
    results = retrieve_documents("laptop", top_k=5)

    assert isinstance(results, list)
    assert len(results) <= 5


def test_category_filter_returns_matching_category():
    results = retrieve_documents("laptop", top_k=5, category="Laptop")

    for result in results:
        category = result["metadata"].get("category")
        assert category == "Laptop"
