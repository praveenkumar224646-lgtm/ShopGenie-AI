
from .vector_store import get_vector_store


def get_product_details(product_name):
    collection = get_vector_store()

    data = collection.get(include=["metadatas", "documents"])

    product_name = product_name.strip().lower()

    for i, metadata in enumerate(data.get("metadatas", [])):
        metadata = metadata or {}
        name = metadata.get("product", "")

        if product_name in name.lower() or name.lower() in product_name:
            document = data.get("documents", [])[i]

            return {
                "product": name,
                "category": metadata.get("category", "Unknown"),
                "price": metadata.get("price"),
                "ram": metadata.get("ram", "Not available"),
                "storage": metadata.get("storage", "Not available"),
                "processor": metadata.get("processor", "Not available"),
                "source": metadata.get("source", "Unknown"),
                "description": document
            }

    return None



def compare_products(product1, product2):
    first = get_product_details(product1)
    second = get_product_details(product2)

    if not first or not second:
        return {
            "error": "One or both products were not found in the catalog."
        }

    if first["category"] != second["category"]:
        return {
            "error": "Please select products from the same category."
        }

    price1 = first.get("price")
    price2 = second.get("price")

    if price1 is not None and price2 is not None:
        if price1 < price2:
            cheaper = first["product"]
        elif price2 < price1:
            cheaper = second["product"]
        else:
            cheaper = "Both products have the same price"
    else:
        cheaper = "Price comparison unavailable"

    return {
        "product1": first,
        "product2": second,
        "comparison": {
            "price_difference": (
                abs(price1 - price2)
                if price1 is not None and price2 is not None
                else None
            ),
            "cheaper_product": cheaper,
            "same_category": True
        }
    }

