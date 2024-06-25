from django.shortcuts import render, redirect
from django.contrib import messages
from inventarioApp.models import Producto
from inventarioApp.forms import FormProducto

# Create your views here.

def index(req):
    productos = Producto.objects.all()
    
    form = FormProducto()
    data = {'productos' : productos, 'form' : form}

    if req.method == "POST":
        form = FormProducto(req.POST)
        if form.is_valid():
            form.save()
        
        form = FormProducto()

        return redirect(index)

    return render(req,'index.html', data)


def eliminarProducto(req, id):
    prod = Producto.objects.get(id = id)
    prod.delete()
    return redirect(index)

def editarProducto(req, id):


    prod = Producto.objects.get(id = id)
    form = FormProducto(instance=prod)


    if req.method == "POST":
        form = FormProducto(req.POST, instance=prod)
        if form.is_valid():
            form.save()
            return index(req)

    data = {'form' : form}
    return render(req,'editar.html', data)