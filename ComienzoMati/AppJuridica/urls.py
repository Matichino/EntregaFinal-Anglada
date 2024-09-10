from django.urls import path
from AppJuridica import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('Servicios Juridicos/', views.ServiciosJuridicos, name= "Servicios Juridicos"),
    path('Servicios Ciberseguridad/', views.ServiciosCiberseguridad, name= "Servicios Ciberseguridad"),
    path('Precios/', views.Precios, name= "Precios"),
    path('Sobre Nosotros/', views.SobreNosotros, name= "Sobre Nosotros")
    
]

Formularios = [
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('editar-cliente/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/', views.cliente_listar, name='cliente_listar'),
    path('crear-datos-contacto/', views.crear_datos_contacto, name='crear_datos_contacto'),
    path('pagina_exito/', views.pagina_exito, name='pagina_exito'), 
    path('buscar-numero-caso/', views.buscar_numero_caso, name='buscar_numero_caso'),
    
        

]

urlpatterns += Formularios