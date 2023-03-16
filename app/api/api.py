from fastapi import APIRouter

from app.api.endpoints import auth, users, band, test

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(band.router, prefix="/band", tags=["bands"])
api_router.include_router(test.router, prefix="/test", tags=["test"])