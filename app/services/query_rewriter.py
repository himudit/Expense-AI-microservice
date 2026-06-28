from openai import AsyncOpenAI

from app.config import settings
from app.prompts.rewrite_prompt import QUERY_REWRITE_PROMPT


class QueryRewriter:

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.GROK_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )

        self.model = settings.GROK_MODEL

    async def rewrite(
        self,
        history_messages: list,
        user_message: str,
    ):

        messages = [
            {
                "role": "system",
                "content": QUERY_REWRITE_PROMPT,
            }
        ]

        messages.extend(history_messages)

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0,
        )

        return response.choices[0].message.content.strip()


query_rewriter = QueryRewriter()