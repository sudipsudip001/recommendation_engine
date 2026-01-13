from sqlmodel import Session, select, delete
from db.models.user_taste import UserTasteProfile
from db.models.user_genre_preference import UserGenrePreference
from db.models.user_author_preference import UserAuthorPreference

def upsert_user_taste(
    *,
    session: Session,
    user_id: int,
    data,
):
    profile = session.exec(
        select(UserTasteProfile)
        .where(UserTasteProfile.user_id == user_id)
    ).first()

    if profile is None:
        profile = UserTasteProfile(
            user_id=user_id,
            preferred_pace=data.preferred_pace,
            preferred_length=data.preferred_length,
            likes_series=data.likes_series,
        )
        session.add(profile)
    else:
        profile.preferred_pace = data.preferred_pace
        profile.preferred_length = data.preferred_length
        profile.likes_series = data.likes_series

    # Clear existing preferences
    session.exec(
        delete(UserGenrePreference).where(UserGenrePreference.user_id == user_id)
    )

    session.exec(
        delete(UserAuthorPreference).where(UserAuthorPreference.user_id == user_id)
    )

    # Insert new preferences
    for genre in data.favorite_genres:
        session.add(
            UserGenrePreference(
                user_id=user_id,
                genre=genre,
                weight=1.0
            )
        )

    for author in data.favorite_authors:
        session.add(
            UserAuthorPreference(
                user_id=user_id,
                author_name=author,
                weight=1.0
            )
        )

    session.commit()

