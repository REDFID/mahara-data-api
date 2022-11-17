import os

DEBUG = 1
VERSION = os.getenv('VERSION')
SECRET_KEY = os.getenv('SECRET_KEY')
REDIS_URL = os.getenv('REDIS_URL')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
