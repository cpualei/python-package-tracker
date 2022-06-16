import os
from os import environ


class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')

