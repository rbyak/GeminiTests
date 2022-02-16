import string
from random import choices


class RandomAlphaNumeric():
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @staticmethod
    def random_str(length):
        rand_str = ''.join(choices(string.ascii_uppercase +
                                   string.digits, k=length))
        return rand_str
