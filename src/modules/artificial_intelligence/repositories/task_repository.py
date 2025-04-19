from src.config.database.dependecies import get_db

from src.modules.artificial_intelligence.dtos.requests.create_task_request_dto import CreateTaskRequestDTO
from src.modules.artificial_intelligence.entities.task_entity import TaskEntity


class TaskRepository:
    def __init__(self):
        self.db = next(get_db())

    def create(self, task: TaskEntity):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def create_many(self, tasks_request: list[CreateTaskRequestDTO]):
        tasks = [TaskEntity(description=task_request.description, points=task_request.points) for task_request in
                 tasks_request]
        self.db.add_all(tasks)
        self.db.commit()
        return self.get_all()

    def get_all(self):
        tasks = self.db.query(TaskEntity.id, TaskEntity.description, TaskEntity.points).all()
        return tasks
