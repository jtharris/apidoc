import os
from flask import Flask
from mongoengine import connect


def create_app(init_db=True):
    config_obj = os.environ.get('ENV_CONFIG', 'dev').capitalize() + 'Config'

    app = Flask(__name__)
    app.config.from_object('app.config.{}'.format(config_obj))

    if init_db:
        connect(host=app.config.get('MONGODB_URL'))

    from app.views import api_doc
    app.register_blueprint(api_doc)

    # TODO:  Set up defaults for 404, 500 pages
    return app
