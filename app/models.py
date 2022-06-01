from beanie import Document

from .schemas import ReceiptCreate, InvoiceCreate, Metadata, Image


class ReceiptInDB(Document, ReceiptCreate):
    metadata: Metadata = Metadata()

    class Collection:
        name = "receipts"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5eb7cf5a86d9755df3a6c593",
                "ImageId": "6161",
                "Firm": "Ozocr A.S.",
                "No": "003",
                "Date": "11/01/2021",
                "TotalAmount": "85,6",
                "TotalKdv": "5,6",
                "Metadata": {"CreatedAt": "22/04/2022 22:38:40", "CreatedBy": "null"},
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


class ReceiptOcrResultInDB(Document, ReceiptCreate):
    metadata: Metadata = Metadata()

    class Collection:
        name = "receipts-ocr-results"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5eb7cf5a86d9755df3a6c593",
                "ImageId": "6161",
                "Firm": "Ozocr A.S.",
                "No": "003",
                "Date": "11/01/2021",
                "TotalAmount": "85,6",
                "TotalKdv": "5,6",
                "Metadata": {"CreatedAt": "22/04/2022 22:38:40", "CreatedBy": "null"},
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


class InvoiceInDB(Document, InvoiceCreate):
    metadata: Metadata = Metadata()

    class Collection:
        name = "invoices"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5eb7cf5a86d9755df3a6c593",
                "ImageId": "6161",
                "Firm": "Ozocr A.S.",
                "No": "003",
                "Date": "11/01/2021",
                "TotalAmount": "85,6",
                "TotalKdv": "5,6",
                "Metadata": {"CreatedAt": "22/04/2022 22:38:40", "CreatedBy": "null"},
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


class InvoiceOcrResultInDB(Document, InvoiceCreate):
    metadata: Metadata = Metadata()

    class Collection:
        name = "invoices-ocr-results"

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5eb7cf5a86d9755df3a6c593",
                "ImageId": "6161",
                "Firm": "Ozocr A.S.",
                "No": "003",
                "Date": "11/01/2021",
                "TotalAmount": "85,6",
                "TotalKdv": "5,6",
                "Metadata": {"CreatedAt": "22/04/2022 22:38:40", "CreatedBy": "null"},
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


class ImageInDB(Document, Image):
    metadata: Metadata = Metadata()

    class Collection:
        name = "images"

    class Config:
        allow_population_by_field_name = True
