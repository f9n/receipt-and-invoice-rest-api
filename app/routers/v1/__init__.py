from fastapi import APIRouter

from .receipt import router as receipt_router
from .ocr import router as ocr_router

router = APIRouter()


@router.get("/configs")
async def get_configs():
    return {
        "product": {
            "categories": ["giyim", "icecek", "yiyecek", "teknoloji", "kirtasiye"]
        }
    }


@router.get("/images/{image_id}")
async def get_image():
    return {"message": "Send image"}


router.include_router(
    ocr_router,
    prefix="/ocr",
    tags=["ocr"],
)

router.include_router(
    receipt_router,
    prefix="/receipts",
    tags=["receipts"],
)
