from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings using Pydantic Settings with .env file support."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    # PostgreSQL Database settings
    pgsql_host: str = Field(default="localhost", description="PostgreSQL host")
    pgsql_port: int = Field(default=5432, description="PostgreSQL port")
    pgsql_user: str = Field(default="postgres", description="PostgreSQL username")
    pgsql_password: str = Field(default="root", description="PostgreSQL password")
    pgsql_db: str = Field(
        default="expense_tracker", description="PostgreSQL database name"
    )

    # JWT settings
    jwt_secret: str = Field(
        default="6e4b2a7c8f9d4e1a3b7f5c2e8d1f0a6b9c3e7d2a4f8b6c1e5d0a9f3b2c7e4d1",
        description="JWT secret key",
    )
    jwt_algorithm: str = Field(default="HS256", description="JWT algorithm")
    jwt_exp_delta_seconds: int = Field(
        default=3600, description="JWT expiration time in seconds"
    )

    # Application settings
    app_name: str = Field(default="Expense Tracker", description="Application name")
    app_version: str = Field(default="1.0.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")

    # Database settings
    database_echo: bool = Field(default=False, description="Echo SQL queries")

    # API settings

    @property
    def database_url(self) -> str:
        """Get PostgreSQL database URL."""
        return f"postgresql://{self.pgsql_user}:{self.pgsql_password}@{self.pgsql_host}:{self.pgsql_port}/{self.pgsql_db}"

    @property
    def database_url_async(self) -> str:
        """Get asynchronous PostgreSQL database URL."""
        return f"postgresql+asyncpg://{self.pgsql_user}:{self.pgsql_password}@{self.pgsql_host}:{self.pgsql_port}/{self.pgsql_db}"


# Create a global settings instance
settings = Settings()
