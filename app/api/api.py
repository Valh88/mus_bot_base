from fastapi import APIRouter, Depends
from app.api.endpoints import auth, users, band, genre, media, album, test
from app.api.deps import check_api_key
api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    band.router,
    prefix="/band", tags=["bands"],
    dependencies=[Depends(check_api_key)]
)
api_router.include_router(
    album.router,
    prefix="/album", tags=["albums"],
    dependencies=[Depends(check_api_key)]
)
api_router.include_router(
    genre.router, prefix="/genre", tags=["genres"],
    dependencies=[Depends(check_api_key)],
)
api_router.include_router(
    media.router, prefix="/media", tags=["media"],
    dependencies=[Depends(check_api_key)]
)
api_router.include_router(
    test.router, prefix="/test", tags=["test"],
    dependencies=[Depends(check_api_key)]
)
