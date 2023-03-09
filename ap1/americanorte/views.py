from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "indexAM.html")

def canada(request):
    return render(request, "canada.html")

def eua(request):
    return render(request, "eua.html")

def voltar(request):
    return render(request, "indexEU.html")