from fastapi import APIRouter, HTTPException

from app.models import Receipt

router = APIRouter()

dummy_receipts = [
    {
        "id": "6102",
        "receipt_image_id": "61",
        "receipt_created_date": "24/01/2022",
        "firm": "Ozocr A.S.",
        "no": "0023",
        "date": "13/11/2021",
        "total_amount": "81,90",
        "total_kdv": "12,49",
        "products": [
            {
                "name": "Cay",
                "ratio_kdv": 8,
                "quantity": 2,
                "unit_price": "4,5",
                "category": "icecek",
            },
            {
                "name": "Makarna",
                "ratio_kdv": 18,
                "quantity": 3,
                "unit_price": "3",
                "category": "yiyecek",
            },
        ],
    },
    {
        "id": "6103",
        "receipt_image_id": "62",
        "receipt_created_date": "25/01/2022",
        "firm": "Kiskanc A.S.",
        "no": "0023",
        "date": "13/11/2021",
        "total_amount": "81,90",
        "total_kdv": "12,49",
        "products": [
            {
                "name": "Kola",
                "ratio_kdv": 8,
                "quantity": 2,
                "unit_price": "4,5",
                "category": "icecek",
            },
            {
                "name": "Et",
                "ratio_kdv": 18,
                "quantity": 3,
                "unit_price": "3",
                "category": "yiyecek",
            },
        ],
    },
]


@router.post("/")
async def create_receipt():
    return {"message": "Receipt created!"}


@router.get("/{receipt_id}", response_model=Receipt)
async def get_receipt(receipt_id: str):
    _receipt = None
    for dummy_receipt in dummy_receipts:
        if dummy_receipt["id"] == receipt_id:
            _receipt = dummy_receipt

    if _receipt is None:
        raise HTTPException(status_code=404, detail="Receipt with given id not found")

    return _receipt


@router.put("/{receipt_id}")
async def update_receipt(receipt_id: str):
    return {"message": "Receipt updated!"}


@router.delete("/{receipt_id}")
async def delete_receipt(receipt_id: str):
    return {"message": "Receipt deleted!"}


@router.get("/", response_model=list[Receipt])
async def get_all_receipts():
    return dummy_receipts
