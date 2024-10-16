# tests/test_commands.py

import pytest
import logging
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.commands import CommandHandler

def test_add_command(caplog):
    command = AddCommand()
    with caplog.at_level(logging.INFO):
        command.execute('2', '3')
    assert "Result: 5.0" in caplog.text

def test_add_command_random(caplog, faker):
    command = AddCommand()
    num1 = str(faker.random_number())
    num2 = str(faker.random_number())
    expected_result = float(num1) + float(num2)
    with caplog.at_level(logging.INFO):
        command.execute(num1, num2)
    assert f"Result: {expected_result}" in caplog.text

def test_subtract_command(caplog):
    command = SubtractCommand()
    with caplog.at_level(logging.INFO):
        command.execute('5', '3')
    assert "Result: 2.0" in caplog.text

def test_multiply_command(caplog):
    command = MultiplyCommand()
    with caplog.at_level(logging.INFO):
        command.execute('2', '3')
    assert "Result: 6.0" in caplog.text

def test_divide_command(caplog):
    command = DivideCommand()
    with caplog.at_level(logging.INFO):
        command.execute('6', '3')
    assert "Result: 2.0" in caplog.text

def test_divide_by_zero_command(caplog):
    command = DivideCommand()
    with caplog.at_level(logging.ERROR):
        command.execute('6', '0')
    assert "Error: Cannot divide by zero" in caplog.text
