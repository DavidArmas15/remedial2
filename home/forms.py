from django import forms

from .models import Equipo, Jugador, Estadio

class UpdateEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
        "user",
        "nombre",
        "evento",
        "ndueno",
        "user"
        ]

class NewEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
        "user",
        "nombre",
        "evento",
        "ndueno"
        ]

class UpdateJugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
        "equipo",
        "name",
        'last_name',
        "numero",
        "posicion",
        ]

class NewJugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
        "equipo",
        "name",
        'last_name',
        "numero",
        "posicion",
        ]



class UpdateEstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = [
        "equipo",
        "name",
        "capacidad",
        "tamano",
        ]



class NewEstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = [
        "equipo",
        "name",
        "capacidad",
        "tamano",
        ]

