from django.shortcuts import render
#Se importa httpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hola desde mi primera vista!🥰")
def author(request):
    return HttpResponse("Autor: Paola Huerta💁")
