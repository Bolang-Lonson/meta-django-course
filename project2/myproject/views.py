from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception:Exception) -> HttpResponse:
    return HttpResponse("404: Page Not Found! <br><br> <button href='/home/'>Go to Homepage</button>")


def home(request) -> HttpResponseNotFound:
    return HttpResponseNotFound('Little Lemon !')