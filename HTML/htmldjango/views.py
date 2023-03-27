from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "htmldjango/index.html")

def brian(request):
    return HttpResponse("hello, brian")

def harry(request):
    return HttpResponse("hello, harry")

def greet(request, name):
    return render(request, "htmldjango/greet.html",{
        "name": name.capitalize()
    })
