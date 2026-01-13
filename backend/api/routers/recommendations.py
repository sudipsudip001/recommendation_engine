from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.deps import get_current_user
from db.session import get_session
from api.services.recommender_service import recommend_books_for_user

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)

@router.get("/")
def get_recommendations(
    session: Session = Depends(get_session),
    user = Depends(get_current_user),
):
    books = recommend_books_for_user(
        session=session,
        user_id=user.id,
    )

    return [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "genre": b.genre,
        }
        for b in books
    ]

