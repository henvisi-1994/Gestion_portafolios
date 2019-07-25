from django.shortcuts import render

# Create your views here.
def test(request):
	return render(request,"principal.html", {})
def inicio(request):
	return render(request,"inicio.html", {})
def gestion_portafolio(request):
	return render(request,"gestionPortafolio.html")
def datos_informativos(request):
	return render(request,"datosInformativos.html")
def distribucion_diarios(request):
	return render(request,"distribucionDiarios.html")
def proyecto(request):
	return render(request,"proyecto.html")
def tareas_intraclase(request):
	return render(request,"intraclases.html")
def tareas_extraclase(request):
	return render(request,"extraclase.html")
def practica_laboratorio(request):
	return render(request,"practicaLaboratorio.html")
def evaluaciones(request):
	return render(request,"evaluaciones.html")
def examenes(request):
	return render(request,"examenes.html")
def anexos(request):
	return render(request,"anexos.html")
def crear_portafolios(request):
	return render(request,"crearPortafolio.html")
def eliminar_portafolios(request):
	return render(request,"eliminarPortafolio.html")
def visualizar_portafolios(request):
	return render(request,"visualizarPortafolio.html")
def matricula_est(request):
	return render(request,"matriculaEst.html")
def aulas_virtuales(request):
	return render(request,"aulasVirtuales.html")
def diarios(request):
	return render(request,"diarios.html")
def lista_diarios(request):
	return render(request,"listaDiarios.html")
def mis_port_est(request):
	return render(request,"misPortEst.html")
def gestion_est(request):
	return render(request,"gestionAlumnos.html")
