from fastapi import Depends, HTTPException, status
from core.security import decode_token
from db.models.user import User

async def get_current_user(token: str = Depends(decode_token)) -> User:
    if not token:
        raise HTTPException(status_code=401, detail="Not Authenticated")
    return token

async def get_admin_user(
    current_user: User = Depends(get_current_user)
) -> User:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privilege required",
        )
    return current_user

