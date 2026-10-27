# ShopGenie AI
### Intelligent Commerce — RAG-Powered Product Discovery

ShopGenie AI is an AI-powered shopping assistant that helps users discover products, compare alternatives, and receive personalized product recommendations based on their requirements and budget.

## Features

- **Smart Product Search:** Find products using natural-language queries.
- **Product Comparison:** Compare two products and understand their differences.
- **AI Recommendations:** Get product suggestions powered by Google Gemini.
- **Retrieval-Augmented Generation (RAG):** Retrieve relevant product information from the product knowledge base before generating answers.
- **Shopping Agent:** Identify whether a user wants to search, compare, or receive recommendations.
- **Search History:** Store and access previous searches.
- **MLOps and Evaluation:** Track RAG evaluation metrics using MLflow.
- **Automated Testing:** Run project tests using pytest.
- **Continuous Integration:** Validate code using GitHub Actions.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend API | FastAPI |
| Language | Python |
| LLM | Google Gemini |
| Vector Database | ChromaDB |
| Relational Database | SQLite |
| RAG Evaluation and Experiment Tracking | MLflow |
| Testing | pytest |
| CI/CD | GitHub Actions |

## Architecture

1. The user enters a product query through the Streamlit interface.
2. The FastAPI backend receives the search request.
3. The shopping agent identifies the intended action.
4. The RAG system retrieves relevant product information from ChromaDB.
5. Google Gemini generates a response using the retrieved context.
6. The application displays product results, comparisons, or recommendations.
7. Search history and evaluation metrics are stored using the configured tracking mechanisms.

## Project Structure

```text
ShopGenie-AI/
├── agents/
│   └── shopping_agent.py
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
├── mlops/
│   └── tracking.py
├── tests/
├── .github/
│   └── workflows/
├── .env
├── .gitignore
└── README.md
```

*Note: This is a high-level structure. Some folders may contain additional files.*

## Prerequisites

- Python 3.12 recommended for a compatible environment.
- A Google Gemini API key.
- Git.
- VS Code or another Python IDE.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/praveenkumar224646-lgtm/ShopGenie-AI.git
cd ShopGenie-AI
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If the repository contains `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure your Gemini API key:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own API key. Never commit secrets to GitHub.

### 5. Start the backend

From the project root:

```powershell
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Backend API documentation:

http://127.0.0.1:8000/docs

### 6. Start the frontend

Open a second terminal, activate the virtual environment, and run:

```powershell
python -m streamlit run frontend/app.py
```

Open the local URL displayed in the terminal.

## Testing

Run the complete test suite:

```powershell
python -m pytest -q
```

The project test suite has previously completed successfully with **9 passed**.

## RAG Evaluation and MLflow

The RAG evaluation workflow measures retrieval quality using metrics such as:

- **Retrieval Hit Rate:** Measures whether relevant information is retrieved.
- **Mean Reciprocal Rank (MRR):** Measures the ranking position of relevant results.
- **Average Retrieval Distance:** Measures the distance associated with retrieved results.

Previously recorded evaluation results included a retrieval hit rate of 1.0, MRR of 1.0, and average retrieval distance of approximately 1.07381. Results may vary when the evaluation data or configuration changes.

## Future Improvements

- Improve shopping-agent planning and action execution.
- Expand the product catalogue.
- Add more retrieval evaluation cases.
- Improve recommendation quality and error handling.
- Expand automated tests and deployment support.

## Disclaimer

ShopGenie AI is an academic project intended to demonstrate AI-assisted product discovery, RAG, shopping-agent workflows, and MLOps evaluation. Recommendations depend on the available product catalogue and retrieved information.

## Author

Developed as an academic project using Python, generative AI, RAG, and MLOps technologies.
