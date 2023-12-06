from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, null=False, blank=False)
    bio = models.TextField(max_length=256, default="I Love This APP")
    timestamp = models.DateField(auto_now_add=True)
    age = models.IntegerField(default=18)
    weight = models.FloatField(default=50.45)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=16)



    def __str__(self):
        return self.name

class Equipo(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=32, default="Equipo")
    evento = models.CharField(max_length=32, default="Evento")
    ndueno = models.CharField(max_length=100, default="Nombre del dueño")

    def __str__(self):
        return self.nombre




class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default="Nombre")
    last_name = models.CharField(max_length=32, default="Apellido")
    numero = models.DecimalField(max_digits=7, decimal_places=2)
    posicion = models.CharField(max_length=32, default="Posición")

    def __str__(self):
        return self.name

    
class Estadio(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default="Nombre")
    capacidad = models.DecimalField(max_digits=10, decimal_places=2)
    tamano = models.TextField(max_length=150, default="Tamaño")
    
    def __str__(self):
        return self.name

