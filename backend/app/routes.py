from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends,Query 
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app.models import Product
from app.schemas import ProductListResponse
from app.utils import decode_cursor
from app.schemas import ProductCreate

router = APIRouter()


@router.get("/products", response_model=ProductListResponse)
def list_products(
    limit: int = Query(20, ge=1, le=100),
    category: Optional[str] = None,
    cursor: Optional[str] = None,
    db: Session = Depends(get_db),
):
    cursor_updated_at = None
    cursor_id = None

    if cursor:
        cursor_updated_at, cursor_id = decode_cursor(cursor)

    return crud.get_products(
        db=db,
        limit=limit,
        category=category,
        cursor_updated_at=cursor_updated_at,
        cursor_id=cursor_id,
    )

@router.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product