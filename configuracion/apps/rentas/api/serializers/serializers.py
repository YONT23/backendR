from rest_framework import serializers
from ...models import *

class MaestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maestra
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()

    class Meta:
        model = Cliente
        fields = '__all__'


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'


class ReseñaPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseñaPropiedad
        fields = '__all__'


class ReservacionSerializer(serializers.ModelSerializer):
    cliente = PersonaSerializer()
    propiedad = PropiedadSerializer()

    class Meta:
        model = Reservacion
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'


class ConfirmacionFacturaSerializer(serializers.ModelSerializer):
    pago = PagoSerializer()
    reseña_propiedad = ReseñaPropiedadSerializer()
    reservacion = ReservacionSerializer()

    class Meta:
        model = ConfirmacionFactura
        fields = '__all__'

