# tests/test_command_handler.py

import pytest
from app.commands import CommandHandler, Command

class MockCommand(Command):
    def execute(self, *args):
        print(f"MockCommand executed with args: {args}")

def test_register_command(capsys):
    handler = CommandHandler()
    handler.register_command('mock', MockCommand())
    assert 'mock' in handler.commands

def test_execute_command_known(capsys):
    handler = CommandHandler()
    handler.register_command('mock', MockCommand())
    handler.execute_command('mock arg1 arg2')
    captured = capsys.readouterr()
    assert "MockCommand executed with args: ('arg1', 'arg2')" in captured.out

def test_execute_command_unknown(capsys):
    handler = CommandHandler()
    handler.execute_command('unknown')
    captured = capsys.readouterr()
    assert "Unknown command: unknown" in captured.out

def test_execute_command_exit(capsys):
    handler = CommandHandler()
    with pytest.raises(SystemExit):
        handler.execute_command('exit')
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

def test_execute_command_empty_input(capsys):
    handler = CommandHandler()
    handler.execute_command('')
    captured = capsys.readouterr()
    assert captured.out == ''
