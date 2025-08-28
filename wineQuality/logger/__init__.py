import logging
import os 
from datetime import datetime
from from_root import from_root


# make the log dir
LOG_DIR = os.path.join(from_root() , "logs")
os.makedirs(LOG_DIR , exist_ok = True)

# log filename
now = datetime.now()
LOG_FILE = f"{now.strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# create the log message format
log_format = "[%(asctime)s] Line: %(lineno)d | %(name)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = log_format,
    datefmt = date_format,
    level = logging.INFO
)

