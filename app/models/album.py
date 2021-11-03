from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Album(Base):
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    author = relationship("AuthorSchema", back_populates="albums")
    tracks = relationship('Track', cascade='all,delete-orphan', back_populates='album', uselist=True)
