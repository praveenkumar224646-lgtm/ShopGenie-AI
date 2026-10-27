
from rag.product_comparator import compare_products


def choose_shopping_action(query):
    query_lower = query.lower()

    if any(word in query_lower for word in ["compare", "difference", "vs"]):
        return "compare"

    if any(word in query_lower for word in ["recommend", "suggest", "best", "buy"]):
        return "recommend"

    if any(word in query_lower for word in ["find", "search", "show", "under"]):
        return "search"

    return "search"


def run_shopping_agent(query):
    action = choose_shopping_action(query)

    if action == "compare":
        task = "Compare the matching products and explain their differences."
    elif action == "recommend":
        task = "Recommend the best suitable products for the user's needs."
    else:
        task = "Search for products matching the user's requirements."

    return {
        "query": query,
        "action": action,
        "task": task
    }


def execute_shopping_agent(query):
    action = choose_shopping_action(query)

    if action == "compare":
        query_lower = query.lower()

        product_names = [
            "ASUS Vivobook 15",
            "HP Victus",
            "Lenovo LOQ",
            "MacBook Air M3",
            "iPhone 16",
            "Samsung Galaxy S25",
            "OnePlus 13"
        ]

        matched_products = [
            name for name in product_names
            if name.lower() in query_lower
        ]

        if len(matched_products) < 2:
            return {
                "action": action,
                "result": {
                    "error": "Please mention two products to compare."
                }
            }

        comparison = compare_products(
            matched_products[0],
            matched_products[1]
        )

        return {
            "action": action,
            "result": comparison
        }

    return {
        "action": action,
        "result": {
            "task": (
                "Recommend the best suitable products "
                "for the user's needs."
                if action == "recommend"
                else "Search for products matching the user's requirements."
            )
    }
}
