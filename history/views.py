from django.shortcuts import render
from .models import *


def history(request):
    context = {}
    context["a"] = "kek"
    return render(
        request,
        "history.html",
        context=context
    )
