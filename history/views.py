from django.shortcuts import render
from .models import *


def history(request):
    context = {}

    return render(
        request,
        "history.html",
        context=context
    )
