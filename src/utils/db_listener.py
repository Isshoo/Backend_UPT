from sqlalchemy import event

from ..database.connection import engine
from ..utils.logger import db_logger as logger


@event.listens_for(engine, "connect")
def receive_connect(dbapi_connection, connection_record):
    logger.info("New database connection established")


@event.listens_for(engine, "checkout")
def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    logger.debug("Connection checked out from pool")
