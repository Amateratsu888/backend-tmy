"""This is init module."""

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

# Place where app is defined
app = Flask(__name__)

from app import routes 