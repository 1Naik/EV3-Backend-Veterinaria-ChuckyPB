from django import forms
from gestorProductos.models import Producto, Categoria

#Clase para editar un producto
class RegistroProductoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea())
    precio = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['placeholder'] = 'Nombre del producto'
    descripcion.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['placeholder'] = 'Descripción del producto'
    precio.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['placeholder'] = 'Precio'
    categoria.widget.attrs['class'] = 'form-control'


#Clase para crear un producto
class RegistroProductoForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea())
    precio = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['placeholder'] = 'Nombre del producto'
    descripcion.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['placeholder'] = 'Descripción del producto'
    precio.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['placeholder'] = 'Precio'
    categoria.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','categoria']


#Clase para editar una categoria
class RegistroCategoriaForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea())

    nombre.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['placeholder'] = 'Nombre de la categoría'
    descripcion.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['placeholder'] = 'Descripción de la categoría'


#Clase para crear un categoria
class RegistroCategoriaForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea())

    nombre.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['placeholder'] = 'Nombre de la categoría'
    descripcion.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['placeholder'] = 'Descripción de la categoría'

    class Meta:
        model = Categoria
        fields = ['nombre','descripcion']



