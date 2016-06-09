from flask import render_template, request, Blueprint
from app.forms import ApiSpecForm
from app.models import AppSpec

api_doc = Blueprint('api_doc', __name__, template_folder='templates')


@api_doc.route('/')
def index():
    # TODO:  Paginate
    specs = AppSpec.objects.only('app_name').all()
    return render_template('intro.html', specs=specs)


@api_doc.route('/docs/<name>')
def show(name):
    # TODO:  Handle 404s
    spec = AppSpec.objects.get(app_name=name)
    return render_template('spec.html', spec=spec)


@api_doc.route('/new', methods=['GET', 'POST'])
def new():
    form = ApiSpecForm(request.form)

    if request.method == 'POST':

        if form.validate():
            spec = AppSpec(app_name=form.app_name.data, source=form.source.data)

        # # TODO:  This should be a separate lib
        # response = requests.get(spec.source)
        #
        # if response.status_code == 200:
        #     # TODO:  Should we only assume json??
        #     spec.spec = sanitize(response.json())
        #     spec.save()
    else:
        return render_template('new.html', form=form)


