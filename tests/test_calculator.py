#Test for calculator function
from calculator.calculation import Calculation
#from calculator import Calculator

def test_add():
    #Testing addition function
    assert Calculation.add(4,4) == 8

def test_sub():
    #Testing subtraction function
    assert Calculation.subtract(10,2) == 8

def test_mult():
    #Testing multiplication function
    assert Calculation.multiply(10,10) == 100

def test_div():
    #Testing division function
    assert Calculation.divide(5,5) == 1