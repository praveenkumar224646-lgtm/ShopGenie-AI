
import os
import time
import traceback
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(timeout=60000)
)


def generate_response(query, context):
    prompt = f"""
You are ShopGenie AI, an intelligent AI shopping assistant.

Understand the user's requirements, compare products in the
provided catalog, and recommend the best suitable options.

Rules:
- Recommend only products present in the supplied catalog.
- Respect the user's budget.
- Never invent prices, specifications, or features.
- Explain why each recommendation matches the user's needs.
- If no suitable product exists, say so clearly.
- Be concise, friendly, and professional.

PRODUCT CATALOG:
{context}

USER REQUIREMENT:
{query}

Provide your recommendation using the catalog as the source of truth.
"""

    start = time.time()
    print("ShopGenie AI analysis started...", flush=True)

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        answer = response.text

        print(
            f"AI response time: {time.time() - start:.2f} seconds",
            flush=True
        )

        if not answer:
            return "Sorry, I couldn't generate a recommendation. Please try again."

        return answer

    except Exception:
        print("Gemini API error details:", flush=True)
        traceback.print_exc()
        raise
