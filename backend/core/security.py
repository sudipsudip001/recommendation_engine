from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

from db.models.user import User

load_dotenv()

secret_key = os.getenv("SECRET_KEY")
algo = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

#password helpers
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

#JWT helpers
def create_access_token(user: User) -> str:
    payload = {
        "sub": str(user.id),
        "role": user.role,
        "email": user.email,
        "exp": datetime.utcnow() + timedelta(hours=0.5)
    }
    return jwt.encode(payload, secret_key, algorithm=algo)

def decode_token(token: str = Depends(oauth2_scheme)) -> User:
    try:
        return jwt.decode(token, secret_key, algorithms=[algo])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

