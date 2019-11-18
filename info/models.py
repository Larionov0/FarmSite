from django.db import models

# Create your models here.
class Barn(models.Model):
    number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return f"{self.number}"


class Cell(models.Model):
    barn = models.ForeignKey(Barn, default=0, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default=0)
    troughmate = models.OneToOneField(Cell, blank=True)  # Сокормушечник

    def __str__(self):
        return f"{self.number}"


class Animal(models.Model):
    cell = models.ForeignKey(Cell, default=0, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return f"{self.number} Pig  ({self.cell.number})"
