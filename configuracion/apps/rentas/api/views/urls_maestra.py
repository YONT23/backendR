from django.urls import path
from .views import *

urlpatterns = [
    path('maestras/', MaestraAPIView.as_view(), name='maestra-list'),
]