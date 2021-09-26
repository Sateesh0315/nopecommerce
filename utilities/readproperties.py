import configparser
import os


config = configparser.RawConfigParser()
config.read("E:\Videos\Courses\Practice\GIT\automation-framework\configurations\config.ini")


class ReadConfig:
    @staticmethod
    def base_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password
