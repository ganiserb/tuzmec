from django.db import models

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length = 40)

class Juego(models.Model):
    nombre  = models.CharField(max_length = 40)
    categoria = models.ForeignKey(Categoria)

class Servidor(models.Model):
    nombre  = models.CharField(max_length = 50)
    juego   = models.ForeignKey(Juego)
    online  = models.BooleanField()
    ip      = models.CharField(max_length = 15)
    puerto  = models.BigIntegerField()
    fechaCreacion   = models.DateTimeField()