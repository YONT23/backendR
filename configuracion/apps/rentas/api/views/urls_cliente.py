from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/', ClienteAPIView.as_view(), name='clientes-list'),
]