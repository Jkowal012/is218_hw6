# tests/test_calculations.py

import pytest
from decimal import Decimal
from faker import Faker
from app.calculator.calculation import Calculation
from app.calculator.calculations import Calculations
from app.calculator.operations import add, subtract, multiply, divide

faker = Faker()

@pytest.fixture(autouse=True)
def clear_calculation_history():
    # Automatically clear the calculation history before each test
    Calculations.clear_history()

def test_add_calculation():
    num1 = Decimal(faker.random_number())
    num2 = Decimal(faker.random_number())
    calc = Calculation(num1, num2, add)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_history()[0] == calc

def test_get_history():
    num1 = Decimal(faker.random_number())
    num2 = Decimal(faker.random_number())
    num3 = Decimal(faker.random_number())
    num4 = Decimal(faker.random_number())
    calc1 = Calculation(num1, num2, add)
    calc2 = Calculation(num3, num4, subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    history = Calculations.get_history()
    assert len(history) == 2
    assert history == [calc1, calc2]

def test_clear_history():
    num1 = Decimal(faker.random_number())
    num2 = Decimal(faker.random_number())
    calc = Calculation(num1, num2, add)
    Calculations.add_calculation(calc)
    assert len(Calculations.get_history()) == 1
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest():
    num1 = Decimal(faker.random_number())
    num2 = Decimal(faker.random_number())
    num3 = Decimal(faker.random_number())
    num4 = Decimal(faker.random_number())
    calc1 = Calculation(num1, num2, add)
    calc2 = Calculation(num3, num4, subtract)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    latest = Calculations.get_latest()
    assert latest == calc2

def test_get_latest_empty():
    assert Calculations.get_latest() is None

def test_find_by_operation():
    num1 = Decimal(faker.random_number())
    num2 = Decimal(faker.random_number())
    num3 = Decimal(faker.random_number())
    num4 = Decimal(faker.random_number())
    num5 = Decimal(faker.random_number())
    num6 = Decimal(faker.random_number())
    
    calc1 = Calculation(num1, num2, add)
    calc2 = Calculation(num3, num4, subtract)
    calc3 = Calculation(num5, num6, add)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    Calculations.add_calculation(calc3)
    
    add_operations = Calculations.find_by_operation("add")
    subtract_operations = Calculations.find_by_operation("subtract")
    
    assert len(add_operations) == 2
    assert calc1 in add_operations and calc3 in add_operations
    assert calc2 not in add_operations
    assert len(subtract_operations) == 1
    assert calc2 in subtract_operations
