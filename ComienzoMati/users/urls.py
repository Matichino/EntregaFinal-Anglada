from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from .views import lista_usuarios, register
from .views import editar_usuario_admin


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppJuridica/index.html'), name="Logout"),
    path('editar_usuario/', views.editar_usuario, name='EditarUsuario'),
    path('cambiar_pass/', views.CambiarPassView.as_view(), name="CambiarPass"),
    path('lista_usuarios/', lista_usuarios, name='listausuarios'),
    path('usuarios/editar/<int:pk>/', editar_usuario_admin, name='editar_usuario'),
    
]
