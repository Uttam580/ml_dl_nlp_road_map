import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('./Basic/rotating_file_handler.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(1000):
    logger.info('Hello, world!')