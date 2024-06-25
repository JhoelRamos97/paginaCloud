from django.contrib import admin
from inventarioApp.models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','stock','area']

admin.site.register(Producto, ProductoAdmin)