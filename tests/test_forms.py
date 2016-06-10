import json
import responses

from tests import BaseTest
from app.forms import ApiSpecForm


class ApiSpecFormTest(BaseTest):
    SPEC_URL = 'http://foobar.com/spec/'

    def create_response(self, url=SPEC_URL, spec_text=None, content_type='application/json', status=200):
        if spec_text is None:
            spec_text = json.dumps(self.sample_swagger_spec())

        responses.add(
            method=responses.GET,
            url=url,
            body=spec_text,
            content_type=content_type,
            status=status
        )

    def test_valid_form(self):
        self.create_response()
        form = ApiSpecForm(app_name='foo', source=self.SPEC_URL)

        self.assertTrue(form.validate(), form.errors)

    def test_invalid_url(self):
        form = ApiSpecForm(app_name='foo', source='swagger/')

        self.assertFalse(form.validate(), 'Expecting form to be invalid')

    def test_blank_url(self):
        form = ApiSpecForm(app_name='foo', source='')

        self.assertFalse(form.validate(), 'Expecting form to be invalid')

    def test_source_url_not_found(self):
        self.create_response(status=404)
        form = ApiSpecForm(app_name='foo', source=self.SPEC_URL)

        self.assertFalse(form.validate(), form.errors)
        self.assertListEqual(form.source.errors, ['http://foobar.com/spec/ responded with status:  404.'])

    def test_malformed_json_content_type(self):
        self.create_response(spec_text='<html>Not JSON</html>')
        form = ApiSpecForm(app_name='foo', source=self.SPEC_URL)

        self.assertFalse(form.validate(), form.errors)
        self.assertListEqual(form.source.errors, ['Response did not return valid JSON.'])

    def test_app_name_blank(self):
        self.create_response()
        form = ApiSpecForm(app_name='', source=self.SPEC_URL)

        self.assertFalse(form.validate(), 'Expecting form to be invalid')

    def test_app_name_is_none(self):
        self.create_response()
        form = ApiSpecForm(app_name=None, source=self.SPEC_URL)

        self.assertFalse(form.validate(), 'Expecting form to be invalid')
