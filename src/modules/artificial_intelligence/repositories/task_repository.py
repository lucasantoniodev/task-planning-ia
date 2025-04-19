from src.config.database.dependecies import get_db
from sqlalchemy.future import select

from src.modules.artificial_intelligence.entities.ai_model_entity import AiModelEntity
from src.modules.artificial_intelligence.entities.task_entity import TaskEntity


class TaskRepository:
    def __init__(self):
        self.db = next(get_db())

    def get_all(self):
        tasks = self.db.query(TaskEntity.description, TaskEntity.points).all()
        return tasks

