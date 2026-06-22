import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "config.ini"
)
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_application_URL():
        return config.get("commonInfo","baseURL")


    @staticmethod
    def get_browser():
        return config.get("commonInfo","browser")
