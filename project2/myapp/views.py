from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) -> HttpResponse:
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20
    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User_agent: {user_agent}
        <br>Path_info: {path_info}
        <br>Response header: {response.headers}
    """
    
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


def menuitems(request, dish:str) -> HttpResponse:
    items = {
        'pasta': 'Pasta is a type of noodle made from a combination of wheat, water or eggs.',
        'falafel': 'Falafel are deep fried patties or balls made from',
        'cheesecake': 'Cheesecake is a type of dessert made with cream, soft cheese on top of cookie, pastry crust or graham cracker and fruit sauce topping.'
    }

    description = items[dish]
    
    return HttpResponse(f'<h2> {dish} </h2>' + description)