from sys import stdout
from logging.handlers import RotatingFileHandler
from logging import StreamHandler, INFO, getLogger, Formatter
from config import LOGGER_PATH, LOGGER_MAX_BYTES, LOGGER_BACKUP_COUNT

formatter = Formatter(
    fmt='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

logger = getLogger(name='logstash')
logger.setLevel(INFO)


handler = RotatingFileHandler(
    LOGGER_PATH, maxBytes=LOGGER_MAX_BYTES, backupCount=LOGGER_BACKUP_COUNT)

handler.setFormatter(formatter)

stream_handler = StreamHandler(stdout)


logger.addHandler(handler)
logger.addHandler(stream_handler)
