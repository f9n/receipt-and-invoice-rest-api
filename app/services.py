import httpx

from app.core.config import settings


async def get_product_categories(products: list[str]):

    data = {"texts": [products]}
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{settings.PRODUCT_TEXT_CLASSIFICATION_URL}/classification", data=data
        )
        return r.json()
