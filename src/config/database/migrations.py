import src.modules.artificial_intelligence.entities  # noqa: F401 - Load artificial intelligence entities
from src.config.database import database


def run_migrations():
    database.Base.metadata.create_all(bind=database.engine)


if __name__ == '__main__':
    run_migrations()
