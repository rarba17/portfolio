from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Portfolio API"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_debug: bool = True

    frontend_origins: str = "http://localhost:5173,http://127.0.0.1:5173"

    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    contact_to_email: str = ""
    contact_from_email: str = ""

    contact_rate_limit: int = 3
    contact_rate_window_seconds: int = 600

    @property
    def parsed_origins(self) -> list[str]:
        return [origin.strip() for origin in self.frontend_origins.split(",") if origin.strip()]


settings = Settings()
BASE_DIR = Path(__file__).resolve().parents[2]
ROOT_DIR = BASE_DIR.parent
FRONTEND_DIST_DIR = ROOT_DIR / "frontend" / "dist"
RESUME_FILE = ROOT_DIR / "public" / "resume.pdf"
