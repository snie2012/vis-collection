"""
WSGI config for snie_host project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# dj_static: This is a simple Django middleware utility that allows you to properly serve static assets from production with a WSGI server like Gunicorn.
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snie_host.settings")

application = Cling(get_wsgi_application())
