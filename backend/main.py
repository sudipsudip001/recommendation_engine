from fastapi import FastAPI
from api.router import api_router
from db.init_db import init_db
import contextlib

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 App startup")
    init_db()
    yield
    print("🛑 App shutdown")

app = FastAPI(
    title="Recommender engine",
    lifespan=lifespan
)

app.include_router(api_router)



