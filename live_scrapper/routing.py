from django.urls import path, re_path
from live_scrapper.consumers import LiveConsumer

websocket_urlpatterns = [
    re_path(
        r"^ws/live/$", LiveConsumer.as_asgi()
    ),  # re_path ao invés de path pode ajudar com compatibilidade
]
