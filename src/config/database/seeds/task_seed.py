from src.config.database.dependecies import get_db
from src.modules.artificial_intelligence.entities.task_entity import TaskEntity

def create_task_seeds():
    db = next(get_db())

    if db.query(TaskEntity).count() == 0:
        tasks = [TaskEntity(description="Criar uma página de login com autenticação", points=5),
                 TaskEntity(description="Criar dashboard com gráficos e métricas", points=20),
                 TaskEntity(description="Implementar API para pagamentos", points=10),
                 TaskEntity(description="Refatorar código legado", points=30)]

        db.bulk_save_objects(tasks)
        db.commit()
        print("Dados de seed para TaskEntity criados com sucesso!")
