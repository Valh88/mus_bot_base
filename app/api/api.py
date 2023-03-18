from fastapi import APIRouter

from app.api.endpoints import auth, users, band, genre, media, test

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(band.router, prefix="/band", tags=["bands"])
api_router.include_router(genre.router, prefix="/genre", tags=["genres"])
api_router.include_router(media.router, prefix="/media", tags=["media"])
api_router.include_router(test.router, prefix="/test", tags=["test"])