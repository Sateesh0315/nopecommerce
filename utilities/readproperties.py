import configparser
import os

ini_file = os.path.abspath(os.path.dirname(".\\..\configurations\."))
config = configparser.RawConfigParser()
config.read(ini_file + "\config.ini")


class ReadConfig:
    @staticmethod
    def base_url():
        base_url = config.get('common info', 'baseURL')
        return base_url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
