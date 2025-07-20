from fastapi import APIRouter, Query
from models.product import ProductModel
from db.mongo import product_collection
from schemas.product_schema import product_response, product_list
import re

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductModel):
    result = await product_collection.insert_one(product.dict())
    new_product = await product_collection.find_one({"_id": result.inserted_id})
    return product_response(new_product)

@router.get("/products", status_code=200)
async def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": re.compile(name, re.IGNORECASE)}
    if size:
        query["size"] = size
    cursor = product_collection.find(query).skip(offset).limit(limit).sort("_id")
    products = await cursor.to_list(length=limit)
    return product_list(products)