from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders', views.OrderView)      #registers url with all orders ".../orders/"

urlpatterns  = [
    path('', include(router.urls))
]