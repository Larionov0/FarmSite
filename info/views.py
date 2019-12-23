from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from json import loads

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
    request.session.clear()
    context = {}
    context["barns"] = Barn.objects.all()

    return render(
        request,
        "otkorm.html",
        context=context
    )


def cell_info(request, number_of_cell):
    animals = request.session.get("checked_animals")

    if animals is not None:
        request.session["checked_animals"] = None
        cell_from = Cell.objects.get(number=request.session["cell_from_number"])
        cell_to = Cell.objects.get(number=number_of_cell)

        for animal_number in animals:
            print(animal_number)
            animal = cell_from.animal_set.get(number=animal_number)
            cell_to.animal_set.add(animal)

        return redirect('info:otkorm')

    else:
        context = {}
        context["cell"] = Cell.objects.get(number=number_of_cell)

        return render(
            request,
            "cell_info.html",
            context=context
        )


def move(request, number_of_cell):
    animals = loads(request.GET['animals'])
    request.session['checked_animals'] = animals

    context = {}
    cell = Cell.objects.get(number=number_of_cell)
    request.session['cell_from_number'] = cell.number
    context["barns"] = Barn.objects.all()
    context["cell_from"] = cell
    context["count_of_animals"] = len(animals)
    context["rest"] = cell.count_of_animals() - len(animals)
    return render(request, 'otkorm.html', context=context)
