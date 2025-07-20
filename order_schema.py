def order_response(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": order["user_id"],
        "product_ids": order["product_ids"]
    }

def order_list(orders) -> list:
    return [order_response(o) for o in orders]