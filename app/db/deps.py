from typing import Generator
from db.session import SessionLocal


async def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
