from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import TokenResponse
from services.auth_service import AuthService

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await AuthService.login_oauth(
        username=form_data.username,
        password=form_data.password,
    )


