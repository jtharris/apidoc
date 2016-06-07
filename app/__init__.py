import os
from flask import Flask
from mongoengine import connect

CONFIG_OBJ = os.environ.get('ENV_CONFIG', 'dev').capitalize() + 'Config'

app = Flask(__name__)
app.config.from_object('config.{}'.format(CONFIG_OBJ))

# TODO:  Skip connection for unit tests...
connect(host=app.config.get('MONGODB_URL'))

# TODO:  Set up defaults for 404, 500 pages

from . import views
