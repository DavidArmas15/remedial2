from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings
from .models import *
from .forms import *


class Index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request):
        self.context = {
            "equipos": Equipo.objects.all()
        }
        return render(request, self.template_name, self.context)
    

#
#PRODUCT 
#

class Equipoo(generic.View):
    template_name = "home/product/product.html"
    context = {}
    def get(self, request):
        self.context = {
            "Equipo": Equipo.objects.all()
        }
        return render(request, self.template_name, self.context)
    
class DetailEquipo(generic.DetailView):
    template_name = "home/product/detail_product.html"
    model = Equipo

class UpdateEquipo(generic.UpdateView):
    template_name = "home/product/update_planes.html"
    model = Equipo
    form_class = UpdateEquipoForm
    success_url = reverse_lazy("home:product")

class DeleteEquipo(generic.DeleteView):
    template_name = "home/product/delete_product.html"
    model = Equipo
    success_url = reverse_lazy("home:product")

class NewEquipo(generic.CreateView):
    template_name = "home/product/newproduct.html"
    model = Equipo
    form_class = NewEquipoForm
    success_url = reverse_lazy("home:product")


#
#CATEGORIA 
#
class Jugador(generic.View):
    template_name = "home/category.html"
    context = {}
    def get(self, request):
        self.context = {
            "jugador": Jugador.objects.all()
        }
        return render(request, self.template_name, self.context)
    
class DetailJugador(generic.DetailView):
    template_name = "home/detail_category.html"
    model = Jugador

class UpdateJugador(generic.UpdateView):
    template_name = "home/update_category.html"
    model = Jugador
    form_class = UpdateJugadorForm
    success_url = reverse_lazy("home:category")

class DeleteJugador(generic.DeleteView):
    template_name = "home/delete_category.html"
    model = Jugador
    success_url = reverse_lazy("home:category")

class NewJugador(generic.CreateView):
    template_name = "home/newcategory.html"
    model = Jugador
    form_class = NewJugadorForm
    success_url = reverse_lazy("home:category")

#
#ACCESORIOS
#
class Estadio(generic.View):
    template_name = "home/accesorios.html"
    context = {}

    def get(self, request):
        self.context = {
            "Estadio": Estadio.objects.all()
        }
        return render(request, self.template_name, self.context)

class DetailEstadio(generic.DetailView):
    template_name = "home/detail_accesorios.html"
    model = Estadio

class UpdateEstadio(generic.UpdateView):
    template_name = "home/update_accesorios.html"
    model = Estadio
    form_class = UpdateEstadioForm
    success_url = reverse_lazy("home:accesorios")

class DeleteEstadio(generic.DeleteView):
    template_name = "home/delete_accesorios.html"
    model = Estadio
    success_url = reverse_lazy("home:accesorios")

class NewEstadio(generic.CreateView):
    template_name = "home/newaccesorios.html"
    model = Estadio
    form_class = NewEstadioForm
    success_url = reverse_lazy("home:accesorios")


