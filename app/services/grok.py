from openai import AsyncOpenAI
from app.config import settings
from app.services.base import BaseAIService
from app.prompts.system_prompts import (
    EXPENSEMATE_SYSTEM_PROMPT
)
from app.prompts.prompt_builder import (
    build_chat_messages
)
from app.services.chat_history_service import get_recent_messages

class GrokService(BaseAIService):
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.GROK_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )
        self.model = settings.GROK_MODEL

    async def generate_chat_response(self, user_id: str, prompt: str) -> str:
        try:
            history_messages = await get_recent_messages(user_id)
            messages = build_chat_messages(
                EXPENSEMATE_SYSTEM_PROMPT,
                history_messages,
                prompt
            )
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Grok API Error: {str(e)}")
