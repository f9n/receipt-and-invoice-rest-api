import datetime
from pprint import pprint

from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from fastapi.logger import logger

from app.models import ImageInDB, ReceiptOcrResultInDB, InvoiceOcrResultInDB
from app.schemas import Product, ProductCategory
from app.dependencies import get_receipt_ocr_result, get_invoice_ocr_result
from app.services import get_product_categories, send_ocr_request, send_ocr_request2

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

    result = await send_ocr_request2(file=image.file)
    logger.info(result)

    receipt_products = []

    for receipt_p in result.get("products", []):
        receipt_p_name = receipt_p.get("name", "")
        receipt_p_category = receipt_p.get("category", ProductCategory.YIYECEK)
        # logger.info("ReceiptPCategory: ", receipt_p_category)
        # receipt_p_category_ml_result = await get_product_categories([receipt_p_name])
        # if len(receipt_p_category_ml_result) > 0:
        #     receipt_p_category = receipt_p_category_ml_result[0]

        logger.info("Receipt Product Category ML Result: ")
        logger.info(receipt_p_category)
        receipt_products.append(
            Product(
                name=receipt_p_name,
                quantity=receipt_p.get("quantity", 1),
                unit_price=receipt_p.get("unitPrice", ""),
                ratio_kdv=receipt_p.get("ratiokdv", ""),
                category=receipt_p_category,
            )
        )

    receipt_ocr_result = await ReceiptOcrResultInDB(
        firm=result.get("firm", ""),
        no=result.get("no", ""),
        date=result.get("date", ""),
        total_amount=result.get("total_amount", ""),
        total_kdv=result.get("total_kdv", ""),
        image_id=image_id,
        products=receipt_products,
    ).create()

    logger.info("Created Receipt Ocr Result")

    return receipt_ocr_result


@router.get("/receipt", response_model=list[ReceiptOcrResultInDB])
async def get_all_receipt_ocr_results():
    return await ReceiptOcrResultInDB.find_all().to_list()


@router.get("/receipt/{image_id}", response_model=ReceiptOcrResultInDB)
async def get_receipt_ocr_result_with_image_id(
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
async def get_invoice_ocr_result_with_image_id(
    invoice_ocr_result: InvoiceOcrResultInDB = Depends(get_invoice_ocr_result),
):
    return invoice_ocr_result
