from datetime import datetime

from fastapi import APIRouter, Depends, Body
from fastapi.logger import logger

from app.models import InvoiceInDB
from app.schemas import InvoiceCreate, InvoiceUpdate
from app.dependencies import get_invoice

router = APIRouter()


@router.post("/", response_model=InvoiceInDB)
async def create_invoice(invoice: InvoiceCreate):
    # invoice_created_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = await InvoiceInDB(
        **invoice.dict(),
        # invoice_created_date=invoice_created_date
    ).create()
    return data


@router.get("/{invoice_id}", response_model=InvoiceInDB)
async def get_invoice(invoice: InvoiceInDB = Depends(get_invoice)):
    return invoice


@router.put("/{invoice_id}", response_model=InvoiceInDB)
async def update_invoice(
    invoice_update: InvoiceUpdate = Body(...),
    invoice: InvoiceInDB = Depends(get_invoice),
):
    invoice = invoice.copy(update=invoice_update.dict(exclude_unset=True))
    await invoice.save()
    return invoice


@router.delete("/{invoice_id}")
async def delete_invoice(invoice: InvoiceInDB = Depends(get_invoice)):
    await invoice.delete()
    return {"message": "Invoice deleted!"}


@router.get("/", response_model=list[InvoiceInDB])
async def get_all_invoices():
    logger.info("Get All invoices")
    return await InvoiceInDB.find_all().to_list()
