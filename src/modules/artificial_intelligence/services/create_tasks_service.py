from src.modules.artificial_intelligence.dtos.requests.create_task_request_dto import CreateTaskRequestDTO
from src.modules.artificial_intelligence.dtos.responses.task_response_dto import TaskResponseDTO
from src.modules.artificial_intelligence.process.train import train_model
from src.modules.artificial_intelligence.repositories.task_repository import TaskRepository


class CreateTasksService:
    def __init__(self):
        self.repository = TaskRepository()

    def execute(self, tasks: list[CreateTaskRequestDTO]):
        result = self.repository.create_many(tasks)
        train_model()
        return [TaskResponseDTO.model_validate(task) for task in result]
