import configparser
import os

def load_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.ini")
    config.read(config_path)
    return config
