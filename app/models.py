from mongoengine import Document, StringField, URLField


class AppSpec(Document):
    app_name = StringField(required=True, unique=True)
    source = URLField(required=True)

    # The initial approach was to make this a DictField to
    # allow searching, but there turned out to be too much
    # special casing to convert swagger into something that
    # mongodb accepts as a document.  Punting for now - but
    # we could introduce a mapping function to convert swagger
    # into something mongo can work with.
    spec = StringField(required=True)

    meta = {'indexes': ['app_name']}
