from django.db import models
from info.models import *


class Change(models.Model):
    animals = models.ManyToManyField(Animal, blank=True, null=True)
    date = models.DateField(auto_now=True)
    total_weight = models.FloatField(default=0)
    description = models.CharField(max_length=300, default='')


class Move(Change):
    from_ = models.ForeignKey(Cell, on_delete=models.SET_NULL)
    to = models.ForeignKey(Cell, on_delete=models.SET_NULL)


class Purchase(Change):
    supplier = models.CharField(max_length=50, default='')
    to = models.ForeignKey(Cell, on_delete=models.SET_NULL)


class Sale(Change):
    from_ = models.ForeignKey(Cell, on_delete=models.SET_NULL)
    client = models.CharField(max_length=50, default='')


class Die(Change):
    from_ = models.ForeignKey(Cell, on_delete=models.SET_NULL)


class Born(Change):
    to = models.ForeignKey(Cell, on_delete=models.SET_NULL)
