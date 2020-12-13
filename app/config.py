import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger(__name__)

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 1)

@lru_cache() # will cache this function.  Should only see the warning log once 
def get_settings() -> BaseSettings:
    log.warn("Loading config settings from the environment...")
    return Settings()

