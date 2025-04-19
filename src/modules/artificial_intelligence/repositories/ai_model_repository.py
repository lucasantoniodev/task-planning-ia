from sqlalchemy.future import select

from src.config.database.dependecies import get_db
from src.modules.artificial_intelligence.entities.ai_model_entity import AiModelEntity


class AiModelRepository:
    def __init__(self):
        self.db = next(get_db())

    def create(self, ai_model: AiModelEntity):
        self.db.add(ai_model)
        self.db.commit()
        self.db.refresh(ai_model)

    def get_latest(self) -> AiModelEntity:
        result = self.db.query(AiModelEntity).order_by(AiModelEntity.created_at.desc()).first()

        if not result:
            raise ValueError("Nenhum modelo AI encontrado no banco de dados.")

        return result
