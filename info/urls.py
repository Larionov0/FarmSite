from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path("", views.info, name="info"),
    path("lol/", views.lol, name="lol"),
    path("otkorm/", views.otkorm, name="otkorm"),
    path("otkorm/<str:number_of_cell>", views.cell_info, name="cell_info"),
    path("otkorm/animal/<str:number_of_animal>", views.animal_info, name='animal_info'),
    path("otkorm/<str:number_of_cell>/move", views.move, name="move"),
    path("otkorm/animal/<str:number_of_animal>/change", views.animal_change, name="animal_change")
]
