from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router
from app.api.v1.metrics import router as metrics_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Enterprise AI Agent & Operations Copilot Microservice using FastAPI and LangGraph",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(health_router, prefix="/api/v1")
app.include_router(chat_router, prefix="/api/v1")
app.include_router(metrics_router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "OPERATIONAL",
        "documentation": "/docs"
    }
