from typing import Optional
from sqlmodel import Field
from db.base import SQLModel

class UserGenrePreference(SQLModel, table=True):
    __tablename__ = "user_genre_preferences"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)

    genre: str = Field(index=True)
    weight: float = Field(default=1.0)

