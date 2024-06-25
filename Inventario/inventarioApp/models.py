from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=70)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()  # Convertir nombre a MAYUSCULA antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    stock = models.IntegerField()

    area_choices = (
    ('COCINA', 'Cocina'),
    ('ASEO', 'Aseo'),
    ('COMEDOR', 'Comedor')
    )
    area = models.CharField(max_length = 10, choices = area_choices)
