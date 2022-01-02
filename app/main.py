from fastapi import FastAPI
from app.routers import yearly, monthly, daily
from app.services.data_fetch import fetch_total_data

app = FastAPI()

app.include_router(yearly.router)
app.include_router(monthly.router)
app.include_router(daily.router)

@app.get("/")
async def root():
    data = await fetch_total_data()
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }
