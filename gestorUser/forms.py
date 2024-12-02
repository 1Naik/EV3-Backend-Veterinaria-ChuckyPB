from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    username.widget.attrs['class'] = 'form-control'
    username.widget.attrs['placeholder'] = 'Nombre de usuario'
    username.widget.attrs['autocomplete'] = 'username'
    email.widget.attrs['class'] = 'form-control'
    email.widget.attrs['placeholder'] = 'Correo electrónico'
    email.widget.attrs['autocomplete'] = 'email'
    password1.widget.attrs['class'] = 'form-control'
    password1.widget.attrs['placeholder'] = 'Contraseña'
    password1.widget.attrs['autocomplete'] = 'new-password'
    password2.widget.attrs['class'] = 'form-control'
    password2.widget.attrs['placeholder'] = 'Repetir Contraseña'
    password2.widget.attrs['autocomplete'] = 'new-password'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    


class FormularioEditarUsuario(forms.ModelForm):
    nueva_contraseña = forms.CharField(widget=forms.PasswordInput, required=False, label="Nueva Contraseña")
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput, required=False, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username','email']

    def limpiarDatos(self):
        limpiar = super().clean()
        contraseña = limpiar.get("Nueva Contraseña")
        confirmar_contraseña = limpiar.get("Confirmar Contraseña")

        if contraseña and contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return limpiar