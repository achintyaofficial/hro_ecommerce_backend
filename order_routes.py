from fastapi import APIRouter, Path, Query
from models.order import OrderModel
from db.mongo import order_collection
from schemas.order_schema import order_response, order_list

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: OrderModel):
    result = await order_collection.insert_one(order.dict())
    new_order = await order_collection.find_one({"_id": result.inserted_id})
    return order_response(new_order)

@router.get("/orders/{user_id}", status_code=200)
async def get_orders(user_id: str = Path(...), limit: int = 10, offset: int = 0):
    query = {"user_id": user_id}
    cursor = order_collection.find(query).skip(offset).limit(limit).sort("_id")
    orders = await cursor.to_list(length=limit)
    return order_list(orders)