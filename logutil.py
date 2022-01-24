import logging
from datetime import datetime

def getlogger(nm):
    logging.basicConfig(filename="applog" + datetime.now().strftime('%d%m%Y') + ".log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    # Creating an object
    logger = logging.getLogger(nm)
    logger.setLevel(logging.DEBUG)

    return logger
