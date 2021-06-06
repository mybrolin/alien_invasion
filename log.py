import logging
from settings import Settings

setting = Settings()

logging.basicConfig(filename=setting.logFileName, level=logging.INFO,
                    format="%(asctime)s %(levelname)s : %(message)s")

logging.disable(logging.CRITICAL)


def info(message):
    logging.info(message)


def debug(message):
    logging.debug(message)


def warning(message):
    logging.warning(message)


def error(message):
    logging.error(message)


def critical(message):
    logging.critical(message)
