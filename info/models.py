from django.db import models

# Create your models here.
class Barn(models.Model):
    number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return f"{self.number}"


class Trough(models.Model):
    type_of_food = models.CharField(max_length=100, default="")


class Cell(models.Model):
    barn = models.ForeignKey(Barn, default=0, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default=0)
    trough = models.ForeignKey(Trough, default=0, blank=True, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.number}"


class Animal(models.Model):
    cell = models.ForeignKey(Cell, default=0, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return f"{self.number} Pig  ({self.cell.number})"
