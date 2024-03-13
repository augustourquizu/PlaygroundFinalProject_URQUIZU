from django.db import models

class Lista(models.Model):
    descripcion = models.TextField(null=True)
    datos_extra= models.CharField(max_length=50, default='Nombre')
    dia = models.DateField()
    imagen = models.ImageField(upload_to='uploads/', null=True, blank=True)
    lugar = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.datos_extra}"
# Create your models here.
