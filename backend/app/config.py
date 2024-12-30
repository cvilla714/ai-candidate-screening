from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from enum import StrEnum
import logging

class LogLevelEnum(StrEnum):
    DEBUG = logging.getLevelName(logging.DEBUG)
    INFO = logging.getLevelName(logging.INFO)
    WARNING = logging.getLevelName(logging.WARNING)
    ERROR = logging.getLevelName(logging.ERROR)
    CRITICAL = logging.getLevelName(logging.CRITICAL)

class Settings(BaseSettings):
    # App settings
    app_name: str = "Candidate Screening API"
    api_version: str = "v1"
    environment: str = os.getenv("ENV", "local")
    db_hostname: str = "db"
    db_name: str = "candidates_db"
    db_password: str = "password"
    db_port: int = 5432
    db_username: str = "user"

    # Database settings
    sqlalchemy_database_uri: str = (
        "postgresql://user:password@db:5432/candidates_db"
    )
    sqlalchemy_test_database_uri: str = (
        "postgresql://user:password@db-test:5432/candidates_test_db"
    )

    # Logging settings
    log_level: str = LogLevelEnum.DEBUG
    log_format: str = "%(levelname)s: %(message)s"
    log_file: str = "app.log"

    # CORS settings
    cors_origins: list = [
        "http://localhost:3000",
    ]
    cors_methods: list = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    cors_allow_headers: list = [
        "Authorization",
        "Content-Type",
        "Access-Control-Allow-Origin",
    ]

    # Model config
    model_config = SettingsConfigDict(
        env_file=f"conf/.env", extra="ignore"
    )

    def get_database_uri(self, is_test=False) -> str:
        """
        Return the database URI based on the environment.
        If `is_test` is True, return the test database URI.
        """
        if is_test:
            return self.sqlalchemy_test_database_uri
        return self.sqlalchemy_database_uri

settings = Settings()
