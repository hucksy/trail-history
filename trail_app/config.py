from functools import lru_cache
from pydantic import BaseSettings


class EnvConfigs(BaseSettings):
    """secret config stuff validated with pydantic"""
    SECRET_KEY: str
    SENTINEL_CLIENT_ID: str
    SENTINEL_CLIENT_SECRET: str
    ENVIRONMENT: str


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf8'


@lru_cache
def get_env_config() -> EnvConfigs:
    return EnvConfigs()
