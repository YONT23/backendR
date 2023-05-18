from django.urls import path
from .views import *

urlpatterns = [
    path('pagos/', PagoAPIView.as_view(), name='pagos-list'),
]