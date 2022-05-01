# extends db base classes with additional methods
from flask_login import UserMixin
from .__db_model import *

"""
Here database model classes are extended with additional functionality.
It was created to keep actual table models from __db_model.py as simple as possible.
For example - the database doesn't need to know that the user class in the codebase
should also inherit from UserMixin
"""


class User(UserModel, UserMixin):
    def __init__(self, name, passwd):
        super().__init__(name, passwd)

    def get_id(self):
        return self.name