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
    
    # Loads variables from the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Initialize a global settings object
settings = Settings()
