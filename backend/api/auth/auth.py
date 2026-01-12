from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from db.session import get_session
from schemas.auth import TokenResponse
from services.auth_service import AuthService

router = APIRouter()

@router.post("/register")
def register(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    service = AuthService(session)
    return service.register(form_data.username, form_data.password)


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    service = AuthService(session)
    return service.login(form_data.username, form_data.password)


