# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

#Test for calculator function
from calculator.operations import add, multiply, subtract, divide

def test_add():
    #Testing addition function
    assert add(4,4) == 8

def test_sub():
    #Testing subtraction function
    assert subtract(10,2) == 8

def test_mult():
    #Testing multiplication function
    assert multiply(10,10) == 100

def test_div():
    #Testing division function
    assert divide(5,5) == 1
    