from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.crud import bands
from app.schemas import band as schema
from app.api import deps
from app.models import Band

router = APIRouter()


@router.get('/band/{band_id}', response_model=schema.BandFullSchema)
async def get_band_by_id(
    band_id: str,
    session: AsyncSession = Depends(deps.get_session),
):
    band = await bands.get_by_id(band_id=band_id, session=session)
    return band


@router.get('/band', response_model=List[schema.BandListSchema])
async def get_all_bands(
    session: AsyncSession = Depends(deps.get_session),
):
    bands_list = await bands.get_all_bands(session=session)
    return bands_list

@router.post('/band')
async def create_band(
    band: schema.BandSchema,
    session: AsyncSession = Depends(deps.get_session),
):
    """Create band"""

    return await bands.create(band=band, session=session)