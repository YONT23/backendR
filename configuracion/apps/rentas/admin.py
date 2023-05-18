from django.contrib import admin
from .models import Pago, Propiedad, Persona, Maestra, Cliente, ReseñaPropiedad, Reservacion, ConfirmacionFactura

admin.site.register(Pago)
admin.site.register(Propiedad)
admin.site.register(Persona)
admin.site.register(Maestra)
admin.site.register(Cliente)
admin.site.register(ReseñaPropiedad)
admin.site.register(Reservacion)
admin.site.register(ConfirmacionFactura)
