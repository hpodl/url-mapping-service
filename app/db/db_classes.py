# extends db base classes with additional methods
from .__db_model import *

class User(UserModel):
    def __init__(self, name, passwd):
        super().__init__(name, passwd)
        self.is_authenticated = False
        self.is_active = True
        self.is_anonymous = False

    def get_id(self):
        return self.name

    def log_in(self):
        self.is_authenticated = True

    def log_out(self):
        self.is_authenticated = False
    