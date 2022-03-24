from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    # size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    flavour=serializers.CharField(max_length=40)
    size = serializers.ChoiceField(choices = Order.PIZZA_SIZES)
    
    class Meta:
        model=Order 
        fields=['order_status', 'size', 'quantity','flavour']

class UpdateOrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    # size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField(required=False)
    flavour=serializers.CharField(max_length=40,required=False)
    size = serializers.ChoiceField(choices = Order.PIZZA_SIZES,
        required=False)
    
    class Meta:
        model=Order 
        fields=['order_status', 'size', 'quantity','flavour']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.ChoiceField(choices = Order.ORDER_STATUSES)

    class Meta:
        model=Order
        fields=['order_status']

