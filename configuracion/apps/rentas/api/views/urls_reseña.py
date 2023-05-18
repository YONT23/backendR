from django.urls import path
from .views import *

urlpatterns = [
    path('reseña/', ReseñaPropiedadAPIView.as_view(), name='reseña-list'),
]