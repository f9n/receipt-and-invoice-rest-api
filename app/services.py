import json

import httpx

from app.core.config import settings


async def get_product_categories(products: list[str]):
    data = {"texts": [products]}
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{settings.PRODUCT_TEXT_CLASSIFICATION_URL}/classification", data=data
        )
        return r.json()


async def send_ocr_request(file, language="eng"):
    files = {"file": file}
    options_dict = dict(languages=[language])
    # 'options': '{"languages": ["eng"]}'
    payload = {"options": json.dumps(options_dict)}
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{settings.OCR_SERVICE_URL}", data=payload, files=files)
        return r.json()

async def send_ocr_request2(file):
    files = {"uploadedImage": file}
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{settings.OCR_SERVICE_URL}/api/upload", files=files)
        return r.json()
