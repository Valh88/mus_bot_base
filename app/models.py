"""
SQL Alchemy models declaration.
https://docs.sqlalchemy.org/en/14/orm/declarative_styles.html#example-two-dataclasses-with-declarative-table
Dataclass style for powerful autocompletion support.

https://alembic.sqlalchemy.org/en/latest/tutorial.html
Note, it is used by alembic migrations logic, see `alembic/env.py`

Alembic shortcuts:
# create migration
alembic revision --autogenerate -m "migration_name"

# apply all migrations
alembic upgrade head
"""
import uuid
from typing import List
import datetime
from sqlalchemy import String, Integer, ForeignKey, Table, Column, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_utils import ChoiceType


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_model"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(
        String(254), nullable=False, unique=True, index=True
    )
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)


class Band(Base):
    __tablename__ = "bands"

    STATUS = [
        ('active', 'active'),
        ('unactive', 'unactive'),
    ]

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    contry_of_origin: Mapped[str] = mapped_column(String(30), nullable=False)
    location: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[ChoiceType] = mapped_column(ChoiceType(STATUS))
    formed_in: Mapped[datetime.datetime]
    description: Mapped[str] = mapped_column(String(800), nullable=True)
    # # ears_active: Mapped[str]
    genres: Mapped[List['Genre']] = relationship(
        secondary='association_table_band_genres', back_populates='bands', lazy="selectin"
    )
    # genre_associations: Mapped[List['AssociationBandGenres']] = relationship(back_populates='band')
    discography: Mapped[List['Album']] = relationship(
        'Album', back_populates='band', cascade='delete, all'
    )
    themes: Mapped[str] = mapped_column(String(100), nullable=True)
    pictures: Mapped[List['BandPicture']] = relationship(
        secondary='association_band_pictures', back_populates='bands', lazy="selectin"
    )
    # picture_associations: Mapped[List['AssociationBandPicture']] = relationship(back_populates='band')
    commentary: Mapped[str] = mapped_column(String(300), nullable=True)

    @property
    def genres_str(self):
        url_list = []
        [url_list.append(genre.genre) for genre in self.genres]
        return url_list
    
    @property
    def pictures_url(self):
        url_list = []
        [url_list.append(picture.path) for picture in self.pictures]
        return url_list  
            
class Album(Base):
    __tablename__ = 'albums'

    FORMAT = [
        ('cassette', 'cassete'),
        ('disc', 'disc'),
        ('vinil', 'vinil'),
    ]

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type_: Mapped[str] = mapped_column(String(10), nullable=False)
    release_date = Mapped[datetime.datetime]
    catalog_id: Mapped[str] = mapped_column(String(30))
    version_desc = Mapped[str]
    label: Mapped[str] = mapped_column(String(30))
    format: Mapped[ChoiceType] = mapped_column(ChoiceType(FORMAT))
    limitation: Mapped[int] = mapped_column(Integer)
    band_id: Mapped[str] = mapped_column(ForeignKey('bands.id'), nullable=False)
    band: Mapped['Band'] = relationship('Band', back_populates='discography')
    songs: Mapped[List['Track']] = relationship(
        'Track', back_populates='album', cascade='delete, all', lazy='selectin')
    pictures: Mapped[List['AlbumPicture']] = relationship(
        secondary='associations_album_picture', back_populates='album'
    )
    # picture_associations: Mapped[List['AssociationsAlbumPicture']] = relationship(back_populates='album')
    commentary: Mapped[str] = mapped_column(String(300), nullable=True)


class Track(Base):
    __tablename__ = 'songs'

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    num_song: Mapped[int] = mapped_column(Integer, nullable=False)
    sound_time: Mapped[float] = mapped_column(Float(3))
    album_id: Mapped[str] = mapped_column(ForeignKey("albums.id"), nullable=False) 
    album: Mapped["Album"] = relationship("Album", back_populates="songs")


class Genre(Base):
    __tablename__ = 'genres'

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    genre: Mapped[str] = mapped_column(String(20), nullable=False)
    bands: Mapped[List['Band']] = relationship(
        secondary='association_table_band_genres', back_populates='genres',
    )
    # band_associations: Mapped[List['AssociationBandGenres']] = relationship(back_populates='genre')


class BandPicture(Base):
    __tablename__ = 'band_pictures'

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    path: Mapped[str] = mapped_column(String(300), nullable=True)
    bands: Mapped[List['Band']] = relationship(
        secondary='association_band_pictures', back_populates='pictures'
    )
    # band_associations: Mapped[List['AssociationBandPicture']] = relationship(back_populates='picture')


class AlbumPicture(Base):
    __tablename__ = 'album_pictures'

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    path: Mapped[str] = mapped_column(String(60), nullable=True)
    album: Mapped[List['Album']] = relationship(
        secondary='associations_album_picture', back_populates='pictures'
    )
    # album_assotiations: Mapped[List['AssociationsAlbumPicture']] = relationship(back_populates='picture')


class AssociationsAlbumPicture(Base):
    __tablename__ = 'associations_album_picture'

    album_id: Mapped[str] = mapped_column(ForeignKey('albums.id'), primary_key=True)
    picture_id: Mapped[str] = mapped_column(ForeignKey('album_pictures.id'), primary_key=True)
    # album: Mapped['Album'] = relationship(back_populates='picture_associations')
    # picture: Mapped['AlbumPicture'] = relationship(back_populates='album_assotiations')


class AssociationBandPicture(Base):
    __tablename__ = 'association_band_pictures'

    band_id: Mapped[str] = mapped_column(ForeignKey('bands.id'), primary_key=True)
    picture_id: Mapped[str] = mapped_column(ForeignKey('band_pictures.id'), primary_key=True)
    # band: Mapped['Band'] = relationship(back_populates='picture_associations')
    # picture: Mapped['BandPicture'] = relationship(back_populates='band_associations')


class AssociationBandGenres(Base):
    __tablename__ = 'association_table_band_genres'

    band_id: Mapped[str] = mapped_column(ForeignKey('bands.id'), primary_key=True)
    genre_id: Mapped[str] = mapped_column(ForeignKey('genres.id'), primary_key=True)
    # band: Mapped['Band'] = relationship(back_populates='genre_associations')
    # genre: Mapped['Genre'] = relationship(back_populates='band_associations')

