import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data.csv")

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(df["description"])
y = df["estimation"]

model = LinearRegression()
model.fit(x, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Modelo treinado e salvo!")