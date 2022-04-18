from fastapi import APIRouter

router = APIRouter()


@router.post("/ocr/receipt")
async def ocr_from_receipt():
    return {"message": "Get image and Send image_id field to you"}


@router.get("/ocr/receipt/{image_id}")
async def get_receipt_ocr_result():
    return {"message": "Send receipt ocr result"}
