from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.routers import root, yearly, monthly, daily

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(root.router)
app.include_router(yearly.router)
app.include_router(monthly.router)
app.include_router(daily.router)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        content={
            "ok": False,
            "message": exc.detail
        },
        status_code=exc.status_code
    )

@app.exception_handler(Exception)
async def server_exception_handler(request, exc):
    return JSONResponse(
        content={
            "ok": False,
            "message": "Internal Server Error"
        },
        status_code=500
    )
