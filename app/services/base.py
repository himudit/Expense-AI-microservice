from abc import ABC, abstractmethod

class BaseAIService(ABC):
    @abstractmethod
    async def generate_chat_response(self, prompt: str) -> str:
        """
        Takes a prompt string and returns the AI-generated response string.
        """
        pass
