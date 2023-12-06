from django.contrib import admin

# Register your models here.
from home import models



@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "user",
        "timestamp",
        "age",
        "status"
    ]


@admin.register(models.Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "evento",
        "ndueno",
        "id"
    ]


@admin.register(models.Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "last_name",
        "numero",
        "posicion",
        "equipo",
        "id"
    ]

@admin.register(models.Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "capacidad",
        "tamano",
        "equipo",
        "id" 
    ]
