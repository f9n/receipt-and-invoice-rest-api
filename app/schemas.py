import enum

from pydantic import BaseModel

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


class Receipt(BaseModel):
    firm: str
    no: str
    date: str
    total_amount: str
    total_kdv: str
    products: list[Product]


class ReceiptCreate(Receipt):
    image_id: str

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


class ReceiptUpdate(BaseModel):
    firm: str | None = None
    no: str | None = None
    date: str | None = None
    total_amount: str | None = None
    total_kdv: str | None = None
    products: list[Product] | None = None

    class Config:
        allow_population_by_field_name = True