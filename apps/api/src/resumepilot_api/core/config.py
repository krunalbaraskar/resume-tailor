from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration comes from environment variables (or a .env file).

    Field `database_url` is read from env var DATABASE_URL, and so on.
    Nothing secret is hard-coded; these defaults are for local dev only.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database (localhost because the API runs on your machine, DB in Docker)
    database_url: str = (
        "postgresql+psycopg://resumepilot:resumepilot@localhost:5432/resumepilot"
    )

    # Auth
    jwt_secret: str = "change-me-in-production"
    jwt_expire_minutes: int = 10080  # 7 days

    # Storage for uploaded files
    storage_dir: str = "./storage"

    # LLM (used from Week 2)
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-sonnet-4-5"
    llm_provider: str = "auto"  # auto | anthropic | fake


settings = Settings()
