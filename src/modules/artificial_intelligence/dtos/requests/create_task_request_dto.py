from pydantic import BaseModel


class CreateTaskRequestDTO(BaseModel):
    description: str
    points: int
