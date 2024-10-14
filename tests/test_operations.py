import pytest
from app.calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_add_random(faker):
    a = faker.random_number()
    b = faker.random_number()
    assert add(a, b) == a + b

def test_subtract():
    assert subtract(5, 3) == 2

def test_subtract_random(faker):
    a = faker.random_number()
    b = faker.random_number()
    assert subtract(a, b) == a - b

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_random(faker):
    a = faker.random_number()
    b = faker.random_number()
    assert multiply(a, b) == a * b

def test_divide():
    assert divide(6, 3) == 2

def test_divide_random(faker):
    a = faker.random_number()
    b = faker.random_number() or 1  # Avoid zero
    assert divide(a, b) == a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(6, 0)
