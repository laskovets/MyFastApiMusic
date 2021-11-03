from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorSchema(AuthorBase):
    id: int
