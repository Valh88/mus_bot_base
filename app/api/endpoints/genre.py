from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import genres
from app.schemas import genre as schema
from app.api import deps

router = APIRouter()

@router.post('/genre', response_model=schema.GenreResponseSchema)
async def create_genre(
    genre: schema.GenreSchema,
    session: AsyncSession = Depends(deps.get_session),
) -> schema.GenreResponseSchema:
    genre = await genres.create(session=session, genre=genre)
    return genre


@router.get('/genre', response_model=List[schema.GenreResponseSchema])
async def get_all_genre(
    session: AsyncSession = Depends(deps.get_session),
) -> List[schema.GenreResponseSchema]:
    return await genres.get(session=session)
   