import logging
import logging.handlers
import os

from utils import get_full_file_name


LOG_DIR = 'logs'
LOG_FILENAME = 'app.log'
LOG_FORMAT_STRING = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATE_FORMAT = '%m/%d/%Y %H:%M:%S %Z'

if not os.path.exists(get_full_file_name(LOG_DIR)):
    os.mkdir(get_full_file_name(LOG_DIR))


logger = logging.getLogger()

logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
# fh = logging.FileHandler('app.log')
fh = logging.handlers.RotatingFileHandler(
        os.path.join(os.path.abspath(LOG_DIR), LOG_FILENAME),
        maxBytes=1024*10,
        backupCount=2)

fh.setLevel(logging.INFO)

# create formatter and add it to the handlers
logging.basicConfig(format=LOG_FORMAT_STRING, datefmt=LOG_DATE_FORMAT)
formatter = logging.Formatter(LOG_FORMAT_STRING, datefmt=LOG_DATE_FORMAT)
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
