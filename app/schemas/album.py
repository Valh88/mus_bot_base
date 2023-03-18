from pydantic import BaseModel, validator
from typing import List, Optional
from app.models import Album
import datetime

class BaseAlbum(BaseModel):

    class Config:
        orm_mode = True


class Song(BaseAlbum):
    name: str
    num_song: int 
    sound_time: float 
    # album_id: Mapped[str] = mapped_column(ForeignKey("albums.id"), nullable=False) 


class SongFull(Song):
    pass


class AlbumCreateSchema(BaseAlbum):
    name: str
    type_: str
    release_date: datetime.date
    catalog_id: str
    version_desc: str
    label: str 
    format: str
    limitation: int
    songs: Optional[List[Song]]
    band_id: str 

    @validator('format')
    def check_status(cls, format):
        if format in ('disc', 'cassette', 'vinil'):
            return format
        raise ValueError("format must bee 'disc' 'cassette' or 'vinil'")
    


class AlbumListSchema(BaseAlbum):
    name: str
    type_: str
    limitation: str


class AlbumFullSchema(BaseAlbum):
    name: str
    type_: str
    release_date: datetime.datetime
    catalog_id: str
    version_desc: str
    label: str 
    # format: str
    limitation: int
    songs: Optional[List[Song]] = []
    band_id: str 