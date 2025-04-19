from uuid import UUID
from pydantic import BaseModel

class TaskResponseDTO(BaseModel):
    id: UUID
    description: str
    points: int

    class Config:
        from_attributes = True