class BaseConfig:
    DEBUG = False
    TESTING = False
    MONGODB_URL = 'mongodb://localhost/specs'


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    MONGODB_URL = 'mongodb://localhost/specs_testing'


class ProductionConfig(BaseConfig):
    pass
