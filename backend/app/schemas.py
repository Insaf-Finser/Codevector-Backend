from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CursorResponse(BaseModel):
    updated_at: datetime
    id: int


class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    next_cursor: Optional[str]