"""
ASGI config for panaderia_lupita project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panaderia_lupita.settings')

application = get_asgi_application()