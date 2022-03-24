from django.urls import path
from .views import HELLO_ORDER_VIEW, ORDER_VIEW, \
ORDER_ID_VIEW,UPDATE_ORDER_STATUS_VIEW,USER_ORDER_VIEW, USER_ORDER_DETAIL_VIEW

urlpatterns = [
    path('', ORDER_VIEW, name="order_view"),
    path('<int:order_id>/', ORDER_ID_VIEW, name="order_id_view"),
    path('update-status/<int:order_id>/',
        UPDATE_ORDER_STATUS_VIEW,name='update_order_status'),
    path('user/<int:user_id>/',USER_ORDER_VIEW,
        name='user_order_view'),
    path('user/<int:user_id>/order/<int:order_id>/',
        USER_ORDER_DETAIL_VIEW,name='user_order_detail'),
    path('hello/', HELLO_ORDER_VIEW, name="hello_order"),

]