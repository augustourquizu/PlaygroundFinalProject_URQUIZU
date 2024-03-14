from django.db import models
import datetime
class Lista(models.Model):
    descripcion = models.TextField(null=True)
    nombre= models.CharField(max_length=50, default='')
    dia = models.DateField(default=datetime.date.today)
    imagen = models.ImageField(upload_to='uploads/', null=True, blank=True)
    lugar = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}"
# Create your models here.
