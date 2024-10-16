# tests/test_calculation.py

import pytest
from decimal import Decimal
from app.calculator.calculation import Calculation
from app.calculator.operations import add, subtract, multiply, divide

def test_calculation_add():
    calc = Calculation(Decimal('2'), Decimal('3'), add)
    result = calc.perform()
    assert result == Decimal('5')

def test_calculation_subtract():
    calc = Calculation(Decimal('5'), Decimal('3'), subtract)
    result = calc.perform()
    assert result == Decimal('2')

def test_calculation_multiply():
    calc = Calculation(Decimal('2'), Decimal('3'), multiply)
    result = calc.perform()
    assert result == Decimal('6')

def test_calculation_divide():
    calc = Calculation(Decimal('6'), Decimal('3'), divide)
    result = calc.perform()
    assert result == Decimal('2')

def test_calculation_divide_by_zero():
    calc = Calculation(Decimal('6'), Decimal('0'), divide)
    with pytest.raises(ValueError):
        calc.perform()

def test_calculation_create():
    calc = Calculation.create(Decimal('2'), Decimal('3'), add)
    assert isinstance(calc, Calculation)
    assert calc.perform() == Decimal('5')
