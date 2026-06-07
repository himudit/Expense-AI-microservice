from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class Settings(BaseSettings):
    # Which AI to use: "gemini" or "grok"
    AI_PROVIDER: Literal["gemini", "grok"] = "grok"
    
    # Gemini Config
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-1.5-flash"
    
    # Grok Config
    GROK_API_KEY: str = ""
    GROK_MODEL: str = "grok-beta"

    # Mongo Config
    MONGO_URI: str = ""
    
    # Appwrite Config
    APPWRITE_ENDPOINT: str = ""
    APPWRITE_PROJECT_ID: str = ""
    APPWRITE_API_KEY: str = ""
    APPWRITE_DATABASE_ID: str = ""
    # Main
    APPWRITE_COLLECTION1_ID: str = ""
    # Expense
    APPWRITE_COLLECTION2_ID: str = ""
    # Profile
    APPWRITE_COLLECTION3_ID: str = ""
    # Category
    APPWRITE_COLLECTION4_ID: str = ""
    # Income
    APPWRITE_COLLECTION5_ID: str = ""
    # Category Income
    APPWRITE_COLLECTION6_ID: str = ""
    # Recurring Transactions
    APPWRITE_COLLECTION7_ID: str = ""
    # Profile
    APPWRITE_BUCKET_ID: str = ""
    # Expense
    APPWRITE_BUCKET2_ID: str = ""
    # Income
    APPWRITE_BUCKET3_ID: str = ""
    
    # Loads variables from the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Initialize a global settings object
settings = Settings()
