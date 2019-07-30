from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class usuarios(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    usr_cedula=models.CharField(primary_key=True,max_length=10)
    usr_clave=models.CharField(max_length=20)
    usr_tipo=models.CharField(max_length=10)

class persona(models.Model):
    per_nombres=models.CharField(max_length=50)
    per_apellidos=models.CharField(max_length=50)
    per_correo=models.CharField(max_length=100)
    usr_cedula=models.ForeignKey(usuarios, on_delete=models.CASCADE)

class paralelos(models.Model):
    par_codigo=models.CharField(primary_key=True,max_length=20)
    par_nombre=models.CharField(max_length=100)

class periodo(models.Model):
    per_cod=models.CharField(primary_key=True,max_length=20)
    per_nombre=models.CharField(max_length=50)

class facultades(models.Model):
    fac_codigo=models.CharField(primary_key=True,max_length=20)
    fac_nombre=models.CharField(max_length=100)

class carreras(models.Model):
    car_codigo=models.CharField(primary_key=True,max_length=20)
    carr_nombre=models.CharField(max_length=100)
    far_codigo=models.ForeignKey(facultades, on_delete=models.CASCADE)
   
class semestre(models.Model):
    sem_codigo=models.CharField(primary_key=True,max_length=20)
    sem_nombre=models.CharField(max_length=100)
    par_codigo=models.ForeignKey(paralelos, on_delete=models.CASCADE)
    car_codigo=models.ForeignKey(carreras, on_delete=models.CASCADE)
    per_cod=models.ForeignKey(periodo, on_delete=models.CASCADE)

class asignaturas(models.Model):
    asig_codigo=models.CharField(primary_key=True,max_length=20)
    asig_codigo_port=models.CharField(max_length=20)
    asig_nombre=models.CharField(max_length=100)
    sem_codigo=models.ForeignKey(semestre, on_delete=models.CASCADE)

class det_persona_asignaturas(models.Model):
    asig_codigo=models.ForeignKey(asignaturas, on_delete=models.CASCADE)
    usr_cedula=models.OneToOneField(persona,on_delete=models.CASCADE)

