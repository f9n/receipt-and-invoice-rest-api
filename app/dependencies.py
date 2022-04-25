from fastapi import HTTPException
from beanie import PydanticObjectId

from app.models import ImageInDB, ReceiptInDB, ReceiptOcrResultInDB


async def get_receipt(receipt_id: PydanticObjectId) -> ReceiptInDB:
    receipt = await ReceiptInDB.get(receipt_id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt


async def get_receipt_ocr_result(image_id: str) -> ReceiptOcrResultInDB:
    receipt_ocr_result = await ReceiptOcrResultInDB.find_all(
        ReceiptOcrResultInDB.image_id == image_id
    )
    if receipt_ocr_result is None:
        raise HTTPException(status_code=404, detail="Receipt Ocr Result not found")
    return receipt_ocr_result


async def get_image(image_id: PydanticObjectId) -> ImageInDB:
    image = await ImageInDB.get(image_id)
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return image
