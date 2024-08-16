from django.db import models

# Create your models here.
class Cliente(models.Model):
    usuario = models.CharField(max_length=8)
    contraseña= models.CharField(max_length=8)
    numero_de_caso= models.IntegerField()

    
    def __str__(self):
            return "{} | ID: {}" .format (self.usuario, self.id)
    

class Yasoycliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Datosdecontacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=30)

class ProgramarCita(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_cita = models.DateField()
    confirmar= models.BooleanField()