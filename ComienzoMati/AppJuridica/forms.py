from django import forms
from .models import Yasoycliente
from .models import Datosdecontacto



class ClienteFormulario(forms.Form):
    usuario = forms.CharField(label="Nombre de Usuario", max_length=8)
    contraseña = forms.CharField(label="Contraseña", max_length=8)
    numero_de_caso = forms.IntegerField(label="Número de Caso")


class YasoyclienteForm(forms.ModelForm):
    class Meta:
        model = Yasoycliente
        fields = ['nombre', 'apellido', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }

class DatosdecontactoForm(forms.ModelForm):
    class Meta:
        model = Datosdecontacto
        fields = ['nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }       


class BuscarNumeroCasoForm(forms.Form):
    numero_de_caso = forms.IntegerField(label='Número de Caso', widget=forms.NumberInput(attrs={'class': 'form-control'}))


