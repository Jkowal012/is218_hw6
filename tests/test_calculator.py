#Test for calculator function
from calculator import Calculator

def test_add():
    #Testing addition function
    assert Calculator.add(4,4) == 8

def test_sub():
    #Testing subtraction function
    assert Calculator.subtract(10,2) == 8

def test_mult():
    #Testing multiplication function
    assert Calculator.multiply(10,10) == 100

def test_div():
    #Testing division function
    assert Calculator.divide(5,5) == 1