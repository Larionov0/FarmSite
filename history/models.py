from django.db import models
from info.models import *


class Change(models.Model):
    animals = models.ManyToManyField(Animal, blank=True, null=True)
    date = models.DateField(auto_now=True)
    total_weight = models.FloatField(default=0)
    description = models.CharField(max_length=300, default='')
    type = models.CharField(max_length=30, default='move', blank=True)


class Move(models.Model):
    change = models.OneToOneField(Change, on_delete=models.CASCADE)
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL, related_name='all_moves_from')
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL, related_name='all_moves_to')


class Purchase(models.Model):
    change = models.OneToOneField(Change, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=50, default='')
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)


class Sale(models.Model):
    change = models.OneToOneField(Change, on_delete=models.CASCADE)
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)
    client = models.CharField(max_length=50, default='')


class Die(models.Model):
    change = models.OneToOneField(Change, on_delete=models.CASCADE)
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)


class Born(models.Model):
    change = models.OneToOneField(Change, on_delete=models.CASCADE)
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL)


class History(models.Model):
    changes = models.ManyToManyField(Change, blank=True, null=True)
