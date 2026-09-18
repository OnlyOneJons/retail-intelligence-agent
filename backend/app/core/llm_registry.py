from typing import Optional
from langchain_openai import ChatOpenAI
from app.core.config import settings

class LLMRegistry:
    """Registry providing wire-compatible LLM instances (OpenAI, Atlas Cloud, DeepSeek, Ollama, etc.)."""
    
    @staticmethod
    def get_chat_model(
        model_name: Optional[str] = None,
        temperature: Optional[float] = None
    ) -> ChatOpenAI:
        return ChatOpenAI(
            model=model_name or settings.DEFAULT_LLM_MODEL,
            temperature=temperature if temperature is not None else settings.LLM_TEMPERATURE,
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_BASE_URL,
            timeout=30.0,
            max_retries=2,
        )

llm_registry = LLMRegistry()
