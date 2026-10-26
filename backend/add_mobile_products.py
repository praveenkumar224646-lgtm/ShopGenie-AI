
from rag.vector_store import update_documents

products = [
    {
        "id": "iphone_16",
        "text": (
            "Product: Apple iPhone 16. "
            "Category: Mobile. "
            "Price: Rs. 69900. "
            "Display: 6.1-inch OLED. "
            "Storage: 128GB. "
            "RAM: 8GB. "
            "Processor: Apple A18. "
            "Camera: 48MP main camera. "
            "Battery: Built-in rechargeable battery. "
            "Use: Everyday use, photography and performance."
        ),
        "metadata": {
            "category": "Mobile",
            "product": "Apple iPhone 16",
            "price": 69900,
            "ram": "8GB",
            "storage": "128GB",
            "source": "ShopGenie Product Database"
        }
    },
    {
        "id": "samsung_galaxy_s25",
        "text": (
            "Product: Samsung Galaxy S25. "
            "Category: Mobile. "
            "Price: Rs. 80999. "
            "Display: 6.2-inch Dynamic AMOLED 2X. "
            "Storage: 128GB. "
            "RAM: 12GB. "
            "Processor: Snapdragon 8 Elite for Galaxy. "
            "Camera: 50MP main camera. "
            "Use: Multitasking, photography and premium performance."
        ),
        "metadata": {
            "category": "Mobile",
            "product": "Samsung Galaxy S25",
            "price": 80999,
            "ram": "12GB",
            "storage": "128GB",
            "source": "ShopGenie Product Database"
        }
    },
    {
        "id": "oneplus_13",
        "text": (
            "Product: OnePlus 13. "
            "Category: Mobile. "
            "Price: Rs. 69999. "
            "Display: 6.82-inch AMOLED. "
            "Storage: 256GB. "
            "RAM: 12GB. "
            "Processor: Snapdragon 8 Elite. "
            "Camera: 50MP main camera. "
            "Battery: 6000mAh. "
            "Use: Gaming, multitasking and fast performance."
        ),
        "metadata": {
            "category": "Mobile",
            "product": "OnePlus 13",
            "price": 69999,
            "ram": "12GB",
            "storage": "256GB",
            "source": "ShopGenie Product Database"
        }
    }
]


update_documents(
    documents=[product["text"] for product in products],
    ids=[product["id"] for product in products],
    metadatas=[product["metadata"] for product in products]
)

print("Mobile products updated successfully!")