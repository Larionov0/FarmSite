from django.urls import path
from . import views

urlpatterns = [
    path("", views.info, name="info"),
    path("lol/", views.lol, name="lol"),
    path("otkorm/", views.otkorm, name="otkorm"),
    path("otkorm/<str:number_of_cell>", views.cell_info, name="cell_info")
]
