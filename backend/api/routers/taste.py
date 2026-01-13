from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from api.schemas.taste import (
    TasteSurveyCreate,
    TasteSurveyResponse,
)
from api.services.taste_service import upsert_user_taste
from api.deps import get_current_user
from db.session import get_session
from db.models.user_taste import UserTasteProfile
from db.models.user_genre_preference import UserGenrePreference
from db.models.user_author_preference import UserAuthorPreference

router = APIRouter(
    prefix="/taste",
    tags=["Taste Profile"],
)

@router.post("/", response_model=None)
def submit_taste_survey(
    data: TasteSurveyCreate,
    session: Session = Depends(get_session),
    user=Depends(get_current_user),
):
    upsert_user_taste(
        session=session,
        user_id=user.id,
        data=data,
    )
    return {"status": "taste profile saved"}


@router.get("/", response_model=TasteSurveyResponse)
def get_my_taste(
    session: Session = Depends(get_session),
    user=Depends(get_current_user),
):
    profile = session.exec(
        select(UserTasteProfile)
        .where(UserTasteProfile.user_id == user.id)
    ).first()

    if profile is None:
        return TasteSurveyResponse(
            preferred_pace=None,
            preferred_length=None,
            likes_series=None,
            favorite_genres=[],
            favorite_authors=[],
        )

    genres = session.exec(
        select(UserGenrePreference.genre)
        .where(UserGenrePreference.user_id == user.id)
    ).all()

    authors = session.exec(
        select(UserAuthorPreference.author_name)
        .where(UserAuthorPreference.user_id == user.id)
    ).all()

    return TasteSurveyResponse(
        preferred_pace=profile.preferred_pace,
        preferred_length=profile.preferred_length,
        likes_series=profile.likes_series,
        favorite_genres=genres,
        favorite_authors=authors,
    )

