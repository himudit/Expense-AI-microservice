import json
from openai import AsyncOpenAI
from app.config import settings
from app.services.base import BaseAIService
from app.prompts.system_prompts import EXPENSEMATE_SYSTEM_PROMPT
from app.prompts.prompt_builder import build_chat_messages
from app.services.chat_history_service import get_recent_messages
from app.tools.tool_definitions import TOOLS
from app.tools.tool_executor import execute_tool
from datetime import date


class GrokService(BaseAIService):
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.GROK_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )
        self.model = settings.GROK_MODEL

    async def generate_chat_response(self, user_id: str, prompt: str) -> str:
        try:
            systemPrompt = EXPENSEMATE_SYSTEM_PROMPT.format(
                current_date=date.today().isoformat()
            )
            history_messages = await get_recent_messages(user_id)
            messages = build_chat_messages(systemPrompt, history_messages, prompt)
            response = await self.client.chat.completions.create(
                model=self.model, messages=messages, tools=TOOLS, tool_choice="auto"
            )
            message = response.choices[0].message

            if message.tool_calls:
                assistant_message = {
                    "role": "assistant",
                    "content": message.content,
                    "tool_calls": [
                        {
                            "id": tool_call.id,
                            "type": tool_call.type,
                            "function": {
                                "name": tool_call.function.name,
                                "arguments": tool_call.function.arguments,
                            },
                        }
                        for tool_call in message.tool_calls
                    ],
                }
                messages.append(assistant_message)

                # Process all tool calls requested by the model
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    arguments = json.loads(tool_call.function.arguments or "{}") or {}
                    # Inject user_id from context so the LLM doesn't have to guess/provide it
                    arguments["user_id"] = user_id
                    tool_result = await execute_tool(tool_name, arguments)
                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": tool_name,
                            "content": json.dumps(tool_result),
                        }
                    )

                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                )
                return response.choices[0].message.content
            return response.choices[0].message.content

        except Exception as e:
            raise Exception(f"Grok API Error: {str(e)}") from e
