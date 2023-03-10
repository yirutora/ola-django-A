from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>olha se voce nao me ama entao nao me ligue</h1><h2>Caneta.azul,azul caneta</h2>")