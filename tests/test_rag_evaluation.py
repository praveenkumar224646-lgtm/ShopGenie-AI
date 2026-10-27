import mlflow

from rag.retriever import retrieve_documents


EVALUATION_CASES = [
    {
        "query": "ASUS Vivobook 15 laptop",
        "expected_product": "asus_vivobook_15",
        "category": "Laptop",
    },
    {
        "query": "HP Victus laptop for gaming",
        "expected_product": "hp_victus",
        "category": "Laptop",
    },
    {
        "query": "Samsung Galaxy S25 with 12GB RAM",
        "expected_product": "samsung_galaxy_s25",
        "category": "Mobile",
    },
    {
        "query": "OnePlus 13 with 256GB storage",
        "expected_product": "oneplus_13",
        "category": "Mobile",
    },
]


def evaluate_retrieval():
    hits = []
    reciprocal_ranks = []
    distances = []

    for case in EVALUATION_CASES:
        results = retrieve_documents(
            query=case["query"],
            top_k=5,
            category=case["category"],
        )

        expected_id = case["expected_product"]

        matching_rank = None

        for rank, result in enumerate(results, start=1):
            product_name = (
                result.get("metadata", {}).get("product", "").lower()
            )

            expected_names = {
                "asus_vivobook_15": "asus vivobook 15",
                "hp_victus": "hp victus",
                "samsung_galaxy_s25": "samsung galaxy s25",
                "oneplus_13": "oneplus 13",
            }

            if expected_names[expected_id] in product_name:
                matching_rank = rank
                break

        hits.append(1 if matching_rank is not None else 0)

        reciprocal_ranks.append(
            1 / matching_rank if matching_rank is not None else 0
        )

        for result in results:
            distance = result.get("distance")
            if distance is not None:
                distances.append(float(distance))

    return {
        "hit_rate": sum(hits) / len(hits),
        "mrr": sum(reciprocal_ranks) / len(reciprocal_ranks),
        "average_distance": (
            sum(distances) / len(distances) if distances else 0
        ),
        "evaluation_cases": len(EVALUATION_CASES),
        "hits": sum(hits),
    }


def log_evaluation_to_mlflow(metrics):
    mlflow.set_experiment("ShopGenie-AI-RAG")

    with mlflow.start_run(run_name="RAG-Retrieval-Evaluation"):
        mlflow.log_param("project", "ShopGenie AI")
        mlflow.log_param("evaluation_type", "retrieval")
        mlflow.log_param("evaluation_cases", metrics["evaluation_cases"])

        mlflow.log_metric("retrieval_hit_rate", metrics["hit_rate"])
        mlflow.log_metric("retrieval_mrr", metrics["mrr"])
        mlflow.log_metric("average_retrieval_distance", metrics["average_distance"])

    print("RAG evaluation logged to MLflow.")
    print(metrics)
    
def test_rag_retrieval_evaluation():
    metrics = evaluate_retrieval()

    assert metrics["evaluation_cases"] == 4
    assert metrics["hits"] == 4
    assert metrics["hit_rate"] == 1.0
    assert metrics["mrr"] == 1.0