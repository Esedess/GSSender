import logging

from .constants import LOGGING_LEVEL

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

formatter = logging.Formatter('%(levelname)s - %(message)s')
handler = logging.StreamHandler()

handler.setFormatter(formatter)
logger.addHandler(handler)
