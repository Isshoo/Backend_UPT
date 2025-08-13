from dotenv import load_dotenv
import os

load_dotenv()


class EnvironmentConfig:
    # Flask configuration
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.getenv("FLASK_PORT", 3001))
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"

    # database configuration
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL environment variable is not set")

    # JWT configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    if not JWT_SECRET_KEY:
        raise ValueError("JWT_SECRET_KEY environment variable is not set")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRES = int(
        os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))  # default to 1 hour


# Load configurations
env = EnvironmentConfig()
