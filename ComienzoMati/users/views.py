from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from users.models import Avatar

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
        formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if formulario.is_valid():

            if formulario.is_valid():
                if formulario.cleaned_data.get ("imagen"):
                    avatar = Avatar (user= usuario, imagen = formulario.cleaned_data.get ("imagen"))
                    #usuario.avatar.imagen = formulario.cleaned_data.get ("imagen")
                    avatar.save ()

            formulario.save()
            return redirect('Login')  # Redirige a una vista después de guardar
    else:
        formulario = UserEditForm(instance=usuario)

    return render(request, "users/editar_usuario.html", {"form": formulario})


class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy("EditarUsuario")

def lista_usuarios(request):
    usuarios = User.objects.all()  # Obtén todos los usuarios registrados
    return render(request, 'users/lista_usuarios.html', {'usuarios': usuarios})

def editar_usuario_admin(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UserRegisterForm(instance=usuario)
    return render(request, 'users/editar_usuario_admin.html', {'form': form, 'usuario': usuario})