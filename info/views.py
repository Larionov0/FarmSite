from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def info(request):
    context = {}
    context["count_of_animals"] = Animal.objects.count()
    context["count_of_cells"] = Cell.objects.count()
    context["count_of_barns"] = Barn.objects.count()
    return render(request, "index.html", context=context)


def lol(request):
    return HttpResponse(f"Kek {__file__}")


def otkorm(request):
    context = {}
    context["barns"] = Barn.objects.all()

    return render(
        request,
        "otkorm.html",
        context=context
    )
