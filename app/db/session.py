from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD


SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
