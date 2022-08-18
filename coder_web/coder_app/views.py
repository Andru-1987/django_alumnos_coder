from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def calcular_edad(request):
    return HttpResponse("<h1>Hello world</h1>")
