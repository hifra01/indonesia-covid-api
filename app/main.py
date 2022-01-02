from fastapi import FastAPI
from app.routers import root, yearly, monthly, daily

app = FastAPI()

app.include_router(root.router)
app.include_router(yearly.router)
app.include_router(monthly.router)
app.include_router(daily.router)
