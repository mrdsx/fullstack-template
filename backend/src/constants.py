import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_ORIGINS = [os.getenv("ALLOWED_ORIGIN", "http://localhost:5173")]
APP_HOST = "127.0.0.1"
APP_PORT = 8000

PROJECT_ENV = os.getenv("PROJECT_ENV")
PRODUCTION_ENVIRONMENT = "production"
DEVELOPMENT_ENV = "development"
