from sqlalchemy.orm import Session
from typing import Tuple, Type
from app.db.base_class import Base


async def get_or_create(db: Session, model: Type[Base], filter_fields: dict, other_fields: dict = {}) -> Tuple[Base, bool]:
    instance = db.query(model).filter_by(**filter_fields).one_or_none()
    if instance:
        return instance, False
    all_fields = filter_fields.copy()
    all_fields.update(other_fields)
    instance = model(**all_fields)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance, True
