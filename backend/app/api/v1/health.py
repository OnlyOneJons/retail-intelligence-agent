from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import settings

router = APIRouter(prefix="/health", tags=["Health Checks"])

class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str
    services: dict

@router.get("", response_model=HealthResponse)
async def health_check():
    """Liveness and readiness probe for the AI Agent service."""
    return HealthResponse(
        status="HEALTHY",
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
        services={
            "langgraph_checkpointer": "READY",
            "llm_registry": "CONFIGURED",
            "omnicore_service": settings.OMNICORE_API_URL,
            "clearsettle_service": settings.CLEARSETTLE_API_URL,
            "edgepulse_service": settings.EDGEPULSE_API_URL,
        }
    )
