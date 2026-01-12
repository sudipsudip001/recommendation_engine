from fastapi import APIRouter, Depends
from api.deps import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/me")
async def get_profile(user=Depends(get_current_user)):
    return user