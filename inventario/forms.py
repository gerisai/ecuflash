from django import forms

from .models import Producto,Imagen

make_choices = [
    ('Chrysler', 'Chrysler'),
    ('Chevrolet', 'Chevrolet'),
    ('Ford', 'Ford')
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','marca','modelo','año','precio', 'disponible', 'imagen']
        widgets = {
            'marca': forms.Select(choices=make_choices)
        }