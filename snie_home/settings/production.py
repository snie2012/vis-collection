from .base import *

ALLOWED_HOSTS = ['poetry-ncsu.herokuapp.com']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False
