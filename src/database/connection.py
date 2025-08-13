from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool

from ..config import DATABASE_URL


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
