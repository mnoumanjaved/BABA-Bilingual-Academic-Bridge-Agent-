"""
Configuration file for BABA application.
Loads environment variables and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration class."""

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    # Application Settings
    APP_TITLE = os.getenv("APP_TITLE", "BABA - Bilingual Academic Bridge Agent")
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

    # Agent Settings
    MAX_TOKENS = 1500
    TEMPERATURE = 0.7

    # UI Settings
    PAGE_ICON = "🎓"
    LAYOUT = "wide"

    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY or cls.OPENAI_API_KEY == "your_openai_api_key_here":
            raise ValueError(
                "OPENAI_API_KEY not set! Please add your API key to the .env file."
            )
        return True

# Create config instance
config = Config()
