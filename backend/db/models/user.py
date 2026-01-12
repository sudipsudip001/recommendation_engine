from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    id: int
    email: str
    role: Literal["user", "admin"] = "user"


