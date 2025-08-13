# logger.py

import logging


def setup_logger(name, level=logging.INFO):
    """Set up a logger with the specified name and level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger


# You can create different loggers for different modules or components of your application.
# For example:
# db_logger = setup_logger('database_logger', level=logging.DEBUG)
# db_logger.debug("This is a debug message for the database module")


db_logger = setup_logger('database', level=logging.INFO)
app_logger = setup_logger('app', level=logging.INFO)
