import os

from pydantic_settings import BaseSettings


class App(BaseSettings):
    debug: bool
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_prefix = "APP_"


class PostgresConfig(BaseSettings):
    url: str

    class Config:
        env_prefix = "POSTGRES_"


class MinioConfig(BaseSettings):
    endpoint: str
    access_key: str
    secret_key: str

    class Config:
        env_prefix = "MINIO_"


class MainConfig(BaseSettings):
    app: App = App()
    postgres: PostgresConfig = PostgresConfig()
    minio: MinioConfig = MinioConfig()

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')
