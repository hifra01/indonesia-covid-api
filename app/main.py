from fastapi import FastAPI
from app.routers import yearly
from app.services.data_fetch import fetch_total_data

app = FastAPI()

app.include_router(yearly.router)

@app.get("/")
async def root():
    data = await fetch_total_data()
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }
