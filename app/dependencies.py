from fastapi import HTTPException
from beanie import PydanticObjectId

from app.models import ReceiptInDB


async def get_receipt(receipt_id: PydanticObjectId) -> ReceiptInDB:
    receipt = await ReceiptInDB.get(receipt_id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt
