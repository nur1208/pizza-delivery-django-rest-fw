from django.urls import path
from .views import HELLO_ORDER_VIEW

urlpatterns = [
    path('', HELLO_ORDER_VIEW, name="hello_order"),
]