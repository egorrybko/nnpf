"""
ASGI config for image_pnev project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

import image_pnev.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_pnev.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(
        URLRouter(
            image_pnev.routing.websocket_urlpatterns
        )
    ),
})
