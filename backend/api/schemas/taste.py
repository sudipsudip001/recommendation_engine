from typing import List, Optional
from pydantic import BaseModel, Field

class TasteSurveyCreate(BaseModel):
    preferred_pace: Optional[str] = Field(
        None, example="fast"
    )
    preferred_length: Optional[str] = Field(
        None, example="long"
    )
    likes_series: Optional[bool] = None

    favorite_genres: List[str] = Field(
        default_factory=list,
        example=["fantasy", "sci-fi"]
    )

    favorite_authors: List[str] = Field(
        default_factory=list,
        example=["Brandon Sanderson"]
    )

class TasteSurveyResponse(BaseModel):
    preferred_pace: Optional[str]
    preferred_length: Optional[str]
    likes_series: Optional[bool]
    favorite_genres: List[str]
    favorite_authors: List[str]



