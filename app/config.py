import logging

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    app_name: str = "Receipt Invoice OCR Rest API"
    ocr_service_uri: str = (
        "https://tesseract-4-all-langs-example.herokuapp.com/tesseract"
    )
    mongodb_uri: str = "mongodb+srv://root:0VnUxSMny1oOKMHR@impala.zrlzu.mongodb.net/receipt_and_invoice_db?retryWrites=true&w=majority"

def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
