from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "indexEU.html")

def canada(request):
    return render(request, "canada.html")

def eua(request):
    return render(request, "eua.html")