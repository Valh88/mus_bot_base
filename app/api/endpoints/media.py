import aiofiles
import uuid
from pathlib import Path
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import genres, bands
from app.schemas import genre as schema
from app.api import deps
from app.models import BandPicture
router = APIRouter()


@router.post('/band/{band_id}')
async def post_pictire_band(
    band_id: str,
    session: AsyncSession = Depends(deps.get_session),
    picture: UploadFile = File(...),
):
    picture.filename = str(uuid.uuid4()) + '_' + picture.filename
    path = str(uuid.uuid4()) + '_' + picture.filename
    # path = str(Path(__file__).parents[2]) + f'media/band/{picture.filename}'
    band = await bands.get_by_id(band_id=band_id, session=session)
    if band is None:
        raise HTTPException(status_code=404, detail="band not foud")
    async with aiofiles.open(f'media/band/{picture.filename}', "w+b") as buffer:
        picture = await picture.read()
        await buffer.write(picture)
    picture = BandPicture(path=f'media/band/{path}')
    session.add(picture), await session.commit()
    band.pictures.append(picture), 
    session.add(band), await session.commit()


@router.get('/{band_picture_id}', response_class=FileResponse)
async def get_bant_picture(
    band_picture_id: str,
    session: AsyncSession = Depends(deps.get_session),
):
    return f'media/band/{band_picture_id}'