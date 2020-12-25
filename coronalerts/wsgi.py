"""
WSGI config for coronalerts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys


sys.path.append('/home/matanel/coronalerts')
sys.path.append('/home/matanel/coronalerts/coronalerts')
sys.path.append('/home/matanel/coronalerts/venv/lib/python3.8/site-packages')


from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coronalerts.settings.prod')

application = get_wsgi_application()
