from src.modules.artificial_intelligence.entities.ai_model_entity import AiModelEntity
from src.modules.artificial_intelligence.entities.task_entity import TaskEntity
from src.modules.artificial_intelligence.repositories.ai_model_repository import AiModelRepository
from src.modules.artificial_intelligence.repositories.task_repository import TaskRepository


class GetAllTasksService:
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self):
        return self.repository.get_all()