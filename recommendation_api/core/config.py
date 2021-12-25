from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "TEXT BASED RECOMMENDATION API"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
