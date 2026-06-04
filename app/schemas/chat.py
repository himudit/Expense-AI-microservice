from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    # Field validation ensures the message isn't empty
    user_id: str
    message: str = Field(..., min_length=1, description="The message from the user")

class ChatResponse(BaseModel):
    reply: str = Field(..., description="The AI response")
