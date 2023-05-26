#Importar una biblioteca administradora de rutas :)
from django.urls import path

#Importanto vistas
from.import views

#Declaramos las rutas validad
urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author, name="author")
]