from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from app.models import Genre
from app.schemas import genre as schema


async def create(
        session: AsyncSession,
        genre: schema.GenreSchema
) -> Genre:  
    genre = Genre(genre=genre.genre)
    session.add(genre), await session.commit()
    return genre


async def get(
        session: AsyncSession,
) -> List[Genre]:  
    genress_list = await session.execute(select(Genre))
    return genress_list.scalars().all()


async def get_by_id(
        session: AsyncSession,
        genre_id: str
) -> Genre:
    to_db = select(Genre).where(Genre.id == genre_id)
    genre = await session.scalar(to_db)
    return genre
