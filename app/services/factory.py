from app.config import settings
from app.services.base import BaseAIService

def get_ai_service() -> BaseAIService:
    """
    Factory function to return the correct AI service instance 
    based on the AI_PROVIDER environment variable.
    """
    if settings.AI_PROVIDER == "grok":
        from app.services.grok import GrokService
        return GrokService()
    
    # Default to gemini
    from app.services.gemini import GeminiService
    return GeminiService()

# Create a single instance to be used across the app
ai_service = get_ai_service()
