# tests/test_commands.py

import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_add_command(capsys):
    command = AddCommand()
    command.execute('2', '3')
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_add_command_random(capsys, faker):
    command = AddCommand()
    num1 = str(faker.random_number())
    num2 = str(faker.random_number())
    command.execute(num1, num2)
    captured = capsys.readouterr()
    expected_result = float(num1) + float(num2)
    assert f"Result: {expected_result}" in captured.out

def test_subtract_command(capsys):
    command = SubtractCommand()
    command.execute('5', '3')
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out

def test_multiply_command(capsys):
    command = MultiplyCommand()
    command.execute('2', '3')
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out

def test_divide_command(capsys):
    command = DivideCommand()
    command.execute('6', '3')
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out

def test_divide_by_zero_command(capsys):
    command = DivideCommand()
    command.execute('6', '0')
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out
