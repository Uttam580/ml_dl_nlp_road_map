import logging
import math

LOG_FORMAT  = '%(asctime)s:%(levelname)s:%(message)s'

logging.basicConfig(filename='./Basic/div.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT)

def div(a, b):
    try:
        a/b
    except ZeroDivisionError as e:
        logging.error(e)
        logging.error(e, exc_info=True) #capture the traceback in logging.error() by setting the excinfo* parameter to True
    else:
        return a/b

a=2
b=0
div_result = div(a,b)
logging.debug(f'division of {a}/{b} : {div_result}')