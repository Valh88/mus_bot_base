import aiofiles
import uuid
from pathlib import Path
from pathlib import Path
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import genres, bands, medias
from app.schemas import media as schema
from app.api import deps
from app.models import BandPicture
router = APIRouter()


@router.post('/band/{band_id}', response_model=schema.BandPictureSchema)
async def post_pictire_band(
    band_id: str,
    session: AsyncSession = Depends(deps.get_session),
    picture: UploadFile = File(...),
) -> schema.BandPictureSchema:
    path = str(uuid.uuid4()) + '_' + picture.filename
    # path = str(Path(__file__).parents[2]) + f'media/band/{picture.filename}'
    band = await bands.get_by_id(band_id=band_id, session=session)
    if band is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="band not found")
    async with aiofiles.open(f'media/band/{path}', "w+b") as buffer:
        picture = await picture.read()
        await buffer.write(picture)
    picture = BandPicture(path=f'media/band/{path}')
    session.add(picture), await session.commit()
    band.pictures.append(picture), 
    session.add(band), await session.commit()
    return picture


@router.get('/{band_picture_name}', response_class=FileResponse)
async def get_bant_picture_by_name(
    band_picture_name: str,
    session: AsyncSession = Depends(deps.get_session),
):  
    path = Path(f'media/band/{band_picture_name}')
    if path.is_file():
        return f'media/band/{band_picture_name}'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pick not found")

@router.get('/image/{image_id}', response_class=FileResponse)
async def get_bant_picture_by_id(
    image_id: str,
    session: AsyncSession = Depends(deps.get_session),
) -> FileResponse:  
    picture = await medias.get_image_by_id(session=session, image_id=image_id)
    path = Path(picture.path)
    # print(FileResponse(picture.path))
    if path.is_file():
        return picture.path
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pick not found")