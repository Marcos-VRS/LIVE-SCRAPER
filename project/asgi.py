import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from live_scrapper.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # HTTP protocol
        "websocket": AuthMiddlewareStack(  # WebSocket protocol
            URLRouter(websocket_urlpatterns)
        ),
    }
)
