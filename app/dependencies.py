from fastapi import HTTPException
from beanie import PydanticObjectId

from app.models import (
    ImageInDB,
    ReceiptInDB,
    ReceiptOcrResultInDB,
    InvoiceInDB,
    InvoiceOcrResultInDB,
)


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


async def get_invoice(invoice_id: PydanticObjectId) -> InvoiceInDB:
    invoice = await InvoiceInDB.get(invoice_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


async def get_invoice_ocr_result(image_id: str) -> InvoiceOcrResultInDB:
    invoice_ocr_result = await InvoiceOcrResultInDB.find_all(
        InvoiceOcrResultInDB.image_id == image_id
    )
    if invoice_ocr_result is None:
        raise HTTPException(status_code=404, detail="Invoice Ocr Result not found")
    return invoice_ocr_result


async def get_image(image_id: PydanticObjectId) -> ImageInDB:
    image = await ImageInDB.get(image_id)
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return image
