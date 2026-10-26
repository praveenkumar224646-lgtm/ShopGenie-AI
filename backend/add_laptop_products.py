from rag.vector_store import update_documents

products = [
    {
        "id": "asus_vivobook_15",
        "text": (
        "Product: ASUS Vivobook 15 (X1504). "
        "Category: Laptop. "
        "Starting price: Rs. 52000. "
        "Suitable for everyday use and coding."
),
        "metadata": {
            "product": "ASUS Vivobook 15 (X1504)",
            "category": "Laptop",
            "price": 52000,
            "source": "ASUS India Official Website"
}
    },
    {
        "id": "lenovo_loq",
        "text": (
            "Product: Lenovo-loq-15-ahp-11-laptop. "
            "Category: Laptop. "
            "Price: ₹1,57,165 "
            "Suitable for gaming, programming and heavy workloads."
        ),
        "metadata": {
            "product": "Lenovo-loq-15-ahp-11-laptop",
            "price": 157165,
            "category": "Laptop",
            "source": "ShopGenie Product Database"
        }
    },
    {
        "id": "macbook_air_m3",
        "text": (
            "Product: MacBook Air M3. "
            "Category: Laptop. "
            "Price: ₹1,34,900. "
            "Suitable for software development and everyday use."
        ),
        "metadata": {
            "product": "MacBook Air M3",
            "price": 134900,
            "category": "Laptop",
            "source": "ShopGenie Product Database"
        }
    },
    {
        "id": "hp_victus",
        "text": (
            "Product: Hp Victus 15 Intel Core I5 13th Gen 13420h 16 Gb/512 Gb. "
            "Category: Laptop. "
            "Price: ₹72000 . "
            "Suitable for programming, gaming and machine learning."
        ),
        "metadata": {
            "product": "Hp Victus 15 Intel Core I5 13th Gen 13420h 16 Gb/512 Gb",
            "price": 72000,
            "category": "Laptop",
            "source": "ShopGenie Product Database"
        }
    }
]

update_documents(
    documents=[p["text"] for p in products],
    ids=[p["id"] for p in products],
    metadatas=[p["metadata"] for p in products]
)

print("Laptop products updated successfully!")