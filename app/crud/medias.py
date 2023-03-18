from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models import Band, AssociationBandGenres, Genre, BandPicture
from app.schemas import band as schema
import datetime


async def get_image_by_id(
        session: AsyncSession,
        image_id: str,
) -> BandPicture:
    to_db = select(BandPicture).where(BandPicture.id == image_id)
    picture = await session.scalar(to_db)
    return picture