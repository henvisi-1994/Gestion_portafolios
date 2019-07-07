from django.shortcuts import render

# Create your views here.
def test(request):
	return render(request,"principal.html", {})
def inicio(request):
	return render(request,"inicio.html", {})
