"""
WSGI config for todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, '/opt/python/current/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feeds_service.settings")
from django.core.wsgi import get_wsgi_application



application = get_wsgi_application()
