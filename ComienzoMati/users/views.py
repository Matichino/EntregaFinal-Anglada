from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AppJuridica/index.html")  # Cambia 'index' por la vista a la que quieras redirigir
        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirige a la página de inicio de sesión
        msg_register = "Error en los datos ingresados"
    else:
        form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})

@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('Login')  # Redirige a una vista después de guardar
    else:
        formulario = UserEditForm(instance=usuario)

    return render(request, "users/editar_usuario.html", {"form": formulario})


class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy("EditarUsuario")

