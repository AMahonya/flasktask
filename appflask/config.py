import os
from dotenv import load_dotenv
import secrets

SECRET_KEY = secrets.token_urlsafe(32)

load_dotenv()


class Settings:
    DB_HOST: str = os.getenv("DB_HOST")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_PORT: int = os.getenv("DB_PORT")


settings = Settings()


def get_url_db():
    return f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
