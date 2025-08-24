import logging
from datetime import datetime
import os

DIR = "logs"
os.makedirs(DIR, exist_ok=True)

LOG_FILE = os.path.join(DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%M:%S'
)

def get_logger(name):
    """
    Returns a logger with the specified name.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
