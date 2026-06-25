from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from app.models import Product
from app.utils import encode_cursor

def get_products(
    db: Session,
    limit: int = 20,
    cursor_updated_at=None,
    cursor_id=None,
    category=None,
):
    query = db.query(Product)

    # Category filter
    if category:
        query = query.filter(Product.category == category)

    # Cursor pagination
    if cursor_updated_at and cursor_id:
        query = query.filter(
            or_(
                Product.updated_at < cursor_updated_at,
                and_(
                    Product.updated_at == cursor_updated_at,
                    Product.id < cursor_id,
                ),
            )
        )

    products = (
        query.order_by(
            Product.updated_at.desc(),
            Product.id.desc(),
        )
        .limit(limit)
        .all()
    )

    next_cursor = None

    if products:
        last = products[-1]

        next_cursor = encode_cursor(
            last.updated_at,
            last.id
        )

    return {
        "products": products,
        "next_cursor": next_cursor,
    }