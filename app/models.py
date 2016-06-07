from mongoengine import Document, StringField, DictField, URLField


class AppSpec(Document):
    app_name = StringField(required=True, unique=True)
    source = URLField(required=True)
    spec = DictField(required=True)

    meta = {'indexes': ['app_name']}


# TODO:  Have this be a model hook?
def sanitize(spec):
    if '$ref' in spec:
        spec['{ref}'] = spec['$ref']
        del spec['$ref']

    for key, val in spec.items():
        if isinstance(val, dict):
            spec[key] = sanitize(val)

    return spec
