import time

from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import motor
import beanie

from app.core.config import settings
from app.models import ReceiptDB
from app.routers import v1
from . import __version__

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG_MODE, version=__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"request processed in {process_time} s")
    return response


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")


@app.get("/ping")
async def pong():
    return {
        "ping": "pong!",
        "ocr_service_url": settings.OCR_SERVICE_URL,
    }


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """
    Simple route for the GitHub Actions to healthcheck on.

    More info is available at:
    https://github.com/akhileshns/heroku-deploy#health-check

    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code just enables
    the GitHub Actions to rollback to the last version the project was
    found in a "working condition". It acts as a last line of defense in
    case something goes south.

    Additionally, it also returns a JSON response in the form of:

    {
      'healtcheck': 'Everything OK!'
    }
    """
    return {"healthcheck": "Everything OK!"}


@app.on_event("startup")
async def app_init():
    app.mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)

    await beanie.init_beanie(
        database=app.mongodb_client[settings.MONGODB_DB_NAME],
        document_models=[ReceiptDB],
    )

    app.include_router(v1.router, prefix="/api/v1")


@app.on_event("shutdown")
async def app_shutdown():
    app.mongodb_client.close()
