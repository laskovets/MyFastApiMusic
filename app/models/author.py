from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


# Dasha 219p
class Author(Base):
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    albums = relationship('Album', cascade='all,delete-orphan', back_populates='author', uselist=True)
    tracks = relationship('Track', cascade='all,delete-orphan', back_populates='author', uselist=True)
