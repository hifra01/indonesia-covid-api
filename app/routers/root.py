from fastapi import APIRouter
from app.services.root_services import fetch_total_and_update

router = APIRouter()

@router.get("/")
async def root():
    data = await fetch_total_and_update()
    return {
        "ok": True,
        "message": "Data fetched successfully",
        "data": data
    }