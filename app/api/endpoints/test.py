from fastapi import APIRouter, Depends
from app.api import deps
from app.core import security

router = APIRouter()

@router.get('/test', response_model=security.ApiKey)
async def test(api_key: security.ApiKey=Depends(deps.check_api_key)):
    return api_key