"""
WSGI config for sca_sybil_based_collusion_attacks.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sca_sybil_based_collusion_attacks.settings')
application = get_wsgi_application()
