from fastapi import HTTPException, status
from sqlmodel import Session

from core.security import(
    hash_password,
    verify_password,
    create_access_token
)
from db.models.user import User
from db.repositories.user_repository import UserRepository
from schemas.auth import TokenResponse

class AuthService:
    def __init__(self, session: Session):
        self.users = UserRepository(session)

    def register(self, email: str, password: str):
        if self.users.get_by_email(email):
            raise HTTPException(
                status_code=400,
                detail="Email already registered",
            )

        user = User(
            email=email,
            hashed_password=hash_password(password),
            role="admin" if email.endswith("@admin.com") else "user",
        )
        return self.users.create(user)

    def login(self, email: str, password: str) -> TokenResponse:
        user = self.users.get_by_email(email)

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        
        token = create_access_token(user)
        return TokenResponse(access_token=token)


