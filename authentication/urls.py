from django.urls import path
from .views import HELLO_AUTH_VIEW

urlpatterns = [
    path('', HELLO_AUTH_VIEW, name="hello_auth"),
]