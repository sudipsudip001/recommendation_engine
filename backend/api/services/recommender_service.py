from sqlmodel import Session, select
from db.models.book import Book
from db.models.user_genre_preference import UserGenrePreference
from db.models.user_author_preference import UserAuthorPreference

def recommend_books_for_user(
    *,
    session: Session,
    user_id: int,
    limit: int = 10,
):
    books = session.exec(select(Book)).all()

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

    scored = []

    for book in books:
        score = 0.0

        if book.genre in genre_weights:
            score += genre_weights[book.genre] * 2.0
        
        if book.author in author_weights:
            score += author_weights[book.author] * 3.0
        
        scored.append((score, book))
    
    scored.sort(key=lambda x: x[0], reverse=True)

    return [book for score, book in scored[:limit] if score > 0]

