"""
ASGI config for EasyLearning project.

It exposes the ASGI callable as a modules-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyLearning.settings')

application = get_asgi_application()
