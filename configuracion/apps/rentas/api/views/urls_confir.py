from django.urls import path
from .views import *

urlpatterns = [
    path('confirmacion/', ConfirmacionFacturaAPIView.as_view(), name='confirmacion-list'),
]