from unittest import TestCase
from app.models import AppSpec


class AppSpecTest(TestCase):

    def setUp(self):
        AppSpec.objects.delete()

    def test_basic_write(self):
        AppSpec(
            app_name='test-app',
            source='http://dummy.url/swagger/',
            spec={'foo': 'bar'}
        ).save()

        self.assertEqual(1, len(AppSpec.objects))

        actual_spec = AppSpec.objects.get()
        self.assertEqual('test-app', actual_spec.app_name)
        self.assertEqual('http://dummy.url/swagger/', actual_spec.source)
        self.assertEqual({'foo': 'bar'}, actual_spec.spec)

    def test_refs_can_be_persisted(self):
        pass
