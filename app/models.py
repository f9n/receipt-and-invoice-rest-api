from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    quantity: int
    unit_price: str
    ratio_kdv: int
    category: str


class Receipt(BaseModel):
    # id: str | None = Field(None, alias="_id")
    id: str
    receipt_image_id: str
    receipt_created_date: str
    firm: str
    no: str
    date: str
    total_amount: str
    total_kdv: str
    products: list[Product]
