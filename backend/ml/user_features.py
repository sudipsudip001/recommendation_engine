from sqlmodel import Session, select
from db.models.user_taste import UserTasteProfile
from db.models.user_genre_preference import UserGenrePreference
from db.models.user_author_preference import UserAuthorPreference
from ml.feature_space import FeatureSpace

def build_user_feature_vector(
    *,
    session: Session,
    user_id: int,
    feature_space: FeatureSpace,
) -> list[float]:
    vector = []

    profile = session.exec(
        select(UserTasteProfile)
        .where(UserTasteProfile.user_id == user_id)
    ).first()

    genre_prefs = session.exec(
        select(UserGenrePreference)
        .where(UserGenrePreference.user_id == user_id)
    ).all()

    author_prefs = session.exec(
        select(UserAuthorPreference)
        .where(UserAuthorPreference.user_id == user_id)
    ).all()

    genre_weights = {g.genre: g.weight for g in genre_prefs}
    author_weights = {a.author_name: a.weight for a in author_prefs}

    for genre in feature_space.genres:
        vector.append(genre_weights.get(genre, 0.0))

    for author in feature_space.authors:
        vector.append(author_weights.get(author, 0.0))
    
    for pace in feature_space.paces:
        vector.append(1.0 if profile and profile.preferred_pace == pace else 0.0)
    
    for length in feature_space.lengths:
        vector.append(1.0 if profile and profile.preferred_length == length else 0.0)
    
    vector.append(1.0 if profile and profile.likes_series else 0.0)

    return vector


