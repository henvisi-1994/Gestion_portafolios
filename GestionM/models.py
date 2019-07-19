from __future__ import unicode_literals
from django.db import models
from djongo import models
from django import forms
# Create your models here.
class DatosPortafolio (models.Model):
    cod_portafolio = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)

class DatosInformativos (models.Model):
    portada = models.TextField()
    biografia = models.TextField()
    misionyvision = models.TextField()

class Intraclases (models.Model):
    nro_intraclass = models.TextField()
    url = models.TextField()
    Estado = models.TextField()

class Extraclases (models.Model):
    nro_extraclass = models.TextField()
    url = models.TextField()
    Estado = models.TextField()

class Diarios (models.Model):
    cod_estudiante = models.TextField()
    ultima_modificacion = models.TextField()
    num_diario = models.TextField()
    periodo = models.TextField()
    tiempo = models.TextField()
    fecha = models.TextField()
    docente = models.TextField()
    tema = models.TextField()
    contenidos = models.TextField()
    objetivo = models.TextField()
    actividades = models.TextField()
    estra_aprendizaje = models.TextField()
    resumen = models.TextField()
    reflexion = models.TextField()

class Proyectos (models.Model):
    enlace_drive = models.TextField()
    Estado = models.TextField()

class PracticaLaboratorio (models.Model):
    practica = models.TextField()
    url = models.TextField()
    Estado = models.TextField()

class Evaluaciones (models.Model):
    evaluacion = models.TextField()
    Estado = models.TextField()

class Examenes (models.Model):
    examen = models.TextField()
    Estado = models.TextField()

class Anexos (models.Model):
    anexo = models.TextField()
    Estado = models.TextField()

class InformeFinal (models.Model):
    informe = models.TextField()
    estado = models.TextField()
class Notificaciones (models.Model):
    cod_portafolio = models.IntegerField()
    usuario = models.IntegerField()
    estado =  models.CharField(max_length=100)
    num_diario =models. IntegerField()
    fecha = models.DateField()
    mensaje = models.CharField(max_length=100)
