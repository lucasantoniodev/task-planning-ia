from src.config.database.seeds.task_seed import create_task_seeds


def run_seeds():
    print("Iniciando a execução das seeds...")
    create_task_seeds()
    print("Seeds executadas com sucesso!")

if __name__ == "__main__":
    run_seeds()