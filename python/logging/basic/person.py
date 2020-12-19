import logging

LOG_FORMAT = '%(levelname)s:%(message)s'
FILE_NAME  = './Basic/person.log'

logging.basicConfig(filename=FILE_NAME,
                     level=logging.INFO,
                    format=LOG_FORMAT)

class Person:
    """A sample Person class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logging.info(f'Created Person:{self.fullname}{self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f"{self.first}{self.last}"


emp_1 = Person('John', 'Smith')
emp_2 = Person('will', 'smith')
emp_3 = Person('Jane', 'Doe')