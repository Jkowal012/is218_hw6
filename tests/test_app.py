# tests/test_app.py

import pytest
import logging
from unittest.mock import patch
from app import App

def test_app_get_environment_variable():
    app = App()
    env = app.get_environment_variable()
    assert env == 'TESTING'  # Assuming default is 'TESTING'

def test_app_start(caplog):
    app = App()
    app.load_plugins()  # Ensure plugins are loaded

    # Simulate user input
    inputs = iter(['add 2 3', 'exit'])

    def mock_input(prompt):
        return next(inputs)

    with patch('builtins.input', mock_input):
        with caplog.at_level(logging.INFO):
            with pytest.raises(SystemExit):
                app.start()
    # Check that 'Result: 5.0' is in the log output
    assert "Result: 5.0" in caplog.text
    assert "Goodbye!" in caplog.text
