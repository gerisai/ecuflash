from django.contrib import admin

from .models import Producto, Imagen
#from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    #form = ProductForm
    list_display = ('id','nombre', 'marca', 'año', 'disponible', 'precio')
    list_display_links = ('nombre',)
    list_filter = ('marca', 'año', 'modelo')
    search_fields = ('nombre','marca','modelo','año', 'precio')
    list_per_page = 25

admin.site.register(Producto, ProductAdmin)
admin.site.register(Imagen)
