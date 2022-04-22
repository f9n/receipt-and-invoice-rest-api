from fastapi import APIRouter

router = APIRouter()


@router.post("/receipt")
async def ocr_from_receipt():
    return {"message": "Get image and Send image_id field to you"}


@router.get("/receipt/{image_id}")
async def get_receipt_ocr_result():
    return {"message": "Send receipt ocr result"}


@router.post("/invoice")
async def ocr_from_invoice():
    return {"message": "Get image and Send image_id field to you"}


@router.get("/invoice/{image_id}")
async def get_invoice_ocr_result():
    return {"message": "Send invoice ocr result"}
