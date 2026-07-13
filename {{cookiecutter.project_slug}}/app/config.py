from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="{{ cookiecutter.project_name }}")
    environment: str = Field(default="local")
    log_level: str = Field(default="INFO")
    model_provider: str = Field(default="{{ cookiecutter.model_provider }}")
    vector_store: str = Field(default="{{ cookiecutter.vector_store }}")

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
