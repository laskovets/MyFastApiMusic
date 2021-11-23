from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Author(Base):
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    albums = relationship('Album', back_populates='author', uselist=True)
    tracks = relationship('Track', back_populates='author', uselist=True)
    password = Column(String, nullable=False)
