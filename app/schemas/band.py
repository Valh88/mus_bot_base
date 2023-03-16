from pydantic import BaseModel, validator
from typing import List, Optional, Union
import datetime


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
    genres: List[str]
    themes: str

    @validator('status')
    def check_status(cls, status):
        if status in ('active', 'unactive'):
            return status
        raise ValueError("status must bee 'active' or 'unactive'")