from ...database.connection import engine
from ...utils.logger import db_logger as logger


def check_database_health():
    """Check if database is accessible"""
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return False
