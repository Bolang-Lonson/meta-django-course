from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request:HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request:HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def menu(request:HttpRequest) -> HttpResponse:
    return render(request, 'menu.html')