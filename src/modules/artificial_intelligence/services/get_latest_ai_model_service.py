import pickle

from src.modules.artificial_intelligence.repositories.ai_model_repository import AiModelRepository


class GetLatestAiModelService:
    def __init__(self):
        self.repository = AiModelRepository()

    def execute(self):
        result = self.repository.get_latest()
        vectorizer = pickle.loads(result.vectorizer_file)
        model = pickle.loads(result.model_file)
        return vectorizer, model
