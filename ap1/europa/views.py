from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "indexEU.html")

def espanha(request):
    return render(request, "espanha.html")

def franca(request):
    return render(request, "franca.html")

def italia(request):
    return render(request, "italia.html")

def voltar(request):
    return render(request, "indexAM.html")