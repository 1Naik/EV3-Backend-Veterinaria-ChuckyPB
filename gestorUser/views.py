from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib import messages
from gestorUser.forms import FormularioEditarUsuario, RegistroUsuarioForm





# Vista para la creación de usuarios.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"


#Vista para ver el listado de usuarios
def listaUsuarios(request):
    users = User.objects.all()
    data = {'users':users}
    return render(request, 'gestorUser/lista_usuarios.html', data)

#Vista para la modificación de perfiles de usuarios
def editarUsuarios(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = FormularioEditarUsuario(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            nueva_contraseña = form.cleaned_data.get('nueva_contraseña')
            if nueva_contraseña:
                user.set_password(nueva_contraseña)
            user.save()
            messages.success(request, 'Usuario actualizado con éxito')
            return redirect('login')
    else:
        form = FormularioEditarUsuario(instance=user)
    return render(request, 'gestorUser/editar_usuarios.html', {'form':form})
