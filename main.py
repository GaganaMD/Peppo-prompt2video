from fastapi import FastAPI
from backend.app.api import router

app = FastAPI()

# include API router
app.include_router(router)
