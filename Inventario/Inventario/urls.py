
from django.contrib import admin
from django.urls import path

from inventarioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('delete/<int:id>', views.eliminarProducto),
    path('editar/<int:id>', views.editarProducto),
]
