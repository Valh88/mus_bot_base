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

import datetime
from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
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
        ('yes', 'active'),
        ('no', 'unactive')
    ]

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    contry_of_origin: Mapped[str] = mapped_column(String(30), nullable=False)
    location: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[ChoiceType] = mapped_column(ChoiceType(STATUS))
    formed_in: Mapped[datetime.datetime]
    # # ears_active: Mapped[str]
    # # genre
    # # discography: Mapped[str]
    themes: Mapped[str] = mapped_column(String(100), nullable=False)
    commentary: Mapped[str] = mapped_column(String(300))


class Album(Base):
    __tablename__ = 'albums'

    FORMAT = [
        ('cassette', 'cassete'),
        ('disc', 'disc'),
        ('vinil', 'vinil')
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
    # songs: