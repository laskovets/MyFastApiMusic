from fastapi.routing import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.author import AuthorSchema, AuthorBase
from db.deps import get_db
from app.models.author import Author


router = APIRouter()


@router.post("/authors", response_model=AuthorBase)
async def create_author(request: Request, author: AuthorSchema, db: Session = Depends(get_db)) -> dict:
    obj = Author(**AuthorSchema.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
