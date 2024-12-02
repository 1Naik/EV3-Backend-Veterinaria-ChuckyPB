from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from gestorProductos.models import Producto, Categoria
from django.contrib.auth.decorators import login_required, user_passes_test
from gestorProductos.forms import RegistroProductoForm, RegistroCategoriaForm



# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"

#Definir si es staff
def staff(user):
    return user.is_staff

#PRODUCTOS
#Vista para listado de productos
@login_required
def listadoProductos(request):
    if request.user.is_staff:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(creador=request.user)
    return render(request, 'gestorProductos/tabla_productos.html', {'productos':productos})

#Vista para registro (agregar) productos
@login_required
def registroProductos(request):
    if request.method == 'POST':
        form = RegistroProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creador = request.user
            producto.save()
            return redirect('productosData')
    else:
        form = RegistroProductoForm()
    return render(request, 'gestorProductos/añadir_producto.html', {'form':form})

#Vista para editar un producto
@login_required
def editarProducto(request, id):
    #Buscar el producto dentro de la base de datos con el id
    producto = Producto.objects.get(id=id)
    if producto.creador != request.user and not request.user.is_staff:
        return redirect('productosData')
    if request.method == 'POST':
        form = RegistroProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productosData')
    else:
        form = RegistroProductoForm(instance=producto)
    return render(request, 'gestorProductos/añadir_producto.html', {'form':form})

#Vista para eliminar un producto
@login_required
@user_passes_test(staff)
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productosData')

#CATEGORIAS
#Vista para listado de categorias
@login_required
@user_passes_test(staff)
def listadoCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestorProductos/tabla_categorias.html', {'categorias':categorias})


#Vista para registro (agregar) categorias
@login_required
@user_passes_test(staff)
def registroCategorias(request):
    if request.method == 'POST':
        form = RegistroCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoriasData')
    else:
        form = RegistroCategoriaForm()
    return render(request, 'gestorProductos/añadir_categoria.html', {'form':form})


#Vista para editar una categoria
@login_required
@user_passes_test(staff)
def editarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoriasData')
    else:
        form = RegistroCategoriaForm(instance=categoria)
    return render(request, 'gestorProductos/añadir_categoria.html', {'form':form})

#Vista para eliminar una categoria
@login_required
@user_passes_test(staff)
def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categoriasData')







