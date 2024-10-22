# app/__init__.py

import os
from dotenv import load_dotenv
import logging
import pkgutil
import importlib

# Load environment variables from .env
load_dotenv()

# Remove all handlers associated with the root logger object
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging
log_level = os.environ.get('LOG_LEVEL', 'WARNING').upper()
numeric_level = getattr(logging, log_level, logging.WARNING)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(numeric_level)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logging.txt', mode='w')  # 'w' to overwrite the file each time
file_handler.setLevel(numeric_level)
file_handler.setFormatter(formatter)

# Get the root logger
logger = logging.getLogger()
logger.setLevel(numeric_level)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        # Access settings from environment or use default values
        self.settings = os.environ.copy()
        self.settings.setdefault('ENVIRONMENT', 'DEVELOPMENT')

        # Configure other app components
        self.command_handler = CommandHandler()

    def get_environment_variable(self, envvar: str = 'ENVIRONMENT'):
        return self.settings.get(envvar)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        package = importlib.import_module(plugins_package)
        package_path = package.__path__
        for finder, plugin_name, is_pkg in pkgutil.iter_modules(package_path):
            if is_pkg:
                module_name = f'{plugins_package}.{plugin_name}'
                plugin_module = importlib.import_module(module_name)
                if hasattr(plugin_module, 'plugin_name') and hasattr(plugin_module, 'plugin_class'):
                    command_name = plugin_module.plugin_name
                    command_class = plugin_module.plugin_class
                    if issubclass(command_class, Command):
                        self.command_handler.register_command(command_name, command_class())

    def start(self):
        self.load_plugins()
        logging.info("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            self.command_handler.execute_command(user_input)
