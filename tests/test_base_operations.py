# tests/test_base_operation.py

import pytest
from decimal import Decimal
from app.plugins.base_operation import BaseOperationCommand

def test_base_operation_command_execute_invalid_args(capsys):
    class TestCommand(BaseOperationCommand):
        operation = lambda a, b: a + b

    command = TestCommand()
    command.execute('1')
    captured = capsys.readouterr()
    assert "Usage: test <num1> <num2>" in captured.out

def test_base_operation_command_execute_invalid_numbers(capsys):
    class TestCommand(BaseOperationCommand):
        operation = lambda a, b: a + b

    command = TestCommand()
    command.execute('a', 'b')
    captured = capsys.readouterr()
    assert "Please enter valid numbers" in captured.out

def test_base_operation_command_execute_operation_exception(capsys):
    class TestCommand(BaseOperationCommand):
        def operation(self, a, b):
            raise ValueError("Operation error")

    command = TestCommand()
    command.execute('1', '2')
    captured = capsys.readouterr()
    assert "Error: Operation error" in captured.out
