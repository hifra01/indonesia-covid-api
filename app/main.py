from fastapi import FastAPI
from app.services.data_fetch import getTotalData

app = FastAPI()

@app.get("/")
async def root():
    data = await getTotalData()
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }
