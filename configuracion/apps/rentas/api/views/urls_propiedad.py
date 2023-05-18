from django.urls import path
from .views import *

urlpatterns = [
    path('propiedad/', PropiedadAPIView.as_view(), name='propiedad-list'),
]