from fastapi.routing import APIRouter, Request
# from fastapi import Depends
# from sqlalchemy.orm import Session
# from schemas.author import AuthorSchema, AuthorBase
# from db.deps import get_db
# from models.author import Author


router = APIRouter()


# @router.post("/authors", response_model=AuthorSchema)
# async def create_author(request: Request, author: AuthorBase, db: Session = Depends(get_db)) -> dict:
#     obj = Author(**author.dict())
#     db.add(obj)
#     await db.commit()
#     await db.refresh(obj)
#     return obj
