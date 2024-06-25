
from django import forms
from inventarioApp.models import Producto


class FormProducto(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = '__all__'
