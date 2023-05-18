from django.db import models

class Maestra(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return f"Código: {self.codigo}"

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    tipo_documento = models.ForeignKey(Maestra, on_delete=models.CASCADE, related_name='personas')
    numero_identidad = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Cliente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.persona)
    
class Propiedad(models.Model):
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    costnoche = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    reglas = models.TextField()
    tipo_propiedad = models.ForeignKey(Maestra, on_delete=models.CASCADE, related_name='propiedades')
    tipo_ciudad = models.ForeignKey(Maestra, on_delete=models.CASCADE, related_name='propiedades_ciudad')
    detalles = models.ForeignKey(Maestra, on_delete=models.CASCADE, related_name='propiedades_detalles')

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}"
    
class ReseñaPropiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    comentarios = models.TextField()
    rating = models.IntegerField()
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    estatus = models.CharField(max_length=20)

    def __str__(self):
        return f"Reseña de {self.propiedad} - Rating: {self.rating}"
    
class Reservacion(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    cantidad_noches = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservación de {self.cliente} en {self.propiedad}"
    
class Pago(models.Model):
    total = models.DecimalField(max_digits=8, decimal_places=2)
    status_pago = models.CharField(max_length=20)
    fecha_pago = models.DateField()
    metodo_pago = models.ForeignKey(Maestra, on_delete=models.CASCADE, related_name='pagos')

    def __str__(self):
        return f"Pago de {self.total} - {self.status_pago}"
    
class ConfirmacionFactura(models.Model):
    fecha_emision = models.DateField()
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    reseña_propiedad = models.ForeignKey(ReseñaPropiedad, on_delete=models.CASCADE)
    reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Confirmación de factura ({self.id})"