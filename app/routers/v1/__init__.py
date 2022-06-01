import io

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.dependencies import get_image
from app.models import ImageInDB
from app.schemas import ProductCategory
from .receipt import router as receipt_router
from .invoice import router as invoice_router
from .ocr import router as ocr_router

router = APIRouter()


@router.get("/configs")
async def get_configs():
    return {"product": {"categories": ProductCategory.list()}}


@router.get("/images/{image_id}")
async def get_image(image: ImageInDB = Depends(get_image)):
    content_type = image.content_type

    # def iterfile():
    #     yield image.content

    out_image = io.BytesIO(image.content)

    return StreamingResponse(out_image, media_type=content_type)


# def iterfile():
#     with open(some_file_path, mode="rb") as file_like:
#         yield from file_like

# return StreamingResponse(iterfile(), media_type="video/mp4")

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

router.include_router(
    invoice_router,
    prefix="/invoices",
    tags=["invoices"],
)
