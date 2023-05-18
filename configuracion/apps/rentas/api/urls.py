from django.urls import path, include
from .views import *

urlpatterns = [
    path('maestras/', include('apps.rentas.api.views.urls_maestra')),
    path('personas/', include('apps.rentas.api.views.urls_persona')),
    path('clientes/', include('apps.rentas.api.views.urls_cliente')),
    path('propiedad/', include('apps.rentas.api.views.urls_propiedad')),
    path('reseñapro/', include('apps.rentas.api.views.urls_reseña')),
    path('reservacion/', include('apps.rentas.api.views.urls_reserva')),
    path('pago/', include('apps.rentas.api.views.urls_pago')),
    path('confirmacionf/', include('apps.rentas.api.views.urls_confir')),
]