from django.shortcuts import render
#Se importa httpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def author(request):
    return HttpResponse("Autor: Paola Huerta💁")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitilize()
    })
