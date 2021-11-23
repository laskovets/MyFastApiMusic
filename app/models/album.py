from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Album(Base):
    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    author = relationship("Author", cascade='all,delete-orphan', back_populates="albums", single_parent=True)
    tracks = relationship('Track', back_populates='album', uselist=True)
