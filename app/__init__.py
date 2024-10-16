import os
from dotenv import load_dotenv
import logging
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        load_dotenv()
        self.settings = os.environ.copy()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.settings.setdefault('LOG_LEVEL', 'WARNING')

        # Configure logging
        log_level = self.settings.get('LOG_LEVEL', 'WARNING').upper()
        logging.basicConfig(level=getattr(logging, log_level))

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
        print("Type 'exit' to exit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())