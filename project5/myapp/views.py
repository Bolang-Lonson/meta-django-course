from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm

# Create your views here.
def home(request) -> HttpResponse:
    return HttpResponse(DemoForm())