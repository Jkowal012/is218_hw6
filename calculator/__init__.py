# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

# Do the work, create the methods
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
# Creating the methods
class Calculator:
    @staticmethod
    def add(first, second):
        calculation = Calculation(first, second, add)
        return calculation.get_ans()
    @staticmethod
    def subtract(first, second):
        calculation = Calculation(first, second, subtract)
        return calculation.get_ans
    @staticmethod
    def multiply(first, second):
        calculation = Calculation(first, second, multiply)
        return calculation.get_ans
    @staticmethod
    def divide(first, second):
        calculation = Calculation(first, second, divide)
        return calculation.get_ans
    