from django.urls import include, path
from GestionM import views

urlpatterns = [
    path('', views.gestion_portafolio),
    path('datosInformativos', views.datos_informativos),
    path('distribucionDiarios', views.distribucion_diarios),
    path('proyecto', views.proyecto),
    path('intraclases', views.tareas_intraclase),
    path('extraclases', views.tareas_extraclase),
    path('practicalaboratorio', views.practica_laboratorio),
    path('evaluaciones', views.evaluaciones),
    path('examenes', views.examenes),
    path('anexos', views.anexos),
    path('visualizarPortafolios', views.visualizar_portafolios),
    path('eliminarPortafolios', views.eliminar_portafolios),
    path('matriculaEst', views.matricula_est),
    path('aulasVirtuales', views.aulas_virtuales),
    path('diario', views.diarios),
    path('listaDiarios', views.lista_diarios),
    path('misPortEst', views.mis_port_est),
]