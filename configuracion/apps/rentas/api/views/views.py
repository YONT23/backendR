from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.serializers import *
from rest_framework import status

class MaestraAPIView(APIView):
    def get(self, request):
        maestras = Maestra.objects.all()
        serializer = MaestraSerializer(maestras, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MaestraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        maestra = self.get_object(pk)
        serializer = MaestraSerializer(maestra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        maestra = self.get_object(pk)
        maestra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PersonaAPIView(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClienteAPIView(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PropiedadAPIView(APIView):
    def get(self, request):
        propiedades = Propiedad.objects.all()
        serializer = PropiedadSerializer(propiedades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        propiedad = self.get_object(pk)
        serializer = PropiedadSerializer(propiedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        propiedad = self.get_object(pk)
        propiedad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReseñaPropiedadAPIView(APIView):
    def get(self, request):
        reseñas = ReseñaPropiedad.objects.all()
        serializer = ReseñaPropiedadSerializer(reseñas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReseñaPropiedadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        reseña = self.get_object(pk)
        serializer = ReseñaPropiedadSerializer(reseña, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reseña = self.get_object(pk)
        reseña.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PagoAPIView(APIView):
    def get(self, request):
        pagos = Pago.objects.all()
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pago = self.get_object(pk)
        serializer = PagoSerializer(pago, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pago = self.get_object(pk)
        pago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReservacionAPIView(APIView):
    def get(self, request):
        reservaciones = Reservacion.objects.all()
        serializer = ReservacionSerializer(reservaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        reservacion = self.get_object(pk)
        serializer = ReservacionSerializer(reservacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservacion = self.get_object(pk)
        reservacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConfirmacionFacturaAPIView(APIView):
    def get(self, request):
        confirmaciones = ConfirmacionFactura.objects.all()
        serializer = ConfirmacionFacturaSerializer(confirmaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConfirmacionFacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        confirmacion = self.get_object(pk)
        serializer = ConfirmacionFacturaSerializer(confirmacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        confirmacion = self.get_object(pk)
        confirmacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
