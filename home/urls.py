from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.shortcuts import render
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),

    path('estadio/', views.Estadio.as_view(), name="estadio"),
    path('new/estadio/', views.NewEstadio.as_view(), name="newestadio"),
    path('update/estadio/<int:pk>/', views.UpdateEstadio.as_view(), name="update_estadio"),
    path('detail/estadio/<int:pk>/', views.DetailEstadio.as_view(), name="detail_estadio"),
    path('delete/estadio/<int:pk>/', views.DeleteEstadio.as_view(), name="delete_estadio"),
    
    path('jugador/', views.Jugador.as_view(), name="jugador"),
    path('new/jugador/', views.NewJugador.as_view(), name="newjugador"),
    path('update/jugador/<int:pk>/', views.UpdateJugador.as_view(), name="update_jugador"),
    path('detail/jugador/<int:pk>/', views.DetailJugador.as_view(), name="detail_jugador"),
    path('delete/jugador/<int:pk>/', views.DeleteJugador.as_view(), name="delete_jugador"),
    
    path('equipo/', views.Equipoo.as_view(), name="equipo"),
    path('nueva/equipo/', views.NewEquipo.as_view(), name="newequipo"),
    path('update/equipo/<int:pk>/', views.UpdateEquipo.as_view(), name="update_equipo"),
    path('detail/equipo/<int:pk>/', views.DetailEquipo.as_view(), name="detail_equipo"),
    path('delete/equipo/<int:pk>/', views.DeleteEquipo.as_view(), name="delete_equipo"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)