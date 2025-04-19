import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression

from src.modules.artificial_intelligence.entities.ai_model_entity import AiModelEntity
from src.modules.artificial_intelligence.services.create_ai_model_service import CreateAIModelService
from src.modules.artificial_intelligence.services.get_all_tasks_service import GetAllTasksService


def main():
    get_all_tasks_service = GetAllTasksService()
    tasks = get_all_tasks_service.execute()

    df = pd.DataFrame(tasks, columns=["description", "points"])

    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(df["description"])
    y = df["points"]

    model = LinearRegression()
    model.fit(x, y)

    model_blob = pickle.dumps(model)
    vectorizer_blob = pickle.dumps(vectorizer)

    create_ai_model_service = CreateAIModelService()
    create_ai_model_service.execute(AiModelEntity(
        model_file=model_blob,
        vectorizer_file=vectorizer_blob,
    ))

    print("Modelo treinado e salvo no banco de dados!")


if __name__ == "__main__":
    main()
