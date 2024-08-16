from django.urls import path, include
from vbc import views


urlpatterns = [
    path('yasoycliente/listar', views.YasoyclienteListView.as_view(), name='ListaYasoycliente'),
    path('yasoycliente/<pk>', views.YasoyclienteDeleteView.as_view(), name='YasoyclienteBorrar'),
    path('yasoycliente/<pk>/actualizar', views.YasoyclienteUpdateView.as_view(), name='ActualizaYasoycliente')

]
