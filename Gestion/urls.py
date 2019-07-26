from django.urls import include, path
from Gestion import views

urlpatterns = [
	path('agregarAsignatura', views.agregar_asignatura),
	path('verAsignatura', views.ver_asignatura),
	path('insertarAsignatura', views.insertar_asignatura),
	path('eliminarAsignatura', views.eliminar_asignatura),
	path('editar_asignatura', views.editar_asignatura),
	path('gestionEst', views.gestion_est),
]