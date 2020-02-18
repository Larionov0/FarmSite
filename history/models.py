from django.db import models
from info.models import *


class History(models.Model):
    pass


class Change(models.Model):
    animals = models.ManyToManyField(Animal, blank=True, null=True)
    date = models.DateField(auto_now=True)
    total_weight = models.FloatField(default=0)
    description = models.CharField(max_length=300, default='')
    history = models.ForeignKey(History, null=True, on_delete=models.SET_NULL)


class Move(Change):
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL, related_name='all_moves_from')
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL, related_name='all_moves_to')


class Purchase(Change):
    supplier = models.CharField(max_length=50, default='')
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)


class Sale(Change):
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)
    client = models.CharField(max_length=50, default='')


class Die(Change):
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)


class Born(Change):
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)
