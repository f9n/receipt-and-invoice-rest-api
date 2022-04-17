from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from config import settings

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def index():
  return RedirectResponse("/docs")

@app.get("/ping")
async def pong():
  return {"ping": "pong!"}

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
  '''
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
  '''
  return {'healthcheck': 'Everything OK!'}

@app.get("/api/v1/config")
async def get_config():
  return {
    "product": {
      "categories": [
        "giyim",
        "icecek",
        "yiyecek",
        "teknoloji",
        "kirtasiye"
      ]
    }
  }

@app.post("/api/v1/ocr/receipt")
async def ocr_from_receipt():
  return {"message": "Get image and Send image_id field to you"}

@app.get("/api/v1/ocr/receipt/{image_id}")
async def get_receipt_ocr_result():
  return {"message": "Send receipt ocr result"}

@app.post("/api/v1/receipts")
async def create_receipt():
  return {"message": "Receipt created!"}

@app.get("/api/v1/receipts/{receipt_id}")
async def get_receipt(receipt_id: str):
  return {"message": "Receipt getted!"}

@app.put("/api/v1/receipts/{receipt_id}")
async def update_receipt(receipt_id: str):
  return {"message": "Receipt updated!"}

@app.delete("/api/v1/receipts/{receipt_id}")
async def update_receipt(receipt_id: str):
  return {"message": "Receipt deleted!"}

@app.get("/api/v1/receipts")
async def get_all_receipts():
  dummy_receipts = [
    {
      "id": "6102",
      "image_id": "61",
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
      "image_id": "62",
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

  return dummy_receipts
