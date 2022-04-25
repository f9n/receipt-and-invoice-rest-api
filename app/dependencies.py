from fastapi import HTTPException
from beanie import PydanticObjectId

from app.models import ReceiptInDB, ReceiptOcrResultInDb


async def get_receipt(receipt_id: PydanticObjectId) -> ReceiptInDB:
    receipt = await ReceiptInDB.get(receipt_id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt


async def get_receipt_ocr_result(image_id: str) -> ReceiptOcrResultInDb:
    receipt_ocr_result = await ReceiptOcrResultInDb.find_all(
        ReceiptOcrResultInDb.image_id == image_id
    )
    if receipt_ocr_result is None:
        raise HTTPException(status_code=404, detail="Receipt Ocr Result not found")
    return receipt_ocr_result
