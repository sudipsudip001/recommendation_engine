from schemas.auth import LoginRequest, TokenResponse
from core.security import create_access_token
from db.models.user import User

class AuthService:
    @staticmethod
    async def login(data: LoginRequest) -> TokenResponse:
        if data.password != "password":
            raise ValueError("Invalid credentials")
        
        role = "admin" if data.email.endswith("@admin.com") else "user"

        user = User(
            id=1,
            email=data.email,
            role=role,
        )

        token = create_access_token(user)

        return TokenResponse(access_token=token)

    @staticmethod
    async def register(data):
        return {"message": f"User registered (placeholder)"}

    @staticmethod
    async def login_oauth(username: str, password: str) -> TokenResponse:
        if password != "password":
            raise ValueError("Invalid credentials")

        role = "admin" if username.endswith("@admin.com") else "user"

        user = User(
            id=1,
            email=username,  # username == email
            role=role,
        )

        token = create_access_token(user)

        return TokenResponse(access_token=token)
    

    