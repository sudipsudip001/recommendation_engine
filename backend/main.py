from fastapi import FastAPI
from api.router import api_router

app = FastAPI(title="Recommender engine")

app.include_router(api_router)



