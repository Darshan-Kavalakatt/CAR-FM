import os
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://filefish:filefish@sediment:5432/sediment'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')