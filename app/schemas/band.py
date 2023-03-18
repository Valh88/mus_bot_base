from pydantic import BaseModel, validator
from typing import List, Dict, Optional
import datetime
from app.schemas.genre import GenreSchema


class BaseBand(BaseModel):

    class Config:
        orm_mode = True


class BandSchema(BaseBand):
    name: str
    contry_of_origin: str 
    location: str
    status: str
    formed_in: datetime.datetime
    description: str
    genres: List[str] = []
    themes: str


    @validator('status')
    def check_status(cls, status):
        if status in ('active', 'unactive'):
            return status
        raise ValueError("status must bee 'active' or 'unactive'")
    

class BandListSchema(BaseBand):
    id: str
    name: str
    contry_of_origin: str 
    location: str
    # status: Dict
    # genres: List[GenreSchema] = []
    pictures_url: List[str] = []
    themes: Optional[str] = None
    genres_str: List[str] = []


class BandFullSchema(BaseBand):
    name: str
    contry_of_origin: str 
    location: str
    # status: str
    pictures_url: List[str]
    formed_in: datetime.datetime
    description: str
    genres: List[GenreSchema] = []
    themes: Optional[str] = None