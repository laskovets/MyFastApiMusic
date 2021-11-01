from app.db.base_class import Base
from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship


class Track(Base):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    listeners = Column(Integer, nullable=False, default=0)
    playcount = Column(Integer, nullable=False, default=0)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=True, default=None)
    author = relationship('Author', back_populates='tracks')
    album_id = Column(Integer, ForeignKey('album.id'), nullable=True, default=None)
    album = relationship('Album', back_populates='tracks')
