# config.py
import yaml

class Config:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as file:
            self._config = yaml.safe_load(file)

    def get(self, key, default=None):
        return self._config.get(key, default)

# Create a global instance of Config
config = Config()
