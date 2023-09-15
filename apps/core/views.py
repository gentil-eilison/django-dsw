from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def index(request: HttpRequest):
    return HttpResponse('Hello World')