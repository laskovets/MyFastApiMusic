from pydantic import BaseModel
from pydantic import Field


class AuthorBase(BaseModel):
    name: str = Field(min_length=3)


class AuthorSchema(AuthorBase):
    id: int


class CreateSchema(AuthorBase):
    password: str = Field(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{8,}$')
