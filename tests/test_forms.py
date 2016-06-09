import unittest

from tests import BaseTest
from app.forms import ApiSpecForm


class ApiSpecFormTest(BaseTest):

    @unittest.skip
    def test_valid_form(self):
        # TODO:  Mock out requests for validation
        form = ApiSpecForm(app_name='foo', source='http://foobar.com/swagger/')

        self.assertTrue(form.validate(), 'Expecting form to be valid')

    def test_invalid_url(self):
        form = ApiSpecForm(app_name='foo', source='swagger/')

        self.assertFalse(form.validate(), 'Expecting form to be invalid')

    def test_blank_url(self):
        form = ApiSpecForm(app_name='foo', source='')

        self.assertFalse(form.validate(), 'Expecting form to be invalid')

    def test_app_name_blank(self):
        form = ApiSpecForm(app_name='', source='http://swagger.edu/spec')

        self.assertFalse(form.validate(), 'Expecting form to be invalid')

    def test_app_name_is_none(self):
        form = ApiSpecForm(app_name=None, source='http://swagger.edu/spec')

        self.assertFalse(form.validate(), 'Expecting form to be invalid')
