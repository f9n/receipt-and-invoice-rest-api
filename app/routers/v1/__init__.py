from io import BytesIO

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse

from app.schemas import ProductCategory

from .receipt import router as receipt_router
from .ocr import router as ocr_router

router = APIRouter()


@router.get("/configs")
async def get_configs():
    return {"product": {"categories": ProductCategory.list()}}


@router.get("/images/{image_id}")
async def get_image():
    return {"message": "Send image"}


# @router.get("/download/{name_file}")
# def download_file(name_file: str):
#     return FileResponse(path=getcwd() + "/" + name_file, media_type='application/octet-stream', filename=name_file)

# @router.get("/file/{name_file}")
# def get_file(name_file: str):
#     return FileResponse(path=getcwd() + "/" + name_file)

# @app.post("/image_filter")
# def image_filter(img: UploadFile = File(...)):
#     original_image = Image.open(img.file)
#     original_image = original_image.filter(ImageFilter.BLUR)

#     filtered_image = BytesIO()
#     original_image.save(filtered_image, "JPEG")
#     filtered_image.seek(0)

#     return StreamingResponse(filtered_image, media_type="image/jpeg")

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
