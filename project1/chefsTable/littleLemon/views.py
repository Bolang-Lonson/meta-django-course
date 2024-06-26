from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu

# Create your views here.
def hello(request) -> str:
    return HttpResponse('Hello World')


def menu_by_id(request, menu_id: int) -> str:
    menu = Menu.objects.get(pk = menu_id)
    return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine")