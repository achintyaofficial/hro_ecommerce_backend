from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    name: str
    description: Optional[str]
    price: float
    size: Optional[str]