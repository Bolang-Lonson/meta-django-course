imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) -> HttpResponse:
    return HttpResponse('Welcome to Little Lemon restaurant')