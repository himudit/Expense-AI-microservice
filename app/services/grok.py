from openai import AsyncOpenAI
from app.config import settings
from app.services.base import BaseAIService

class GrokService(BaseAIService):
    def __init__(self):
        # Your API key (gsk_...) is for Groq (the super-fast AI company), not Grok (by xAI)!
        # So we need to point this to Groq's API url instead.
        self.client = AsyncOpenAI(
            api_key=settings.GROK_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )
        self.model = settings.GROK_MODEL

    async def generate_chat_response(self, user_id: str, prompt: str) -> str:
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Grok API Error: {str(e)}")
