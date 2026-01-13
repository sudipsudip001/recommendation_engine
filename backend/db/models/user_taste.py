from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field
from db.base import SQLModel

class UserTasteProfile(SQLModel, table=True):
    __tablename__ = "user_taste_profiles"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)

    preferred_place: Optional[str] = None
    preferred_length: Optional[str] = None
    likes_series: Optional[bool] = None

    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc))

