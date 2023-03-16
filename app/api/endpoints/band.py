from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import band
from app.schemas import band as schema
from app.api import deps

router = APIRouter()


@router.post('/create-band', response_model=schema.BandSchema)
async def create_band(
    band: schema.BandSchema,
    session: AsyncSession = Depends(deps.get_session),
):
    """Create band"""

    return band