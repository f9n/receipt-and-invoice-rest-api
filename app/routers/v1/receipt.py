from datetime import datetime

from fastapi import APIRouter, Depends, Body

from app.models import ReceiptInDB
from app.schemas import ReceiptCreate, ReceiptUpdate

from app.dependencies import get_receipt

router = APIRouter()


@router.post("/", response_model=ReceiptInDB)
async def create_receipt(receipt: ReceiptCreate):
    # receipt_created_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = await ReceiptInDB(
        **receipt.dict(),
        # receipt_created_date=receipt_created_date
    ).create()
    return data


@router.get("/{receipt_id}", response_model=ReceiptInDB)
async def get_receipt(receipt: ReceiptInDB = Depends(get_receipt)):
    return receipt


@router.put("/{receipt_id}", response_model=ReceiptInDB)
async def update_receipt(
    receipt_update: ReceiptUpdate = Body(...),
    receipt: ReceiptInDB = Depends(get_receipt),
):
    receipt = receipt.copy(update=receipt_update.dict(exclude_unset=True))
    await receipt.save()
    return receipt


@router.delete("/{receipt_id}")
async def delete_receipt(receipt: ReceiptInDB = Depends(get_receipt)):
    await receipt.delete()
    return {"message": "Receipt deleted!"}


@router.get("/", response_model=list[ReceiptInDB])
async def get_all_receipts():
    return await ReceiptInDB.find_all().to_list()
