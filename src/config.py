import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "").strip()
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "").strip()
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "").strip()
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432").strip()
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "").strip()
