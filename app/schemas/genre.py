from pydantic import BaseModel, validator
from typing import List, Optional, Union
import datetime

class BaseGenre(BaseModel):

    class Config:
        orm_mode = True


class GenreSchema(BaseGenre):
    genre: str


class GenreResponseSchema(BaseGenre):
    id: str
    genre: str