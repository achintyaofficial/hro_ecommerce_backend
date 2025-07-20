def product_response(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product.get("description"),
        "price": product["price"],
        "size": product.get("size")
    }

def product_list(products) -> list:
    return [product_response(p) for p in products]