from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_books():
    return {"message": "Here are your public books"}





