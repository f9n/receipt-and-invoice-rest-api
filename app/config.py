import logging
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    app_name: str = "Receipt Invoice OCR Rest API"
    ocr_service_uri: str
    mongodb_uri: str


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
