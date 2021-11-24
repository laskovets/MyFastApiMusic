from fastapi.routing import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from db.base import Author
from db.deps import get_db
from datetime import timedelta
from schemas.author import CreateSchema, AuthorSchema
from schemas.authentication import Token
from db.query_tools import get_or_create
from settings import ACCESS_TOKEN_EXPIRE_MINUTES
from tools.authentication import create_access_token, get_current_active_author


router = APIRouter()
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post("/register/", response_model=AuthorSchema, status_code=status.HTTP_201_CREATED)
async def register(*, new_author: CreateSchema, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(new_author.password)
    instance, created = await get_or_create(db, Author, {'name': new_author.name}, {'password': hashed_password})
    if created:
        return AuthorSchema(**instance.__dict__)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This author already exists!")


@router.post("/token/", response_model=Token)
async def login_author_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    author = db.query(Author).filter_by(**{'name': form_data.username}).one_or_none()
    if (not author) or (not pwd_context.verify(form_data.password, author.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={'WWW-Authenticate': 'bearer'}
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': author.name},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, "token_type": "bearer"}


@router.get("/authorization/test/")
async def test(author: Author = Depends(get_current_active_author)):
    return {"res": 'test_complete'}
