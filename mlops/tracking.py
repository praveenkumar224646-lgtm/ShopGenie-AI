
import mlflow


def start_tracking():
    mlflow.set_experiment("ShopGenie-AI-RAG")

    with mlflow.start_run():
        mlflow.log_param("project", "ShopGenie AI")
        mlflow.log_param("system", "RAG")
        mlflow.log_metric("rag_tests_passed", 3)

        mlflow.log_param("llm_provider", "Google Gemini")
        mlflow.log_param("vector_database", "ChromaDB")

        print("ShopGenie AI experiment logged successfully!")
