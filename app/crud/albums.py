from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models import Band, AssociationBandGenres, Genre, Album, Track
from app.schemas import album as schema
import datetime


async def create(
        session: AsyncSession,
        album: schema.AlbumCreateSchema
) -> Album:
    traks = album.songs
    print(album.release_date)
    print(datetime.datetime.now())
    album = Album(
        name=album.name,
        type_=album.type_,
        release_date=album.release_date,
        catalog_id=album.catalog_id,
        version_desc=album.version_desc,
        label=album.label,
        format=album.format,
        limitation=album.limitation,
        # songs=album.songs
        band_id=album.band_id
        #commentary='3123123',
    )
    session.add(album), await session.commit()
    if len(traks) > 0:
        traks_list = [
            Track(
            name=track.name, 
            num_song=track.num_song, 
            sound_time=track.sound_time,
            album_id=album.id,
            ) for track in traks
        ]
        [session.add(obj) for obj in traks_list]
        await session.commit()            
    return album


async def get_by_id(
    session: AsyncSession,
    album_id: str,
)-> Album:
    to_db = select(Album).where(Album.id == album_id)
    album = await session.scalar(to_db)
    print(album)
    return album