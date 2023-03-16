from fastapi import APIRouter, Depends
from app.api import deps
from app.core import security

router = APIRouter(dependencies=[Depends(deps.check_api_key)])

@router.get('/test')
async def test():
    return '123'