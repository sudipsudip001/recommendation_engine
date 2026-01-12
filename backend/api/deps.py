from fastapi import Depends, HTTPException
from sqlmodel import Session

from core.security import decode_token
from db.session import get_session
from db.repositories.user_repository import UserRepository

def get_current_user(
    payload: dict = Depends(decode_token),
    session: Session = Depends(get_session),
):
    user_id = int(payload["sub"])
    user = UserRepository(session).get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

def get_admin_user(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user
