from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Barn)
admin.site.register(Cell)
admin.site.register(Animal)
admin.site.register(Trough)

admin.site.register(TypeOfBarn)
admin.site.register(TypeOfFood)
admin.site.register(TypeOfCell)
