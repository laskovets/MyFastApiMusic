from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@localhost/my_fast_api_music"


engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
