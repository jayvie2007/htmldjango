from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hilaaw wolrd')

def brian(request):
    return HttpResponse("hello, brian")

def harry(request):
    return HttpResponse("hello, harry")

def greet(request, name):
    return HttpResponse(f"Hello {name}")
