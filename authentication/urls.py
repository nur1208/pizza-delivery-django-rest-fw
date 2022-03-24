from django.urls import path
from .views import HELLO_AUTH_VIEW,USER_CREATE_VIEW

urlpatterns = [
    path('', HELLO_AUTH_VIEW, name="hello_auth"),
    path('signup/',USER_CREATE_VIEW , name="user_create_view"),
]