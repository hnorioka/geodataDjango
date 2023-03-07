from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("espanha.html", views.espanha, name="espanha"),
    path("franca.html", views.franca, name="franca"),
    path("italia.html", views.italia, name="italia")
]