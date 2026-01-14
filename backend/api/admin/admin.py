from fastapi import APIRouter, Depends
from api.deps import get_admin_user

router = APIRouter(dependencies=[Depends(get_admin_user)])

@router.get("/train_model")
async def train_model():
    return {"status": "training started"}

