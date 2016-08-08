from .base import *
from django.core.exceptions import ImproperlyConfigured

DEBUG = True

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )

