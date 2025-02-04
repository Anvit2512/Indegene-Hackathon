from django.urls import path
from .views import chatbot_response, chatbot_home

urlpatterns = [
    path("", chatbot_home, name="chatbot_home"),
    path("chat/", chatbot_response, name="chatbot_response"),
]
