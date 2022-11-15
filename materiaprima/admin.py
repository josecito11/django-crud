from django.contrib import admin
from .models import Produccin, materiaprima, Inventario, Entrada, Salida
# Register your models here.
admin.site.register(Produccin)
admin.site.register(materiaprima)
admin.site.register(Inventario)
admin.site.register(Entrada)
admin.site.register(Salida)