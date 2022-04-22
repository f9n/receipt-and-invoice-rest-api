from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from beanie import PydanticObjectId

from app.models import ReceiptIn, ReceiptDB

router = APIRouter()


async def get_receipt(receipt_id: PydanticObjectId) -> ReceiptDB:
    receipt = await ReceiptDB.get(receipt_id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt


@router.post("/", response_model=ReceiptDB)
async def create_receipt(receipt: ReceiptIn):
    receipt_created_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = await ReceiptDB(
        **receipt.dict(), receipt_created_date=receipt_created_date
    ).create()
    return data


@router.get("/{receipt_id}", response_model=ReceiptDB)
async def get_receipt(receipt: ReceiptDB = Depends(get_receipt)):
    return receipt


@router.put("/{receipt_id}")
async def update_receipt(receipt: ReceiptDB = Depends(get_receipt)):
    return {"message": "@TODO: Receipt updated!"}


@router.delete("/{receipt_id}")
async def delete_receipt(receipt: ReceiptDB = Depends(get_receipt)):
    await receipt.delete()
    return {"message": "Receipt deleted!"}


@router.get("/", response_model=list[ReceiptDB])
async def get_all_receipts():
    return await ReceiptDB.find_all().to_list()
