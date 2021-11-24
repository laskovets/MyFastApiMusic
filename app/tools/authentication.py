from typing import Optional
from datetime import timedelta, datetime
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from settings import SECRET_KEY, ALGORITHM
from db.base import Author
from db.deps import get_db
from schemas.authentication import TokenData
from schemas.author import AuthorSchema


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_author(name: str):
    db = next(get_db())
    author = db.query(Author).filter_by(**{'name': name}).one_or_none()
    if author is not None:
        return AuthorSchema(**author.__dict__)


async def get_current_author(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        author_name: str = payload.get('sub')
        if author_name is None:
            raise credentials_exception
        token_data = TokenData(author_name=author_name)
    except JWTError:
        raise credentials_exception
    author = get_author(token_data.author_name)
    if author is None:
        raise credentials_exception
    return author


async def get_current_active_author(current_author: Author = Depends(get_current_author)):
    return current_author
