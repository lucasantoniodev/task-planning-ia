from fastapi import FastAPI
import pickle
from pydantic import BaseModel

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = FastAPI()

class TaskRequest(BaseModel):
    description: str

@app.post("/predict")
def predict(task: TaskRequest):
    X = vectorizer.transform([task.description])
    prediction = model.predict(X)[0]
    return { "estimated_points": round(prediction, 2)}