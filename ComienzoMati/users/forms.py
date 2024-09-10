from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    

class UserEditForm(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Nombre:', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido:', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Ingrese su email:", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]