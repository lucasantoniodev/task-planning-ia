from src.modules.artificial_intelligence import router
from src.modules.artificial_intelligence.dtos.requests.create_task_request_dto import CreateTaskRequestDTO
from src.modules.artificial_intelligence.dtos.responses.task_response_dto import TaskResponseDTO
from src.modules.artificial_intelligence.services.create_tasks_service import CreateTasksService

path = "/tasks"
summary = "Rota para buscar estimativa sugerida pela inteligência artificial"


@router.post(path, response_model=list[TaskResponseDTO], summary=summary, status_code=201)
def execute(tasks: list[CreateTaskRequestDTO]) -> list[TaskResponseDTO]:
    service = CreateTasksService()
    tasks = service.execute(tasks)
    return tasks
