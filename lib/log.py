import logging
from logging.handlers import RotatingFileHandler

def get_logger(): 
  handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
  logger = logging.getLogger('tdm')
  logger.setLevel(logging.ERROR)
  logger.addHandler(handler)

  return logger