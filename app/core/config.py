from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'AvaProDetailing_Bot'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
