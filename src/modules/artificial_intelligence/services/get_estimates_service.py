import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


class GetEstimatesService:
    def __init__(self, model_path: str = "model.pkl", vectorizer_path: str = "vectorizer.pkl"):
        self.model: any = pickle.load(open(model_path, "rb"))
        self.vectorizer: TfidfVectorizer = pickle.load(open(vectorizer_path, "rb"))

    def execute(self, description: str) -> float:
        x = self.vectorizer.transform([description])
        prediction = self.model.predict(x)[0]
        return round(prediction, 2)
