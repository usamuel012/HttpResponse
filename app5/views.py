from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def samuel(request):
    return HttpResponse('<marquee><h2>Hello world</h2></marquee')

def flint(request):
    return HttpResponse('<h><h1><h1>nope...</h1></h1></h1>')
