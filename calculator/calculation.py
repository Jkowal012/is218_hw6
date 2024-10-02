# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

class Calculation:
    def __init__(self,first, second, operation):
        self.first = first
        self.second = second
        self.operation = operation

    def get_ans(self):
        return self.operation(self.first, self.second)
