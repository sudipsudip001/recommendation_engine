from fastapi import APIRouter

from api.public.books import router as books_router
from api.auth.auth import router as auth_router
from api.user.profile import router as user_router
from api.admin.admin import router as admin_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=["Auth"])
api_router.include_router(books_router, prefix="/books", tags=["Public"])
api_router.include_router(user_router, prefix="/user", tags=["User"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])


