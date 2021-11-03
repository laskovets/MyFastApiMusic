from pydantic import BaseModel
from typing import Sequence


class TrackBase(BaseModel):
    name: str
    listeners: int
    playcounts: int
