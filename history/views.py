from django.shortcuts import render
from .models import *


def history(request):
    context = {}
    history = History.objects.all()[0]
    changes = history.changes
    context['changes'] = changes

    return render(
        request,
        "history.html",
        context=context
    )
