from src.modules.artificial_intelligence import router
from src.modules.artificial_intelligence.dtos.responses.points_response_dto import PointsResponseDTO
from src.modules.artificial_intelligence.services.get_estimates_service import GetEstimatesService

path = "/estimates"
summary = "Rota para buscar estimativa sugerida pela inteligência artificial"


@router.get(path, response_model=PointsResponseDTO, summary=summary)
def execute(description: str) -> PointsResponseDTO:
    service = GetEstimatesService()
    points = service.execute(description)
    return PointsResponseDTO(points=points)
