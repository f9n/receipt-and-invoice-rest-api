import logging

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class CommonSettings(BaseSettings):
    APP_NAME: str = "Receipt N' Invoice OCR Rest API"
    DEBUG_MODE: bool = False


class Settings(CommonSettings):
    OCR_SERVICE_URL: str
    MONGODB_URL: str
    MONGODB_DB_NAME: str = "receipt-and-invoice"


settings = Settings()
