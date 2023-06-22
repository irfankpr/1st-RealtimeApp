from django.urls import path
from .consumers import WSconsumer

ws_urlpatterns = [
    path("ws/start/",WSconsumer.as_asgi())
]