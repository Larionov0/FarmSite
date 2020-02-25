from django.db import models
from info.models import *


class History(models.Model):
    pass


class ChangeType(models.Model):
    name = models.CharField(max_length=20, default='')

    @classmethod
    def get_by_name(cls, name):
        return cls.objects.get(name=name)

    def __str__(self):
        return self.name


class Change(models.Model):
    animals = models.ManyToManyField(Animal, blank=True, null=True)
    date = models.DateField(auto_now=True)
    total_weight = models.FloatField(default=0)
    description = models.CharField(max_length=300, default='')
    history = models.ForeignKey(History, null=True, on_delete=models.SET_NULL)
    from_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL, related_name='all_moves_from')
    to_cell = models.ForeignKey(Cell, null=True, on_delete=models.SET_NULL, related_name='all_moves_to')
    partner = models.CharField(max_length=50, default='', blank=True)
    type = models.ForeignKey(ChangeType, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.type.name} ({self.id})"
