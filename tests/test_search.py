import requests

BASE_URL = "http://127.0.0.1:8000"

def test_search_returns_success():
    payload = {
        "query": "Best laptop for coding",
        "budget": 80000,
        "category": "Laptop"
    }

    response = requests.post(
        f"{BASE_URL}/search",
        json=payload,
        timeout=120
    )

    assert response.status_code == 200

    data = response.json()

    assert "query" in data
    assert "budget" in data
    assert "category" in data
    assert "answer" in data
    assert "sources" in data

def test_search_rejects_negative_budget():
    payload = {
        "query": "gaming laptop",
        "budget": -100,
        "category": "Laptop"
    }

    response = requests.post(
        f"{BASE_URL}/search",
        json=payload,
        timeout=10
    )

    assert response.status_code == 422


def test_search_rejects_empty_query():
    payload = {
        "query": "",
        "budget": 60000,
        "category": "Laptop"
    }

    response = requests.post(
        f"{BASE_URL}/search",
        json=payload,
        timeout=10
    )

    assert response.status_code == 422
