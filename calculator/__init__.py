from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(first, second):
        calculation = Calculation(first, second, add)
        return calculation.get_ans()
    @staticmethod
    def subtract(first, second):
        calculation = Calculation(first, second, subtract)
        return calculation.get_ans
    def multiply(first, second):
        calculation = Calculation(first, second, multiply)
        return calculation.get_ans
    def divide(first, second):
        calculation = Calculation(first, second, divide)
        return calculation.get_ans