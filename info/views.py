from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from history.models import *  # Отседа импортируются и модели info
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
    """
    Два варианта вызова:
    - либо когда пользователь просто хочет посмотреть информацию про ячейку
    - либо когда он хочет переместить в ячейку свиней, которых мы сохранили
    в сессии заранее
    :param request:
    :param number_of_cell: какую ячейку посмотреть / в какую закинуть свинюшек
    """
    animals = request.session.get("checked_animals")

    # когда мы хотим переместить
    if animals is not None:
        request.session["checked_animals"] = None
        cell_from = Cell.objects.get(number=request.session["cell_from_number"])
        cell_to = Cell.objects.get(number=number_of_cell)
        history = History.objects.all()[0]
        change = Change.objects.create(history=history, total_weight=0, description='auto', type=ChangeType.get_by_name('Move'), from_cell=cell_from, to_cell=cell_to)

        total_weight = 0
        for animal_number in animals:
            animal = cell_from.animal_set.get(number=animal_number)
            cell_to.animal_set.add(animal)
            change.animals.add(animal)
            total_weight += animal.last_weight
        change.total_weight = total_weight
        change.save()

        return redirect('info:otkorm')

    # когда мы хотим посмотреть инфо про ячейку
    else:
        context = {}
        context["cell"] = Cell.objects.get(number=number_of_cell)

        return render(
            request,
            "cell_info.html",
            context=context
        )


def move(request, number_of_cell):
    """

    :param request:
    :param number_of_cell:
    :return:
    """
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


def animal_info(request, number_of_animal):
    pass
