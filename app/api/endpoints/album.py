from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.schemas import album as schema
from app.api import deps
from app.models import Album
from app.crud import albums

router = APIRouter()


@router.post('/album')
async def create_album(
    album: schema.AlbumCreateSchema,
    session: AsyncSession = Depends(deps.get_session),
):
    """Create band"""

    return await albums.create(album=album, session=session)


@router.get('/album/{album_id}', response_model=schema.AlbumFullSchema)
async def get_band_by_id(
    album_id: str,
    session: AsyncSession = Depends(deps.get_session),
):
    album = await albums.get_by_id(album_id=album_id, session=session)
    return album