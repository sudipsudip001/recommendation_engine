from db.models.book import Book
from ml.feature_space import FeatureSpace

def build_book_feature_vector(
    *,
    book: Book,
    feature_space: FeatureSpace,
) -> list[float]:
    vector = []

    for genre in feature_space.genres:
        vector.append(1.0 if book.genre == genre else 0.0)
    
    for author in feature_space.authors:
        vector.append(1.0 if book.author == author else 0.0)

    for pace in feature_space.paces:
        vector.append(1.0 if book.pace == pace else 0.0)
    
    for length in feature_space.lengths:
        vector.append(1.0 if book.length == length else 0.0)
    
    vector.append(0.0)

    return vector

