from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from json import dumps

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


def cell_info(request, number_of_cell):
    context = {}
    context["cell"] = Cell.objects.get(number=number_of_cell)

    return render(
        request,
        "cell_info.html",
        context=context
    )


def move(request, number_of_cell):
    print("polucheno")
    return HttpResponse(dumps({"result":True}))
