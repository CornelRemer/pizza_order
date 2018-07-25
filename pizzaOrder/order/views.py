from django.shortcuts import get_object_or_404  # return 404 if object dosen' exist
from rest_framework.views import APIView        # return API data
from rest_framework.response import Response    # send back specific response status (e.g. 200)
from rest_framework import status
from .models import Order
from . serializeJSON import OrderSerializer

# set as class based view
class OrderList(APIView):

    # list all orders
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    # create new order
    def post(self):
        pass