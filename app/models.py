import enum
import uuid

from pydantic import BaseModel, Field
from beanie import Document, PydanticObjectId

from .utils import to_camel


class ProductCategory(str, enum.Enum):
    GIYIM = "giyim"
    YIYECEK = "yiyecek"
    ICECEK = "icecek"
    ELEKTRONIK = "elektronik"
    KIRTASIYE = "kirtasiye"


class Product(BaseModel):
    name: str
    quantity: int
    unit_price: str
    ratio_kdv: int
    category: ProductCategory

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class ReceiptIn(BaseModel):
    image_id: str
    firm: str
    no: str
    date: str
    total_amount: str
    total_kdv: str
    products: list[Product]

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "ImageId": "6161",
                "Firm": "Ozocr A.S.",
                "No": "003",
                "Date": "11/01/2021",
                "TotalAmount": "85,6",
                "TotalKdv": "5,6",
                "Products": [
                    {
                        "Name": "cay",
                        "Quantity": 2,
                        "UnitPrice": "40",
                        "RatioKdv": 8,
                        "Category": "icecek",
                    }
                ],
            }
        }


class ReceiptDB(Document, ReceiptIn):
    receipt_created_date: str | None

    class Collection:
        name = "receipts"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5eb7cf5a86d9755df3a6c593",
                "ReceiptCreatedDate": "22/04/2022 22:38:40",
                "ImageId": "6161",
                "Firm": "Ozocr A.S.",
                "No": "003",
                "Date": "11/01/2021",
                "TotalAmount": "85,6",
                "TotalKdv": "5,6",
                "Products": [
                    {
                        "Name": "cay",
                        "Quantity": 2,
                        "UnitPrice": "40",
                        "RatioKdv": 8,
                        "Category": "icecek",
                    }
                ],
            }
        }
