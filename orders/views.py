from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your views here.

class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message":"hello order"}, 
                        status=status.HTTP_200_OK)
        
HELLO_ORDER_VIEW = HelloOrderView.as_view()


class OrderView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        orders=Order.objects.all()

        serializer=self.serializer_class(instance=orders,
            many=True)

        return Response(data=serializer.data,
            status=status.HTTP_200_OK)
    
    def post(self,request):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,
                status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)     
ORDER_VIEW = OrderView.as_view()

class OrderIdView(generics.GenericAPIView):
    serializer_class=serializers.UpdateOrderSerializer
    permission_classes=[IsAuthenticated]
    # queryset = Order.objects.all()

    def get(self, request,order_id):


        order=get_object_or_404(Order,pk=order_id)

        
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,
            status=status.HTTP_200_OK)

    def put(self,request,order_id):
        
        order=get_object_or_404(Order,pk=order_id)
        
        serializer=self.serializer_class(instance=order,
            data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,
                status=status.HTTP_200_OK)

        return Response(data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,order_id):        
        order =get_object_or_404(Order,id=order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
ORDER_ID_VIEW = OrderIdView.as_view()

class UpdateOrderStatusView(generics.GenericAPIView):
    serializer_class=serializers.OrderStatusUpdateSerializer
    permission_classes=[IsAuthenticated, IsAdminUser]

    def put(self, request,order_id):
        order=get_object_or_404(Order,pk=order_id)

        serializer=self.serializer_class(instance=order,
            data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK,
                data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors)

UPDATE_ORDER_STATUS_VIEW = UpdateOrderStatusView.as_view()


class UserOrdersView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)

        orders=Order.objects.all().filter(customer=user)

        serializer=self.serializer_class(instance=orders,
            many=True)

        return Response(data=serializer.data,
            status=status.HTTP_200_OK)

USER_ORDER_VIEW = UserOrdersView.as_view()

class UserOrderDetailView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)

        order=Order.objects.all().filter(customer=user).get(pk=order_id)
        print(order)

        serializer=self.serializer_class(instance=order,)

        return Response(data=serializer.data,
            status=status.HTTP_200_OK)

USER_ORDER_DETAIL_VIEW = UserOrderDetailView.as_view()