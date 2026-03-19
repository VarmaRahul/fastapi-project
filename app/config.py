from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # These must exist because Docker is injecting them
    db_user: str
    db_password: str
    db_name: str
    
    db_connection: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    # This tells Pydantic to look for a .env file automatically
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

print(f"DEBUG: Connecting to {settings.db_connection}")