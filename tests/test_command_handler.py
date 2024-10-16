# tests/test_command_handler.py

import pytest
import logging
from app.commands import CommandHandler, Command

class MockCommand(Command):
    def execute(self, *args):
        logging.info(f"MockCommand executed with args: {args}")

def test_register_command():
    handler = CommandHandler()
    handler.register_command('mock', MockCommand())
    assert 'mock' in handler.commands

def test_execute_command_known(caplog):
    handler = CommandHandler()
    handler.register_command('mock', MockCommand())
    with caplog.at_level(logging.INFO):
        handler.execute_command('mock arg1 arg2')
    assert "MockCommand executed with args: ('arg1', 'arg2')" in caplog.text

def test_execute_command_unknown(caplog):
    handler = CommandHandler()
    with caplog.at_level(logging.WARNING):
        handler.execute_command('unknown')
    assert "Unknown command: unknown" in caplog.text

def test_execute_command_exit(caplog):
    handler = CommandHandler()
    with caplog.at_level(logging.INFO):
        with pytest.raises(SystemExit):
            handler.execute_command('exit')
    assert "Goodbye!" in caplog.text

def test_execute_command_empty_input(caplog):
    handler = CommandHandler()
    handler.execute_command('')
    # No logs should be captured for empty input
    assert caplog.text == ''
