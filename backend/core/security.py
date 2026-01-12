from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
from dotenv import load_dotenv

from db.models.user import User

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algo = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(user: User) -> str:
    payload = {
        "sub": user.email,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(hours=0.5)
    }
    return jwt.encode(payload, secret_key, algorithm=algo)

def decode_token(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algo])
        return User(
            id=1,
            email=payload["sub"],
            role=payload["role"],
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )




