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
def matricula_est(request):
	return render(request,"matriculaEst.html")