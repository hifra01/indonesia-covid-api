from fastapi import APIRouter
from app.services.data_fetch import fetch_yearly_data

router = APIRouter()

@router.get("/yearly", tags=["years"])
async def get_yearly_data():
    data = await fetch_yearly_data()
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }