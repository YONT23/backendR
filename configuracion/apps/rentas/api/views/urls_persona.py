from django.urls import path
from .views import *

urlpatterns = [
    path('personas/', PersonaAPIView.as_view(), name='personas-list'),
]