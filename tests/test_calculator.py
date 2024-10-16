# tests/test_calculator.py

import pytest
from decimal import Decimal
from app.calculator import Calculator
from app.calculator.calculations import Calculations

def test_calculator_add():
    Calculations.clear_history()
    result = Calculator.add(Decimal('2'), Decimal('3'))
    assert result == Decimal('5')
    assert Calculations.count_history() == 1

def test_calculator_subtract():
    Calculations.clear_history()
    result = Calculator.subtract(Decimal('5'), Decimal('3'))
    assert result == Decimal('2')
    assert Calculations.count_history() == 1

def test_calculator_multiply():
    Calculations.clear_history()
    result = Calculator.multiply(Decimal('2'), Decimal('3'))
    assert result == Decimal('6')
    assert Calculations.count_history() == 1

def test_calculator_divide():
    Calculations.clear_history()
    result = Calculator.divide(Decimal('6'), Decimal('3'))
    assert result == Decimal('2')
    assert Calculations.count_history() == 1

def test_calculator_divide_by_zero():
    Calculations.clear_history()
    with pytest.raises(ValueError):
        Calculator.divide(Decimal('6'), Decimal('0'))
    assert Calculations.count_history() == 0
