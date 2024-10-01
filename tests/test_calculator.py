#Test for /calculator/__init__.py
from calculator import add, subtract

def test_add():
    #Testing addition function
    assert add(2,2) == 4

def test_sub():
    #Testing subtraction function
    assert subtract(2,2) == 0
