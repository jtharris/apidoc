import os.path
import json
import yaml
from tests import BaseTest
from app.models import AppSpec


class AppSpecTest(BaseTest):
    uses_db = True

    def test_basic_write(self):
        AppSpec(
            app_name='test-app',
            source='http://dummy.url/swagger/',
            spec=json.dumps({'foo': 'bar'})
        ).save()

        self.assertEqual(1, len(AppSpec.objects))

        actual_spec = AppSpec.objects.get()
        self.assertEqual('test-app', actual_spec.app_name)
        self.assertEqual('http://dummy.url/swagger/', actual_spec.source)
        self.assertEqual('{"foo": "bar"}', actual_spec.spec)

    def test_spec_can_be_persisted(self):
        spec_text = json.dumps(self.sample_swagger_spec())

        AppSpec(
            app_name='petstore',
            source='http://petstore.com/spec',
            spec=spec_text
        ).save()

        actual_spec = AppSpec.objects.get()
        self.assertEqual(spec_text, actual_spec.spec)
