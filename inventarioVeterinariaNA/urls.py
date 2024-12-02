"""
URL configuration for inventarioVeterinariaNA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventarioVeterinariaNA.views import index
from gestorUser.views import listaUsuarios, editarUsuarios
from gestorProductos.views import listadoProductos, listadoCategorias ,registroProductos, registroCategorias, editarCategoria, editarProducto, eliminarCategoria, eliminarProducto


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # Todas las urls de autenticación
    path("usuarios/", include("gestorUser.urls")),
    path("", index, name="home"),
    #Vistas Usuarios
    path('listaUsuarios/', listaUsuarios, name='lista_usuarios'),
    path('editarUsuarios/<int:id>/', editarUsuarios, name='editar_usuarios'),
    #Vistas Productos y Categorias
    path('productos/', listadoProductos, name='productosData'),
    path('categorias/', listadoCategorias, name='categoriasData'),
    path('nuevoProducto/', registroProductos, name='productoRegistro'),
    path('nuevaCategoria/', registroCategorias, name='categoriaRegistro'),
    path('eliminarProducto/<int:id>', eliminarProducto, name='eliminarProductos'),
    path('eliminarCategoria//<int:id>', eliminarCategoria, name='eliminarCategorias'),
    path('editarProducto/<int:id>', editarProducto, name='editarProducto'),
    path('editarCategoria/<int:id>', editarCategoria, name='editarCategoria'),
]
