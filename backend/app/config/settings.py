from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str = "demo_key"
    OPENAI_MODEL: str = "gpt-4o-mini"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"
    DATABASE_URL: str = "sqlite:///./retail_quality.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    CHROMA_PERSIST_DIRECTORY: str = "./.chroma"
    APP_ENV: str = "development"
    CORS_ORIGINS: str = "http://localhost:3000"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
