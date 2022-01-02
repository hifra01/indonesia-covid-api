from fastapi import APIRouter
from app.services.data_fetch import fetch_total_data

router = APIRouter()

@router.get("/")
async def root():
    data = await fetch_total_data()
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }