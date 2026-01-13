from typing import Optional
from sqlmodel import Field
from db.base import SQLModel

class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str = Field(index=True)
    genre: str = Field(index=True)

    pace: Optional[str] = None
    length: Optional[str] = None
    
