"""
ASGI config for testapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from .middleware.middleware import JWTAuthMiddleware
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from chat.consumer import ChatConsumer
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': JWTAuthMiddleware(
        URLRouter([
            path('ws', ChatConsumer.as_asgi())
        ])
    )
})