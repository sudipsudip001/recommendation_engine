from typing import Optional
from sqlmodel import Field
from db.base import SQLModel

class UserAuthorPreference(SQLModel, table=True):
    __tablename__ = "user_author_preference"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)

    author_name: str = Field(index=True)
    weight: float = Field(default=1.0)

    