# tests/test_base_operation.py

import pytest
import logging
from app.plugins.base_operation import BaseOperationCommand

def test_base_operation_command_execute_invalid_args(caplog):
    class TestCommand(BaseOperationCommand):
        operation = lambda a, b: a + b

    command = TestCommand()
    with caplog.at_level(logging.WARNING):
        command.execute('1')
    assert "Usage: test <num1> <num2>" in caplog.text

def test_base_operation_command_execute_invalid_numbers(caplog):
    class TestCommand(BaseOperationCommand):
        operation = lambda a, b: a + b

    command = TestCommand()
    with caplog.at_level(logging.ERROR):
        command.execute('a', 'b')
    assert "Please enter valid numbers" in caplog.text

def test_base_operation_command_execute_operation_exception(caplog):
    class TestCommand(BaseOperationCommand):
        def operation(self, a, b):
            raise ValueError("Operation error")

    command = TestCommand()
    with caplog.at_level(logging.ERROR):
        command.execute('1', '2')
    assert "Error: Operation error" in caplog.text
