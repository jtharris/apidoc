import requests
from werkzeug.routing import ValidationError
from wtforms import Form, StringField, validators


class ApiSpecForm(Form):
    app_name = StringField(validators=[validators.data_required()])
    source = StringField(validators=[validators.url()])

    def validate_source(self, field):
        response = requests.get(field)

        if not response.ok:
            raise ValidationError('The URL did not respond with 200 OK')

