from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    username: Optional[str] = None
    email: str
