from django.views.generic import ListView, DeleteView, UpdateView
from AppJuridica.models import Yasoycliente
from django.urls import reverse_lazy

class YasoyclienteListView(ListView):
    model = Yasoycliente
    context_object_name = 'Yasoyclientes'
    template_name = 'vbc/lista_yasoycliente.html'

class YasoyclienteDeleteView(DeleteView):
    model = Yasoycliente
    template_name = 'vbc/yasoycliente_borrar.html'
    success_url = reverse_lazy('ListaYasoycliente')

class YasoyclienteUpdateView(UpdateView):
    model = Yasoycliente
    template_name = 'vbc/actualiza_yasoycliente.html'
    success_url = reverse_lazy('ListaYasoycliente')
    fields = ['nombre', 'apellido']




