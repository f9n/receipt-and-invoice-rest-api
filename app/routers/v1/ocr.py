import logging
import datetime

from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from fastapi.logger import logger

from app.models import ImageInDB, ReceiptOcrResultInDB, InvoiceOcrResultInDB
from app.schemas import Product, ProductCategory
from app.dependencies import get_receipt_ocr_result, get_invoice_ocr_result
from app.services import get_product_categories, send_ocr_request

router = APIRouter()


@router.post("/receipt", response_model=ReceiptOcrResultInDB)
async def ocr_result_from_receipt_image(image: UploadFile = File(...)):
    logger.info(f"Filename: {image.filename}")
    logger.info(f"Filename Content Type: {image.content_type}")

    if image.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
        raise HTTPException(
            status_code=405, detail="Allowed image files are in PNG or JPG format"
        )

    image_content = await image.read()
    image_db = await ImageInDB(
        name=image.filename,
        content_type=image.content_type,
        size=len(image_content),
        content=image_content,
    ).create()

    logger.info(f"ImageDb Name: {image_db.name}")
    logger.info(f"ImageDb Id: {image_db.id}")
    image_id = image_db.id

    await image.seek(0)
    logger.info(f"Image Seek to 0")

    # result = await send_ocr_request(file=image, language="tur")

    # async with aiofiles.open(filepath, 'wb') as f:
    #     while buffer := await image.read(1024):
    #         await f.write(buffer)

    #     await f.close()

    # filename = secure_filename(f"{str(uuid.uuid4())}_{image.filename}")
    # id = pymongo.save_file(filename, image, base="images")

    # Move file cursor to beginning
    # await image.seek(0)

    receipt_ocr_result = await ReceiptOcrResultInDB(
        firm=f"Okey: {datetime.datetime.now(tz=datetime.timezone.utc)}",
        no="021",
        date="22/05/2022",
        total_amount="72,5",
        total_kdv="2,5",
        image_id=image_id,
        products=[
            Product(
                name="yag",
                quantity=1,
                unit_price="70",
                ratio_kdv=8,
                category=ProductCategory.YIYECEK,
            )
        ],
    ).create()

    logger.info("Created Receipt Ocr Result")

    return receipt_ocr_result


@router.get("/receipt", response_model=list[ReceiptOcrResultInDB])
async def get_all_receipt_ocr_results():
    return await ReceiptOcrResultInDB.find_all().to_list()


@router.get("/receipt/{image_id}", response_model=ReceiptOcrResultInDB)
async def get_receipt_ocr_result(
    receipt_ocr_result: ReceiptOcrResultInDB = Depends(get_receipt_ocr_result),
):
    return receipt_ocr_result


@router.post("/invoice", response_model=InvoiceOcrResultInDB)
async def ocr_result_from_invoice_image(image: UploadFile = File(...)):
    logger.info(f"Filename: {image.filename}")
    logger.info(f"Filename Content Type: {image.content_type}")

    if image.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
        raise HTTPException(
            status_code=405, detail="Allowed image files are in PNG or JPG format"
        )

    image_content = await image.read()
    image_db = await ImageInDB(
        name=image.filename,
        content_type=image.content_type,
        size=len(image_content),
        content=image_content,
    ).create()

    logger.info(f"ImageDb Name: {image_db.name}")
    logger.info(f"ImageDb Id: {image_db.id}")
    image_id = image_db.id

    await image.seek(0)
    logger.info(f"Image Seek to 0")

    # result = await send_ocr_request(file=image, language="tur")

    # async with aiofiles.open(filepath, 'wb') as f:
    #     while buffer := await image.read(1024):
    #         await f.write(buffer)

    #     await f.close()

    # filename = secure_filename(f"{str(uuid.uuid4())}_{image.filename}")
    # id = pymongo.save_file(filename, image, base="images")

    # Move file cursor to beginning
    # await image.seek(0)

    invoice_ocr_result = await InvoiceOcrResultInDB(
        firm=f"Okey: {datetime.datetime.now(tz=datetime.timezone.utc)}",
        no="021",
        date="22/05/2022",
        total_amount="72,5",
        total_kdv="2,5",
        image_id=image_id,
        products=[
            Product(
                name="yag",
                quantity=1,
                unit_price="70",
                ratio_kdv=8,
                category=ProductCategory.YIYECEK,
            )
        ],
    ).create()

    logger.info("Created Invoice Ocr Result")

    return invoice_ocr_result


@router.get("/invoice", response_model=list[InvoiceOcrResultInDB])
async def get_all_invoice_ocr_results():
    return await InvoiceOcrResultInDB.find_all().to_list()


@router.get("/invoice/{image_id}", response_model=InvoiceOcrResultInDB)
async def get_invoice_ocr_result(
    invoice_ocr_result: InvoiceOcrResultInDB = Depends(get_invoice_ocr_result),
):
    return invoice_ocr_result
