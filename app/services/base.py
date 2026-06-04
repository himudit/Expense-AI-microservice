from abc import ABC, abstractmethod

class BaseAIService(ABC):
    @abstractmethod
    async def generate_chat_response(self, user_id: str, prompt: str) -> str:
        pass
