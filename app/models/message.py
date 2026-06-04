from pydantic import BaseModel, Field
from datetime import datetime


class Message(BaseModel):
    user_id: str
    role: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)