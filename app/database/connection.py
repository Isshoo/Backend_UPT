from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool

from ..config import DATABASE_URL
from ..utils.logger import db_logger as logger


engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,  # Increase pool size
    max_overflow=20,  # Increase max overflow
    pool_timeout=30,  # Increase timeout to 60 seconds
    pool_recycle=3600,  # Recycle connections after 1 hour
    pool_pre_ping=True,  # Enable connection health checks
    # Set connection timeout
    connect_args={
        "connect_timeout": 10,
        "application_name": "Flask"
    }
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()


# Event listener untuk logging


@event.listens_for(engine, "connect")
def receive_connect(dbapi_connection, connection_record):
    logger.info("New database connection established")


@event.listens_for(engine, "checkout")
def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    logger.debug("Connection checked out from pool")


# Health check function


def check_database_health():
    """Check if database is accessible"""
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return False
