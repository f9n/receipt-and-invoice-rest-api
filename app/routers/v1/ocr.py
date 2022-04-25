import logging

from fastapi import APIRouter, HTTPException, UploadFile, File

from app.database import ReceiptInDB
from app.schemas import Product, ProductCategory

router = APIRouter()


@router.post("/receipt")
async def ocr_from_receipt(image: UploadFile = File(...)):
    print(f"Filename: {image.filename}")
    print(f"Filename Content Type: {image.content_type}")

    if image.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
        raise HTTPException(
            status_code=405, detail="Allowed image files are in PNG or JPG format"
        )

    # filename = secure_filename(f"{str(uuid.uuid4())}_{image.filename}")
    # id = pymongo.save_file(filename, image, base="images")

    # Move file cursor to beginning
    # image.seek(0)

    receipt = ReceiptInDB(
        firm="Okey",
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
    )
    return receipt


@router.get("/receipt/{image_id}")
async def get_receipt_ocr_result():
    return {"message": "Send receipt ocr result"}
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
async def ocr_from_invoice():
    return {"message": "Get image and Send image_id field to you"}


@router.get("/invoice/{image_id}")
async def get_invoice_ocr_result():
    return {"message": "Send invoice ocr result"}
