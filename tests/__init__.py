import os
import sys
from unittest import TestCase

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
