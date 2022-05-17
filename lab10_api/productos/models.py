from django.db import models

# Create your models here.

class Producto(models.Model):
    
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    
    def __str__(self) -> str:
        return self.nombre