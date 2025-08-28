import sys 
from wineQuality.exception import WineException
from wineQuality.logger import logging


logging.info("first log")

try:
    a = 12 / 0
except ZeroDivisionError as e:
    WineException(e , sys)