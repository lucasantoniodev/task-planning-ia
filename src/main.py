import uvicorn
from fastapi import FastAPI

from src.config.database.migrations import run_migrations
from src.modules import artificial_intelligence

run_migrations()
app = FastAPI()
app.include_router(artificial_intelligence.router, prefix="/ai", tags=["AI"])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)
