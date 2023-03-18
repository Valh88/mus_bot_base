from pydantic import BaseModel


class BaseBand(BaseModel):

    class Config:
        orm_mode = True


class BandPictureSchema(BaseBand):
    id: str
    path: str