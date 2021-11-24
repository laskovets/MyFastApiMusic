from fastapi.routing import APIRouter, Request
from fastapi import Path, Depends
from sqlalchemy.orm import Session
from schemas.tracks import TrackBase
from db.deps import get_db
from db.base import Track


router = APIRouter()


@router.get('/tracks/{id}', response_model=TrackBase)
async def get_track(*, id: int = Path(..., gt=0), request: Request, db: Session = Depends(get_db)) -> dict:
    result = db.query(Track).filter(Track.id == id).first()
    if result is None:
        return {}
    return TrackBase(**result).dict()
