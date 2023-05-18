from django.urls import path
from .views import *

urlpatterns = [
    path('reserva/', ReservacionAPIView.as_view(), name='reserva-list'),
]