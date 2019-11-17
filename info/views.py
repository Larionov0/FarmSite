from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def info(request):
    lst = []
    for i in range(100):
        lst.append(i)
    return HttpResponse(f"Hello!!! {lst}")


def lol(request):
    return HttpResponse(f"Kek {__file__}")
