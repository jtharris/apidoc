import os
import sys
import yaml
from unittest import TestCase

import responses

APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
sys.path.append(APP_DIR)

from app import create_app
from app.models import AppSpec


class BaseTest(TestCase):
    uses_db = False

    def setUp(self):
        os.environ['ENV_CONFIG'] = 'test'
        self.app = create_app(init_db=self.uses_db)

        if self.uses_db:
            AppSpec.objects.delete()

    # This ensures that no real network calls will be made from any tests
    @responses.activate
    def run(self, result=None):
        super().run(result)

    @staticmethod
    def sample_swagger_spec():
        pet_store_path = os.path.join(os.path.dirname(__file__), 'data', 'petstore.yaml')
        with open(pet_store_path) as stream:
            return yaml.load(stream)
