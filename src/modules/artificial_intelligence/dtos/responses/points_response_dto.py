from pydantic import BaseModel


class PointsResponseDTO(BaseModel):
    points: float
