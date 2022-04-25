import logging
import datetime

from fastapi import APIRouter, HTTPException, UploadFile, File, Depends

from app.models import ReceiptOcrResultInDb
from app.schemas import Product, ProductCategory
from app.dependencies import get_receipt_ocr_result

router = APIRouter()


@router.post("/receipt")
async def ocr_result_from_receipt_image(image: UploadFile = File(...)):
    print(f"Filename: {image.filename}")
    print(f"Filename Content Type: {image.content_type}")

    if image.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
        raise HTTPException(
            status_code=405, detail="Allowed image files are in PNG or JPG format"
        )

    # async with aiofiles.open(filepath, 'wb') as f:
    #     while buffer := await image.read(1024):
    #         await f.write(buffer)

    #     await f.close()

    # filename = secure_filename(f"{str(uuid.uuid4())}_{image.filename}")
    # id = pymongo.save_file(filename, image, base="images")

    # Move file cursor to beginning
    # await image.seek(0)

    receipt_ocr_result = await ReceiptOcrResultInDb(
        firm=f"Okey: {datetime.datetime.now(tz=datetime.timezone.utc)}",
        no="021",
        date="22/05/2022",
        total_amount="72,5",
        total_kdv="2,5",
        image_id="616161",
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

    return receipt_ocr_result


@router.get("/receipt")
async def get_all_receipt_ocr_results():
    return await ReceiptOcrResultInDb.find_all().to_list()


@router.get("/receipt/{image_id}")
async def get_receipt_ocr_result(
    receipt_ocr_result: ReceiptOcrResultInDb = Depends(get_receipt_ocr_result),
):
    return receipt_ocr_result


# return pymongo.send_file(filename, base="images")
# @router.get("/download_csv_use_IO")
# def download_csv_use_IO():
#     csv_data = [
#         ['name', 'sex', 'birthday'],
#         ['user', 'boy', '2019-01-01'],
#         ['张三', '里斯', '2019-01-01']
#     ]
#     # 创建一个 io 流
#     io_stream = io.StringIO()
#     writer = csv.writer(io_stream)
#     for row in csv_data:
#         writer.writerow(row)
#     mem = io.BytesIO()
#     mem.write(io_stream.getvalue().encode('utf-8'))
#     # Change stream position
#     mem.seek(0)
#     io_stream.close()
#     return StreamingResponse(
#         mem, media_type="text/csv",
#         headers={
#             'content-disposition': "attachment; filename*=utf-8''{}".format(
#                 quote("测试.csv"))
#     })


@router.post("/invoice")
async def ocr_result_from_invoice_image(image: UploadFile = File(...)):
    return {"message": "Get image and Send image_id field to you"}


@router.get("/invoice")
async def get_all_invoice_ocr_results():
    return {"message": "Send all invoice ocr result"}


@router.get("/invoice/{image_id}")
async def get_invoice_ocr_result():
    return {"message": "Send invoice ocr result"}
