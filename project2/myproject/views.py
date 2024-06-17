from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

def handler404(request:HttpRequest, exception:Exception) -> HttpResponse:
    return HttpResponse("404: Page Not Found! <br><br> <a href='/home/'><button>Go to Homepage</button></a>")


def home(request) -> HttpResponseNotFound:
    return HttpResponseNotFound('Little Lemon !')