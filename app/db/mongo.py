from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

MONGO_URI = settings.MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)

db = client["expensemate_ai"]
messages_collection = db["messages"]