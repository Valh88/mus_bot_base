from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models import Band, AssociationBandGenres, Genre, BandPicture, AlbumPicture
from app.schemas import band as schema
import datetime


async def get_image_by_id(
        session: AsyncSession,
        image_id: str,
) -> BandPicture:
    to_db = select(BandPicture).where(BandPicture.id == image_id)
    picture = await session.scalar(to_db)
    return picture


async def get_pictures_album_by_id(
        session: AsyncSession,
        album_id: str,
) -> List[AlbumPicture]:
    to_db = select(AlbumPicture).where(AlbumPicture.album_id == album_id)
    pictures = await session.execute(to_db)
    return pictures.scalars().all()


async def get_picture_album_by_id(
        session: AsyncSession,
        picture_id: str,
) -> AlbumPicture:
    to_db = select(AlbumPicture).where(AlbumPicture.id == picture_id)
    picture = await session.scalar(to_db)
    return picture
