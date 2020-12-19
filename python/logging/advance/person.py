import logging

LOG_FORMAT = '%(asctime)s:%(name)s:%(message)s'
FILE_NAME  = './Advance/person.log'


logger = logging.getLogger(__name__)#__name__ contains the full name of the current module, so this will simply work in any module.
logger.setLevel(logging.INFO) #setting loger to info level 

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s') # formatting logger

file_handler = logging.FileHandler(FILE_NAME)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Person:
    """A sample Person class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info(f'Created Person:{self.fullname}{self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f"{self.first}{self.last}"


emp_1 = Person('John', 'Smith')
emp_2 = Person('will', 'smith')
emp_3 = Person('Jane', 'Doe')