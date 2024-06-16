from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def say_hello(request) -> HttpResponse:
    return HttpResponse('Hello World')


def homepage(request) -> HttpResponse:
    return HttpResponse('Welcome to Little Lemon!')


def display_date(request) -> HttpResponse:
    date_joined = datetime.today().year
    return HttpResponse(date_joined)


def menu(request) -> HttpResponse:
    text = """
        <h1 style="color: #f4ce14;">
            This is Little Lemon again!
        </h1>
    """
    return HttpResponse(text)