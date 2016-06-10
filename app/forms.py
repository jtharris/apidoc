import requests
from werkzeug.routing import ValidationError
from wtforms import Form, StringField, validators


class ApiSpecForm(Form):
    app_name = StringField(validators=[validators.data_required()])
    source = StringField(validators=[validators.url()])

    def validate_source(self, field):
        response = requests.get(field.data)

        if not response.ok:
            raise ValidationError('{} responded with status:  {}.'.format(
                response.url,
                response.status_code)
            )

        try:
            swagger_def = response.json()
        except ValueError:
            raise ValidationError('Response did not return valid JSON.')


