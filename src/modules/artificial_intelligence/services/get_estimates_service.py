import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from src.modules.artificial_intelligence.services.get_latest_ai_model_service import GetLatestAiModelService


class GetEstimatesService:
    def __init__(self):
        self.get_latest_ai_model_service = GetLatestAiModelService()

    def execute(self, description: str) -> float:
        vectorizer, model = self.get_latest_ai_model_service.execute()
        x = vectorizer.transform([description])
        prediction = model.predict(x)[0]
        return round(prediction, 2)
