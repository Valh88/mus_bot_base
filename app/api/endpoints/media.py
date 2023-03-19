import aiofiles
import uuid
from pathlib import Path
from pathlib import Path
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import bands, medias, albums
from app.schemas import media as schema
from app.api import deps
from app.models import BandPicture, AlbumPicture
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
    picture = BandPicture(path=path)
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
    if picture is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="picture not found in db")  
    path = Path(picture.path)
    # print(FileResponse(picture.path))
    if path.is_file():
        return picture.path
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="pick not found")


@router.post('/image/album/{album_id}', response_model=schema.AlbumPictureSchema)
async def post_picture_album(
    album_id: str,
    picture: UploadFile = File(...),
    session: AsyncSession = Depends(deps.get_session),
):  
    album = await albums.get_by_id(session=session, album_id=album_id)
    if album is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="album not found")
    
    path = str(uuid.uuid4()) + '_' + picture.filename
    # path = str(Path(__file__).parents[2]) + f'media/band/{picture.filename}'
    async with aiofiles.open(f'media/album/{path}', "w+b") as buffer:
        picture = await picture.read()
        await buffer.write(picture)
    picture = AlbumPicture(
        path=path,
        album_id=album.id
    )
    session.add(picture), await session.commit()
    return picture


@router.get('/album/{album_id}', response_model=List[schema.AlbumPictureSchema])
async def get_all_picture_album_id(
    album_id: str,
    session: AsyncSession = Depends(deps.get_session),
) -> List[schema.AlbumPictureSchema]:
    album = await albums.get_by_id(session=session, album_id=album_id)
    if album is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="album not found") 
    return await medias.get_pictures_album_by_id(session=session, album_id=album.id)


@router.get('/album/id/{picture_id}', response_class=FileResponse)
async def get_picture_album_by_id(
    picture_id: str,
    session: AsyncSession = Depends(deps.get_session),
):
    picture = await medias.get_picture_album_by_id(
        session=session,
        picture_id=picture_id,
    )
    if picture is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="picture not found in db")  
    if not Path(f'media/album/{picture.path}').is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="picture not found on disk")  

    return f'media/album/{picture.path}' 
