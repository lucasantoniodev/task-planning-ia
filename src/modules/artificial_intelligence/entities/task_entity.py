from uuid import uuid4
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

from src.config.database.database import Base


class TaskEntity(Base):
    __tablename__ = 'task'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    description = Column(String, nullable=False)
    points = Column(Integer, nullable=False)
