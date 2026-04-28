"""Configuration settings for Food Store API"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # App
    app_name: str = "Food Store API"
    debug: bool = False
    version: str = "0.1.0"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # CORS
    allowed_origins: list = ["http://localhost:5173", "http://localhost:3000"]

    # Database (will be configured in database-design-migrations change)
    database_url: str = "postgresql://user:password@localhost:5432/foodstore"

    # JWT (will be configured in auth-backend-jwt change)
    secret_key: str = "dev-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # Logging
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
