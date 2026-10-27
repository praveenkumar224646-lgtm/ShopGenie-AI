
import mlflow
from mlops.tracking import start_tracking


def test_mlflow_tracking():
    start_tracking()

    runs = mlflow.search_runs(
        experiment_names=["ShopGenie-AI-RAG"],
        output_format="pandas"
    )

    assert not runs.empty
    assert runs.iloc[0]["status"] == "FINISHED"
    assert runs.iloc[0]["metrics.rag_tests_passed"] == 3
    assert runs.iloc[0]["params.project"] == "ShopGenie AI"
