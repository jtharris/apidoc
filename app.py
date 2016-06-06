import os
from flask import Flask, render_template
from mongoengine import connect, Document, StringField, DictField, URLField

app = Flask(__name__)

# TODO:  Get connection info from env
connect('specs')


class AppSpec(Document):
    app_name = StringField(required=True, unique=True)
    source = URLField(required=True)
    spec = DictField(required=True)

# TODO:  Is there a better place to initialize this?
AppSpec.create_index('app_name', background=True)


@app.route('/docs/<name>')
def spec(name):
    # TODO:  Handle 404s
    spec = AppSpec.objects.get(app_name=name)
    return render_template('spec.html', spec=spec)


@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/')
def index():
    # TODO:  Paginate
    specs = AppSpec.objects.only('app_name').all()
    return render_template('intro.html', specs=specs)


if __name__ == "__main__":
    # Dev mode
    app.run(host='0.0.0.0', port=5000)
