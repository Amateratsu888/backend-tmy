"""This module is to configure app to connect with database."""

from pymongo import MongoClient
from os import environ 


DATABASE = MongoClient()['tmyDB'] # DB_NAME
DEBUG = True
client = MongoClient(environ.get('MONGO_URI'))