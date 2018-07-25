# this is to save python objects as JSON
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
        #fields = ('pizza_id', 'pizza_size', 'customer_name', 'customer_address')