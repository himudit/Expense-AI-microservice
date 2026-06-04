from app.config import settings
from app.services.base import BaseAIService

def get_ai_service() -> BaseAIService:
    if settings.AI_PROVIDER == "grok":
        from app.services.grok import GrokService
        return GrokService()
    from app.services.gemini import GeminiService
    return GeminiService()

ai_service = get_ai_service()
