from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Menu

# Create your views here.
def about(request:HttpRequest) -> HttpResponse:
    about_content = {'about': 'Based in Chicago, Illinois, Little Lemon is a Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit ducimus omnis assumenda illum sapiente aperiam nulla. Tempora ratione dolore repudiandae nisi? Blanditiis molestias nulla iste? Quasi consequatur quos neque ipsum!'}

    return render(request, 'about.html', about_content)


# def menu(request:HttpRequest) -> HttpResponse:
#     newmenu = {'pricechart': [
#         {'name': 'falafel', 'price': '12'},
#         {'name': 'shawarma', 'price': '15'},
#         {'name': 'gyro', 'price':'10'},
#         {'name': 'hummus', 'price':'5'},
#     ]}
#     return render(request, 'menu.html', newmenu)


def menu_by_id(request:HttpRequest) -> HttpResponse:
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}

    return render(request, 'menu_cards.html', newmenu_dict)