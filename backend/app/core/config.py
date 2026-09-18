from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    PROJECT_NAME: str = "Retail Intelligence Agent"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176",
    ]

    # LLM Settings
    OPENAI_API_KEY: str = Field(default="demo-key")
    OPENAI_BASE_URL: str = Field(default="https://api.openai.com/v1")
    DEFAULT_LLM_MODEL: str = Field(default="gpt-4o-mini")
    LLM_TEMPERATURE: float = 0.1

    # Monorepo Microservices
    OMNICORE_API_URL: str = "http://localhost:3000"
    CLEARSETTLE_API_URL: str = "http://localhost:3001"
    EDGEPULSE_API_URL: str = "http://localhost:3002"

    # Tracing
    LANGFUSE_PUBLIC_KEY: str = ""
    LANGFUSE_SECRET_KEY: str = ""
    LANGFUSE_HOST: str = "https://cloud.langfuse.com"

settings = Settings()
