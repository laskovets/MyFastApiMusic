from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Tuple, Type
from db.base_class import Base


async def get_or_create(db: AsyncSession, model: Type[Base], filter_fields: dict, other_fields: dict = {}) -> Tuple[Base, bool]:
    q = select(model).filter_by(**filter_fields)
    instance = (await db.execute(q)).one_or_none()
    if instance:
        return instance, False
    all_fields = filter_fields.copy()
    all_fields.update(other_fields)
    instance = model(**all_fields)
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance, True
