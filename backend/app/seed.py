import random
from datetime import datetime, timedelta

from app.database import SessionLocal
from app.models import Product

db = SessionLocal()

categories = [
    "Electronics",
    "Books",
    "Furniture",
    "Fashion",
    "Sports",
    "Beauty",
    "Toys",
    "Home",
    "Automotive",
    "Groceries"
]

BATCH_SIZE = 1000
TOTAL = 200000

products = []

for i in range(1, TOTAL + 1):

    now = datetime.utcnow() - timedelta(
        days=random.randint(0, 365)
    )

    products.append(
        Product(
            name=f"Product {i}",
            category=random.choice(categories),
            price=round(random.uniform(10, 5000), 2),
            created_at=now,
            updated_at=now,
        )
    )

    if len(products) == BATCH_SIZE:
        db.bulk_save_objects(products)
        db.commit()
        products.clear()
        print(f"Inserted {i}")

if products:
    db.bulk_save_objects(products)
    db.commit()

db.close()

print("Done!")