import base64
import json
from datetime import datetime


def encode_cursor(updated_at: datetime, product_id: int) -> str:
    cursor = {
        "updated_at": updated_at.isoformat(),
        "id": product_id,
    }

    return base64.urlsafe_b64encode(
        json.dumps(cursor).encode()
    ).decode()


def decode_cursor(cursor: str):
    decoded = json.loads(
        base64.urlsafe_b64decode(cursor.encode()).decode()
    )

    return (
        datetime.fromisoformat(decoded["updated_at"]),
        decoded["id"],
    )