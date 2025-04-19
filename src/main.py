import uvicorn
from fastapi import FastAPI
import sys
import os

from src.modules import artificial_intelligence

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()

app.include_router(artificial_intelligence.router, prefix="/ai", tags=["AI"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)