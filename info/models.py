from django.db import models
from django.utils.timezone import now

class TypeOfBarn(models.Model):
    list_of_types = ["откорм", "родилка", "индивидуалки", "доращивание", "хряки"]
    type = models.CharField(default=list_of_types[0], max_length=20)

    def __str__(self):
        return self.type

    @classmethod
    def create_all_types_from_list(cls):
        for type in cls.list_of_types:
            cls.objects.create(type=type)


class Barn(models.Model):
    name = models.CharField(max_length=30, default=0)
    type = models.ForeignKey(TypeOfBarn, null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.name}"
    
    def count_of_cells(self):
        return self.cell_set.count()
    
    def capacity_of_animals(self):
        capacity = 0
        for cell in self.cell_set.all():
            capacity += cell.capacity
        return capacity
    
    def count_of_all_animals(self):
        count = 0
        for cell in self.cell_set.all():
            count +=cell.count_of_animals()
        return count


class TypeOfFood(models.Model):
    list_of_foods = ["Старт", "Финиш", "Гровер", "Лактация", "Предстарт", "Супоросный"]
    type = models.CharField(default=list_of_foods[0], max_length=20)
    
    def __str__(self):
        return self.type

    @classmethod
    def create_all_types_from_list(cls):
        for type in cls.list_of_foods:
            cls.objects.create(type=type)


class Trough(models.Model):
    type_of_food = models.ForeignKey(TypeOfFood, null=True, blank=True, on_delete=models.SET_NULL)


class TypeOfCell(models.Model):
    list_of_types = ["взрослые", "доращивание", "родилка"]
    type = models.CharField(default=list_of_types[0], max_length=20)

    def __str__(self):
        return self.type

    @classmethod
    def create_all_types_from_list(cls):
        for type in cls.list_of_types:
            cls.objects.create(type=type)


class Cell(models.Model):
    barn = models.ForeignKey(Barn, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default=0)
    trough = models.ForeignKey(Trough, null=True, blank=True, on_delete=models.SET_NULL)
    capacity = models.IntegerField(default=0)  # Вместимость
    type = models.ForeignKey(TypeOfCell, null=True, blank=True, on_delete=models.SET_NULL)
    date_of_last_reweighting = models.DateField()
    last_reweighting = models.FloatField(default=0)
    date_of_last_wash = models.DateField()

    def __str__(self):
        return f"{self.number}"

    def count_of_animals(self):
        return self.animal_set.count()


class Animal(models.Model):
    cell = models.ForeignKey(Cell, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, default="")
    number_of_group = models.CharField(max_length=20, default="")
    number_of_mother = models.CharField(max_length=20, default="")
    birthday = models.DateField(auto_now=True)
    weight_of_birth = models.FloatField(default=0)
    lovely_food = models.ForeignKey(TypeOfFood, null=True, blank=True ,on_delete=models.SET_NULL)
    special_marks = models.CharField(max_length=300, default="")
    approximately_date_of_delivery = models.DateField()
    date_of_delivery = models.DateField()
    last_weight = models.FloatField(default=0)
    date_of_last_reweighting = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.number} Pig  ({self.cell.number})"




# --------------------------------------------------------
def autofilling_types():
    list_of_classes = [TypeOfBarn, TypeOfCell, TypeOfFood]
    for cls in list_of_classes:
        for ob in cls.objects.all():
            ob.delete()

    for cls in list_of_classes:
        cls.create_all_types_from_list()
