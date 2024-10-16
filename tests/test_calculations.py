# tests/test_calculations.py
"""
import pytest
from decimal import Decimal
from app.calculator.calculation import Calculation
from app.calculator.calculations import Calculations
from app.calculator.operations import add

def test_add_calculation():
    Calculations.clear_history()
    calc = Calculation(Decimal('2'), Decimal('3'), add)
    Calculations.add_calculation(calc)
    assert Calculations.count_history() == 1

def test_clear_history():
    Calculations.clear_history()
    assert Calculations.count_history() == 0

def test_get_last_calculation():
    Calculations.clear_history()
    calc = Calculation(Decimal('2'), Decimal('3'), add)
    Calculations.add_calculation(calc)
    last_calc = Calculations.get_last_calculation()
    assert last_calc == calc

def test_get_calculation():
    Calculations.clear_history()
    calc = Calculation(Decimal('2'), Decimal('3'), add)
    Calculations.add_calculation(calc)
    retrieved_calc = Calculations.get_calculation(0)
    assert retrieved_calc == calc

def test_calculation_history_multiple_entries():
    Calculations.clear_history()
    calc1 = Calculation(Decimal('2'), Decimal('3'), add)
    calc2 = Calculation(Decimal('5'), Decimal('4'), add)
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    assert Calculations.count_history() == 2
    assert Calculations.get_calculation(0) == calc1
    assert Calculations.get_calculation(1) == calc2
"""