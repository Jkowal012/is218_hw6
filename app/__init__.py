# app/__init__.py

import os
from dotenv import load_dotenv
import logging
import pkgutil
import importlib

load_dotenv()

# Configure logging at the module level
log_level = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.WARNING),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        # Access settings from environment or use default values
        self.settings = os.environ.copy()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        # Configure other app components
        self.command_handler = CommandHandler()

        # Configure logging within the class, if needed
        log_level = self.settings.get('LOG_LEVEL', 'WARNING').upper()
        logging.getLogger().setLevel(getattr(logging, log_level, logging.WARNING))

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
        print("Type 'exit' to exit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())
