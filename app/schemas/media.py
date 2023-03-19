from pydantic import BaseModel


class BasePicture(BaseModel):

    class Config:
        orm_mode = True


class BandPictureSchema(BasePicture):
    id: str
    path: str


class AlbumPictureSchema(BasePicture):
    id: str
    # path: str
    # album_id: str