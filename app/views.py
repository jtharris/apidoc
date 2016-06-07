import requests
from flask import render_template, request
from app import app
from app.models import AppSpec


@app.route('/docs/<name>')
def spec(name):
    # TODO:  Handle 404s
    spec = AppSpec.objects.get(app_name=name)
    return render_template('spec.html', spec=spec)


@app.route('/new', methods=['GET', 'POST'])
def new():
    # TODO:  Lots of error handling here
    if request.method == 'POST':
        spec = AppSpec(
            app_name=request.form['app-name'],
            source=request.form['source']
        )

        # TODO:  This should be a separate lib
        response = requests.get(spec.source)

        if response.status_code == 200:
            # TODO:  Should we only assume json??
            spec.spec = sanitize(response.json())
            spec.save()
    else:
        return render_template('new.html')


@app.route('/')
def index():
    # TODO:  Paginate
    specs = AppSpec.objects.only('app_name').all()
    return render_template('intro.html', specs=specs)
