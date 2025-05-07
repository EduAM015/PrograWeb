"""
WSGI config for panaderia_lupita project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panaderia_lupita.settings')

application = get_wsgi_application()