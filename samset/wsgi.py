"""
WSGI config for samset project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'samset.settings') 
#I have change it when I want to run from model importt *

application = get_wsgi_application()

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'samset.settings'