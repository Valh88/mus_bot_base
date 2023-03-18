from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models import Band, AssociationBandGenres, Genre
from app.schemas import band as schema
import datetime


async def create(
        session: AsyncSession,
        band: schema.BandSchema
) -> Band:
    genres = band.genres
    band = Band(
        name=band.name,
        contry_of_origin=band.contry_of_origin,
        location=band.location,
        status=band.status,
        formed_in=datetime.datetime.now(),
        description=band.description,
        themes=band.themes
        # commentary='3123123',
    )
    session.add(band), await session.commit()
    if len(genres) > 0:
        asociation_obj_list = [
            AssociationBandGenres(band_id=band.id, genre_id=genres_id) for genres_id in genres
        ]
        [session.add(obj) for obj in asociation_obj_list]
        await session.commit()            
    return band


async def get_by_id(
        session: AsyncSession,
        band_id: str, 
) -> Band:
    to_db = select(Band).options(selectinload(Band.genres)).where(Band.id == band_id)
    band = await session.scalar(to_db)
    return band


async def get_all_bands(
        session: AsyncSession,
) -> List[Band]:
    band_list = await session.execute(
        select(Band)
        # .options(selectinload(Band.genres))
    )
    return band_list.scalars().all()
