from src.modules.artificial_intelligence.entities.ai_model_entity import AiModelEntity
from src.modules.artificial_intelligence.repositories.ai_model_repository import AiModelRepository


class CreateAIModelService:
    def __init__(self):
        self.repository = AiModelRepository()

    def execute(self, ai_model: AiModelEntity):
        return self.repository.create(ai_model)
