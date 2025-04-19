from sqlalchemy import Column, Integer, LargeBinary, DateTime, func

from src.config.database.database import Base

class AiModelEntity(Base):
    __tablename__ = "ai_model"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    model_file = Column(LargeBinary, nullable=False)
    vectorizer_file = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)