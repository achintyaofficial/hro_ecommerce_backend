from pydantic import BaseModel
from typing import List

class OrderModel(BaseModel):
    user_id: str
    product_ids: List[str]