from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
# Create your views here.
def test(request):
	return render(request,"principal.html", {})
def inicio(request):
	return render(request,"inicio.html", {})
def agregar_asignatura(request):
	semestre_list = semestre.objects.all()
	context = {'object_list': semestre_list}
	return render(request,"agregar_asignatura.html",context)
def ver_asignatura(request):
	 asignatura_list = asignatura.objects.all()
	 context = {'object_list': asignatura_list}
	 return render(request,"gestion_asignatura.html",context)

def insertar_asignatura(request):
	cod = request.GET.get('asig_codigo','')
	codPort = request.GET.get('asig_codigo_port','')
	nom = request.GET.get('asig_nombre','')
	semestre = request.GET.get('sem_codigo_id','')
	if cod:
		if codPort:
			if nom:
				if semestre:
					p=asignaturas(asig_codigo=cod,asig_codigo_port=codPort,asig_nombre=nom,sem_codigo_id=semestre)
					p.save()
					return render_to_response('gestion_asignatura.html',{"exito":True})							
	else:
		return render_to_response('gestion_asignatura.html')
def eliminar_asignatura(request):
	cod=request.GET.get('asig_codigo','')
	results=asignatura.objects.all().order_by('asig_codigo')
	if cod:
		p = asignatura.objects.get(id=cod)
		p.delete()
		return render_to_response('eliminar_asignatura.html',{"results": results,"cod":cod,"exito":True})
	return render_to_response('eliminar_asignatura.html',{"results": results})	
def editar_asignatura(request):
	id = request.GET.get('asig_codigo','')
	results=asignatura.objects.all().order_by('asig_codigo')
	if id: # si solo obtengo el id , mostrar el detalle
		if not request.GET.get('Codigo',''):
			if not request.GET.get('CodPor',''):
				if not request.GET.get('Nombre_asignatura',''):
					if not request.GET.get('semestre',''):
						results=asignatura.objects.filter(id=id).order_by('asig_codigo')
						return render_to_response('ver_detalle_asignatura.html',{"results":results})	 
	if id:
		if  request.GET.get('Codigo',''):
			if request.GET.get('CodPor',''):
				if request.GET.get('Nombre_asignatura',''):
					if request.GET.get('semestre',''):
						p=asignatura.objects.get(id=request.GET.get('Codigo',''))# Que registro va a actualizar
						p.asig_codigo=request.GET.get('Codigo','')
						p.asig_codigo_port=request.GET.get('asig_codigo_port','')
						p.asig_nombre=request.GET.get('Nombre_asignatura','')
						p.sem_codigo_id=request.GET.get('semestre','')	
						p.save()	
						results=asignatura.objects.all().order_by('asig_codigo')	
						return render_to_response('gestion_asignatura.html',{"results":results,"asig_codigo":id,"exito":True})					
	return render_to_response('gestion_asignatura.html',{"results":results}) 
def gestion_est(request):
	return render(request,"gestionAlumnos.html")		
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return render(request,"inicio.html", {})

    # Si llegamos al final renderizamos el formulario
    return render(request, "principal.html", {'form': form})
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

