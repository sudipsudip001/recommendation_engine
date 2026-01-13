from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field
from db.base import SQLModel

class UserBookInteraction(SQLModel, table=True):
    __tablename__ = "user_book_interactions"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", index=True)

    book_id: int = Field(index=True)
    interaction_type: str
    value: Optional[float] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

