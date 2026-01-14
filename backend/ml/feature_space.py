from typing import List

class FeatureSpace:
    def __init__(
        self,
        genres: List[str],
        authors: List[str],
        paces: List[str] = ["slow", "medium", "fast"],
        lengths: List[str] = ["short", "medium", "long"],
    ):
        self.genres = genres
        self.authors = authors
        self.paces = paces
        self.lengths = lengths
    
    def size(self) -> int:
        return (
            len(self.genres)
            + len(self.authors)
            + len(self.paces)
            + len(self.lengths)
            + 1
        )

