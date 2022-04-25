import logging
import sys

import beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError

from app.core.config import settings
from app.models import ReceiptInDB, ReceiptOcrResultInDb, Image


class Database:
    motor_client: AsyncIOMotorClient = None


db = Database()


def get_database() -> AsyncIOMotorClient:
    return db.motor_client


async def connect():
    logging.info("Connecting to Mongo...")
    db.motor_client = AsyncIOMotorClient(settings.MONGO_URL)
    try:
        db.motor_client.server_info()
    except ServerSelectionTimeoutError:
        sys.exit("Cannot connect the mongodb server")

    logging.info("Connected.")
    await beanie.init_beanie(
        database=db.motor_client[settings.MONGO_DB],
        document_models=[ReceiptInDB, ReceiptOcrResultInDb, Image],
    )


async def disconnect():
    logging.info("Closing Mongo connection...")
    db.motor_client.close()
    logging.info("Connection closed.")
