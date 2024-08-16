from django.shortcuts import render, redirect, get_object_or_404
from AppJuridica.models import Cliente
from AppJuridica.forms import ClienteFormulario
from .models import Yasoycliente
from .forms import YasoyclienteForm
from .forms import DatosdecontactoForm
from .forms import BuscarNumeroCasoForm

def inicio(request):
    return render (request, "AppJuridica/index.html")

def ServiciosJuridicos (request):
    return render ( request, "AppJuridica/Servicios Juridicos.html")

def ServiciosCiberseguridad(request):
    return render ( request,"AppJuridica/Vista Servicios Ciberseguridad.html")

def Precios(request):
    return render ( request,"AppJuridica/Precios.html")

def SobreNosotros(request):
    return render ( request,"AppJuridica/Sobre Nosotros.html")


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuariocreado = Cliente(
                usuario=informacion["usuario"],
                contraseña=informacion["contraseña"],
                numero_de_caso=informacion["numero_de_caso"]
            )
            usuariocreado.save()
            return render(request, "AppJuridica/index.html")
    else:
        mi_formulario = ClienteFormulario()

    return render(request, "AppJuridica/form-con-api.html", {"mi_formulario": mi_formulario})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Yasoycliente, pk=pk)
    if request.method == 'POST':
        form = YasoyclienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_listar')  # Redirige a una página después de guardar
    else:
        form = YasoyclienteForm(instance=cliente)
    
    return render(request, 'AppJuridica/editar_cliente.html', {'form': form})

# Vista para listar todos los clientes
def cliente_listar(request):
    clientes = Yasoycliente.objects.all()
    return render(request, 'AppJuridica/cliente_listar.html', {'clientes': clientes})

def crear_datos_contacto(request):
    if request.method == 'POST':
        form = DatosdecontactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_exito')  # Redirige a una página de éxito o a donde desees
    else:
        form = DatosdecontactoForm()
    return render(request, 'AppJuridica/crear_datos_contacto.html', {'form': form})

def pagina_exito(request):
    return render(request, 'AppJuridica/pagina_exito.html')



# Vista para buscar

def buscar_numero_caso(request):
    resultado = None
    form = BuscarNumeroCasoForm()

    if request.method == 'POST':
        form = BuscarNumeroCasoForm(request.POST)
        if form.is_valid():
            numero_de_caso = form.cleaned_data['numero_de_caso']
            try:
                resultado = Cliente.objects.get(numero_de_caso=numero_de_caso)
            except Cliente.DoesNotExist:
                resultado = None

    return render(request, 'AppJuridica/buscar_numero_caso.html', {'form': form, 'resultado': resultado})

