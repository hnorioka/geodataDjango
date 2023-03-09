from django.urls import path
from . import views

urlpatterns = [
    path("indexAM.html", views.index, name="index"),
    path("canada.html", views.canada, name="canada"),
    path("eua.html", views.eua, name="eua"),
    path("indexEU.html", views.voltar, name="voltar")
]