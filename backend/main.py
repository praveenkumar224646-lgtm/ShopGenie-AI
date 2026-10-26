
from fastapi import FastAPI
from pydantic import BaseModel

from rag.retriever import rag_search
from llm.gemini import generate_response


app = FastAPI(
    title="ShopGenie AI API",
    description="Backend API for ShopGenie AI",
    version="1.2.0"
)


class SearchRequest(BaseModel):
    query: str
    budget: float
    category: str


@app.get("/")
def root():
    return {
        "message": "ShopGenie AI Backend is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/search")
def search_product(request: SearchRequest):
    rag_result = rag_search(
        query=request.query,
        top_k=10,
        category=request.category
    )

    results = rag_result.get("results", [])

    matching_products = [
        p for p in results
        if p.get("metadata", {}).get("price") is not None
        and float(p["metadata"]["price"]) <= request.budget
    ]

    unpriced_products = [
        p for p in results
        if p.get("metadata", {}).get("price") is None
    ]

    if matching_products:
        products_to_show = matching_products[:8]
        price_note = "Products listed have recorded prices within budget."
    elif unpriced_products:
        products_to_show = unpriced_products[:8]
        price_note = (
            "Prices are unavailable. Do not claim these products "
            "are within the user's budget."
        )
    else:
        return {
            "query": request.query,
            "budget": request.budget,
            "category": request.category,
            "answer": "No matching products were found.",
            "sources": []
        }

    context = "\n\n".join(
        p.get("content", "") for p in products_to_show
    )

    agent_query = f"""
Recommend products for: {request.query}
Budget: Rs. {request.budget:.0f}
Category: {request.category}

{price_note}

Use only the supplied catalog. Never invent prices or specifications.
Explain the best match, alternatives, and final verdict.

Catalog:
{context}
"""

    try:
        answer = generate_response(
            query=agent_query,
            context=context
        )
    except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            answer = (
                "Gemini quota exceeded temporarily.\n\n" + context
            )
        else:
            answer = "AI response failed. Product details:\n\n" + context

    return {
        "query": request.query,
        "budget": request.budget,
        "category": request.category,
        "answer": answer,
        "sources": products_to_show
    }
