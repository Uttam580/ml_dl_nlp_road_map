import logging
import math
import person

LOG_FORMAT  = '%(asctime)s:%(name)s:%(message)s'
FILE_NAME = './Advance/div.log'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# defining file handlers with level and dformatter
file_handler = logging.FileHandler(FILE_NAME)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)


# for stream handling , will give output over console
#stream_handler = logging.StreamHandler()
#stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
#logger.addHandler(stream_handler)

def div(a, b):
    try:
        a/b
    except ZeroDivisionError as e:
        logger.exception('Tried to divide by zero')
    else:
        return a/b

a=2
b=0
div_result = div(a,b)
logger.debug(f'division of {a}/{b} : {div_result}')