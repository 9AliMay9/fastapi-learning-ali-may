import os

class Settings:
    # Database Settings
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://alimay:GXS2870gxs@localhost:5432/taskdb")

    # JWT Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
